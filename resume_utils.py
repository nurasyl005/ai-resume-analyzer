import PyPDF2
import os
from openai import OpenAI

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text):
    # Create OpenAI client when the function is called
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""
    You are a career advisor AI. Analyze the following resume and:
    - Identify the main skills
    - Suggest 5 missing in-demand skills
    - Recommend job roles this resume fits best
    - Suggest improvements to the resume

    Resume:
    {resume_text}
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": "write a haiku about ai"}
        ]
    )

    return completion.choices[0].message.content
