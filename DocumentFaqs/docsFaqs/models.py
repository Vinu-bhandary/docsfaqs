from django.db import models
from django.core.validators import FileExtensionValidator

valid = FileExtensionValidator(['pdf','docx'])
class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.FileField(upload_to="documents/", validators=[valid])
    uploaded_by = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="faqs")
    question = models.TextField()
    answer = models.TextField()
    generated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FAQ for {self.document.title}"
