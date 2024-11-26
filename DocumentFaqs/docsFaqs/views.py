# from django.shortcuts import render
# from langchain.chat_models import ChatGooglePalm
# from langchain.prompts import PromptTemplate
# from .models import FAQ

# def generate_faqs(document):
#     # Initialize Google Gemini via LangChain
#     chat = ChatGooglePalm(api_key="your-google-gemini-api-key")

#     # Create a prompt for FAQ generation
#     prompt_template = PromptTemplate(
#         input_variables=["content"],
#         template="Generate FAQs for the following content: {content}",
#     )
#     prompt = prompt_template.format(content=document.content)
    
#     # Get the FAQ response
#     response = chat.predict(prompt)
#     faqs = response.split("\n")  # Assuming responses are newline-separated
    
#     for faq in faqs:
#         if "Q:" in faq and "A:" in faq:
#             question, answer = faq.split("A:", 1)
#             question = question.replace("Q:", "").strip()
#             FAQ.objects.create(
#                 document=document,
#                 question=question,
#                 answer=answer.strip(),
#             )
from pathlib import Path
from main import settings
from docx import Document as DocxDocument
import fitz  # PyMuPDF for PDF reading

def extract_file_content(content):
    """
    Extract text content from PDF or DOCX file.

    Args:
    - file_path (str): Path to the uploaded file.

    Returns:
    - str: Extracted text content.
    """
    
    file_path = str(settings.BASE_DIR) + "\\media\\" + content.name
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        # Extract content from PDF
        text = ""
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text()
        return text

    elif ext == ".docx":
        # Extract content from DOCX
        doc = DocxDocument(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        raise ValueError("Unsupported file format.")
