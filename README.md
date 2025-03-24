# Document FAQ Generator

## Overview
This project is a Django-based backend API that allows document management and automatic FAQ generation using LangChain with Google Gemini.

## Features
- **Document Management**: Upload, update, delete, and list documents.
- **FAQ Generation**: Automatically generate FAQs using Google Gemini when a document is uploaded.
- **User Access**: Users can view available documents and FAQs.
- **Admin Authentication**: Basic authentication is required for admin actions.

## Tech Stack
- **Django**: Web framework
- **Django-Ninja**: API framework
- **SQLite**: Database for simplicity
- **LangChain**: Integrating AI-powered FAQ generation
- **Google Gemini**: AI model for FAQ generation

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- API key for Google Gemini

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Vinu-bhandary/docsfaqs.git
   cd docsfaqs
   ```
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run Server**
   ```bash
   python manage.py runserver
   ```
6. **Access API Documentation**
   - Open [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)

---

## API Endpoints

### **Admin Actions (Requires Authentication)**

#### 1. Add Document
- **Endpoint:** `POST /api/admin/add-document`
- **Authentication:** Basic Auth
- **Request Parameters:**
  ```json
  {
    "title": "Sample Document",
    "description": "Description of the document",
    "content": "Actual document content"
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "message": "Document added and FAQs generated."
  }
  ```

#### 2. Update Document
- **Endpoint:** `PUT /api/admin/update-document/{doc_id}`

#### 3. Delete Document
- **Endpoint:** `DELETE /api/admin/delete-document/{doc_id}`

#### 4. List Documents
- **Endpoint:** `GET /api/admin/list-documents`

---

### **User Actions**

#### 1. View Documents
- **Endpoint:** `GET /api/user/view-documents`

#### 2. View FAQs for a Document
- **Endpoint:** `GET /api/user/view-faqs/{doc_id}`

---

## Validation & Error Handling
- **Validation:**
  - Ensure valid document format.
  - Prevent duplicate or empty FAQs.
- **Error Handling:**
  - Invalid document format
  - Missing fields
  - FAQ generation failures
  - Unauthorized access

