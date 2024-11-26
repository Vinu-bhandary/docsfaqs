from ninja import Router, File, Form
from ninja.files import UploadedFile
from django.core.exceptions import ValidationError
from pathlib import Path
from .models import Document
from django.core.files.storage import default_storage
from .views import extract_file_content
from main import settings



def validate_file(uploaded_file):
    """
    Validate uploaded file format.
    """
    allowed_extensions = [".pdf", ".docx"]
    ext = Path(uploaded_file.name).suffix.lower()
    if ext not in allowed_extensions:
        raise ValidationError("Unsupported file format. Only PDF and DOCX are allowed.")

from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from .models import Document, FAQ
from django.shortcuts import get_object_or_404
from .faq_generator import generate_faqs
from .utils import extract_text_from_pdf  # Assuming the function is defined in utils.py
from django.core.files.storage import default_storage, FileSystemStorage

api = NinjaAPI()
""""""

@api.get("/documents/")
def list_documents(request):
    documents = Document.objects.all().values('id', 'title', 'description', 'upload_date')
    return list(documents)


@api.post("/documents/")
def add_document(
    request,
    title: str,
    description: str,
    uploaded_by: str,
    file: UploadedFile = File(...),
):
    """
    Upload a PDF document, extract content, generate FAQs, and save to the database.
    """
    # try:
    # Save the uploaded file to default storage
    fs = FileSystemStorage(location='media')
    filename = fs.save(file.name, file)
    document_path = fs.url(filename)
    # document_path = default_storage.save(file.name, file)
    #print(f'{document_path=}')
    # Extract text content from the uploaded PDF
    content = extract_file_content(file)

    
    if not content:
        return {"error": "Failed to extract content from the document."}, 400

    # Save the document to the database
    document = Document.objects.create(
        title=title,
        description=description,
        content=content,
        uploaded_by=uploaded_by
    )
    
    # Generate FAQs using the content
    faqs = generate_faqs(content)
    
    #print(f'{faqs=}')

    # # Save each FAQ to the database
    for faq in faqs:
        FAQ.objects.create(
            document=document,
            question=faq['question'],
            answer=faq['answer']
        )
        

    return {"success": True, "document_id:": document.id}   # HTTP 201 Created

    # except Exception as e:
        # return {"error": str(e)}, 400  # HTTP 400 Bad Request
from .schemas import FAQSchema
from django.http import JsonResponse
@api.get("/documents/{document_id}/faqs/",response=FAQSchema)
def get_faqs(request, document_id: int):
    
  
    document = get_object_or_404(Document, id=document_id)
    #faqs = document.faqs.values('question', 'answer', 'generated_date')
    faqs=get_object_or_404(FAQ,document=document)
   # faqs = document.faqs.values('question', 'answer', 'generated_date')
    print(f"FAQs for document {document_id}: {faqs}")  # Debug log

    #return faqs
    #return JsonResponse(faqs,safe=False)
    return {
  "question": faqs.question,
  "answer": faqs.answer
}
    
    
    

@api.put("/documents/{document_id}/")
def update_document(
    request, 
    document_id: int, 
    title: str = None, 
    description: str = None, 
    content: str = None
):
   
    document = get_object_or_404(Document, id=document_id)
    if title:
        document.title = title
    if description:
        document.description = description
    if content:
        document.content = content
        document.faqs.all().delete()  # Delete old FAQs
        faqs = generate_faqs(content)  # Generate new FAQs
        for faq in faqs:
            FAQ.objects.create(document=document, question=faq['question'], answer=faq['answer'])
    document.save()
    return {"success": True}

@api.delete("/documents/{document_id}/")
def delete_document(request, document_id: int):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return {"success": True}