from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import os

# Init Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("podcast-summaries")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Init LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

def retrieve_and_respond(query: str, llm, top_k: int = 5):
    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings,
        namespace="summaries"
    )

    results = vector_store.similarity_search(query=query, k=top_k)

    combined_context = "\n\n".join([
        f"Title: {doc.metadata.get('podcast_title', '')}\nSummary:\n{doc.page_content}"
        for doc in results
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

    final_prompt = prompt_template.format(context=combined_context, question=query)
    return llm.invoke(final_prompt)

