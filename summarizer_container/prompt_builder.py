def build_prompt(params):
    prompt = f"""
    **Task:**  
    Extract key highlights and useful technical resources from the following text.

    **Instructions:**  
    - Read the provided text carefully.  
    - Identify and summarize the most important points as bullet-point highlights.  
    - Extract any mentioned technical resources (tools, frameworks, papers, links, or references) and describe their relevance.  
    - Format the response as follows:

    ---
    ### **Output Format:**
    **Highlights:**
    - [Summarized key point 1]  
    - [Summarized key point 2]  
    - [Summarized key point 3]  

    **Resources:**
    - **[Resource Name]**: Can be used for [specific purpose or function].  
    - **[Resource Name]**: Helps with [specific task or topic].  

    ---
    **Text to analyze:**  
    \"\"\"  
    {params['text']}  
    \"\"\"  
    """
    return prompt