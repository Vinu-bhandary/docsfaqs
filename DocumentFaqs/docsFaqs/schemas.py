from ninja import Schema
from datetime import datetime

class DocumentSchema(Schema):
    title: str
    description: str
    content: str
    uploaded_file: str
    uploaded_by: str

class FAQSchema(Schema):
    id: int
    document_id: int
    question: str
    answer: str
    generated_date: datetime
