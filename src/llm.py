import os
from dotenv import load_dotenv


def get_llm():
    """
    Load settings from .env and create a chat LLM.

    Reads:
        LLM_PROVIDER — "openai" or "gemini" (default: openai)
        OPENAI_API_KEY — required when provider is openai
        OPENAI_MODEL — OpenAI model name (default: gpt-4o-mini)
        GEMINI_API_KEY — required when provider is gemini
        GEMINI_MODEL — Gemini model name (default: gemini-2.0-flash)

    Returns:
        A chat model ready for tool calling (ChatOpenAI or ChatGoogleGenerativeAI).

    Example:
        llm = get_llm()
        reply = llm.invoke("Hello!")
        print(reply.content)
    """
    
    load_dotenv()
    
    provider = os.getenv("LLM_PROVIDER","groq").strip().lower()
    
    if provider == "groq" :
        return _create_groq_llm()
    if provider == "gemini" :
        return _create_gemini_llm()
    
    raise ValueError(
        f'Unknown LLM_PROVIDER: "{provider}."'
        'Use "groq" or "gemini" in your .env file.'
    )
    

def _create_groq_llm():
    """
    Create a ChatGroq client using the Groq API key from .env.

    Returns:
        ChatGroq: A Groq chat model instance.

    Raises:
        ValueError: If GROQ_API_KEY is missing.
    """
    from langchain_groq import ChatGroq

    api_key = os.getenv("GROQ_API_KEY", "").strip()

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Add it to your .env file when LLM_PROVIDER=groq."
        )

    model = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-120b"
    ).strip()

    llm = ChatGroq(
        model=model,
        api_key=api_key,
        temperature=0,
    )

    return llm


def _create_gemini_llm():
    """
    Create a ChatGoogleGenerativeAI client using the Gemini API key from .env.

    Returns:
        ChatGoogleGenerativeAI: A Gemini chat model instance.

    Raises:
        ValueError: If GEMINI_API_KEY is missing.
    """
    
    from langchain_google_genai import ChatGoogleGenerativeAI

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Add it to your .env file when LLM_PROVIDER=gemini."
        )

    model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash").strip()

    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=api_key,
        temperature=0,
    )
    return llm





       