from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import os
import toml
config = toml.load(".streamlit/secrets.toml")
import os
# load_dotenv()

os.environ["OPENAI_API_KEY"] = config["openai"]["api_key"]
os.environ["PINECONE_API_KEY"] = config["pinecone"]["api_key"]
os.environ["mongodb_uri"] = config["mongodb"]["uri"]

# from dotenv import load_dotenv
# load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("podcast-summaries")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

def retrieve_and_respond(query: str, llm, top_k: int = 5, min_score: float = 0.30):
    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings,
        namespace="summaries"
    )

    # Direct similarity search with scores
    results_with_scores = vector_store.similarity_search_with_score(query=query, k=top_k)

    # Filter by score
    high_score_docs = []
    metadata_list = []

    for doc, score in results_with_scores:
        if score >= min_score:
            high_score_docs.append(doc)
            metadata_list.append(doc.metadata)

    # if not high_score_docs:
    #     return "I couldn't find anything relevant in the podcast summaries.", []

    context = "\n\n".join([
        f"Title: {doc.metadata.get('podcast_title', '')}\nSummary:\n{doc.page_content}"
        for doc in high_score_docs
    ])


    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are an expert AI analyst.\n\n"
            "Based on the following podcast summaries:\n\n"
            "{context}\n\n"
            "Answer the question below using only the information above.\n"
            "Be accurate, concise, and clear.\n\n"
            "Question: {question}"
        )
    )

    final_prompt = prompt_template.format(context=context, question=query)
    return llm.invoke(final_prompt).content, metadata_list
