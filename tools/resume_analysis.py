from utils.token_counter import count_tokens


def resume_analysis(llm, documents):
    print("Resume analysis tool called")

    resume_text = "\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
    Analyze this resume.

    Provide:

    ## Strengths
    ## Weaknesses
    ## Suggestions

    Resume:
    {resume_text}
    """
    print("Resume Analysis Tokens:", count_tokens(prompt))
    response = llm.invoke(prompt)

    #print("=== TOOL OUTPUT ===")
    #print(response.content[:500])

    return response.content