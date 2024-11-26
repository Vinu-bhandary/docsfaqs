"""
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import DocumentLoader
from google.auth import load_credentials_from_file

def generate_faqs(content: str):
    # Setup LangChain and Google Gemini integration
    loader = DocumentLoader.from_text(content)
    chain = load_qa_chain(model="google-gemini", credentials=load_credentials_from_file("path/to/google_credentials.json"))

    # Process content
    qa_pairs = chain.run(loader)
    return [{"question": qa['question'], "answer": qa['answer']} for qa in qa_pairs]

from langchain.document_loaders import TextLoader  # Adjust based on your document type

def generate_faqs(document_path):
    loader = TextLoader(document_path)  # Adjust loader usage accordingly
    documents = loader.load()
    # Process documents to generate FAQs
    return documents


from django.conf import settings

API_KEY = settings.GEMINI_API_KEY



from langchain.document_loaders import TextLoader  # Adjust loader usage
#from langchain.document_loaders import DocumentLoader
from google.auth import load_credentials_from_file
from langchain.chains.question_answering import load_qa_chain

def generate_faqs(content):
    

    
    loader = TextLoader(content)
    documents = content
    # return process_with_google_gemini(documents)  # Replace with actual API call
    #chain = load_qa_chain(model="google-gemini", credentials=load_credentials_from_file("path/to/google_credentials.json"))

    # Process documents to generate FAQs
    chain = load_qa_chain(
            model="google-gemini",
            credentials=load_credentials_from_file("path/to/google_credentials.json")
        )

    # Process content
    qa_pairs = chain.run(content)
    return [{"question": qa['question'], "answer": qa['answer']} for qa in qa_pairs]
"""
"""
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    """
"""
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content

# Rest of the FAQ generation logic...
from django.conf import settings
API_KEY = settings.GEMINI_API_KEY
from langchain.document_loaders import TextLoader
from google.auth import load_credentials_from_file
from langchain.chains.question_answering import load_qa_chain

def generate_faqs(content):
    """
  
"""
    # Initialize document loader with the content
    loader = TextLoader(content)
    
    # Load Google Gemini credentials
    credentials = load_credentials_from_file("path/to/google_credentials.json")

    # Load QA Chain
    chain = load_qa_chain(
        model="google-gemini",
        credentials=credentials
    )

    # Generate FAQs
    qa_pairs = chain.run(content)
   

    return [{"question": qa['question'], "answer": qa['answer']} for qa in qa_pairs]
"""
# from main import settings
# from langchain_community.document_loaders import TextLoader
# from langchain.chains import RetrievalQA
# from langchain_community.llms import HuggingFaceHub 

# def generate_faqs(content):
#     """
#     Generates FAQs from given content using a language model.

#     Args:
#         content: The text content to generate FAQs from.

#     Returns:
#         A list of dictionaries, each containing a question and its answer.
#     """

#     # Load the document
#     file_path = str(settings.BASE_DIR) + "\\media\\" + content.name
#     loader = TextLoader(file_path)
#     documents = loader.load()

#     # Initialize the language model
#     llm = HuggingFaceHub(repo_id="google/flan-t5-xxl")  # Replace with your preferred model

#     # Create a retrieval QA chain
#     qa_chain = RetrievalQA.from_llm(llm=llm, retriever=documents.as_retriever())

#     # Generate FAQs
#     qa_pairs = []
#     for query in ["What is the main topic?", "What are the key points?", "What are some potential questions and answers?"]:
#         result = qa_chain.run(query)
#         qa_pairs.append({"question": query, "answer": result})

#     return qa_pairs

# from langchain_community.document_loaders import TextLoader
# from langchain.chains import RetrievalQA
# from langchain_community.llms import HuggingFaceHub
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import OpenAIEmbeddings

# def generate_faqs(content):
#     """
#     Generates FAQs from given text content using a language model.

#     Args:
#         content: The plain text content to generate FAQs from.

#     Returns:
#         A list of dictionaries, each containing a question and its answer.
#     """

#     # Load the text content into a document format
#     from langchain.schema import Document
#     document = Document(page_content=content)

#     # Create a vector store retriever for the document
#     embeddings = OpenAIEmbeddings()  # You can replace with other embeddings if preferred
#     vector_store = FAISS.from_documents([document], embeddings)
#     retriever = vector_store.as_retriever()

#     # Initialize the language model
#     llm = HuggingFaceHub(repo_id="google/flan-t5-xxl")  # Replace with your preferred model

#     # Create a retrieval QA chain
#     qa_chain = RetrievalQA.from_llm(llm=llm, retriever=retriever)

#     # Generate FAQs
#     qa_pairs = []
#     for query in ["What is the main topic?", "What are the key points?", "What are some potential questions and answers?"]:
#         result = qa_chain.run(query)
#         qa_pairs.append({"question": query, "answer": result})

#     return qa_pairs


# from langchain.chains import RetrievalQA
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_community.llms import VertexAI
# from langchain.schema import Document

# def generate_faqs(content):
#     """
#     Generates FAQs from given text content using Google Gemini.

#     Args:
#         content: The plain text content to generate FAQs from.

#     Returns:
#         A list of dictionaries, each containing a question and its answer.
#     """

#     # Load the text content into a document format
#     document = Document(page_content=content)

#     # Create a vector store retriever for the document
#     embeddings = OpenAIEmbeddings()  # Replace with preferred embedding model
#     vector_store = FAISS.from_documents([document], embeddings)
#     retriever = vector_store.as_retriever()

#     # Initialize the Google Gemini LLM via Vertex AI
#     llm = VertexAI(model="text-bison", temperature=0.7)  # Adjust the model and parameters as needed

#     # Create a retrieval QA chain
#     qa_chain = RetrievalQA.from_llm(llm=llm, retriever=retriever)

#     # Generate FAQs
#     qa_pairs = []
#     for query in ["What is the main topic?", "What are the key points?", "What are some potential questions and answers?"]:
#         result = qa_chain.run(query)
#         qa_pairs.append({"question": query, "answer": result})

#     return qa_pairs


from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import VertexAI
from langchain.schema import Document

def generate_faqs(content):
    """
    Generates FAQs from given text content using Google Gemini via Vertex AI.

    Args:
        content: The plain text content to generate FAQs from.

    Returns:
        A list of dictionaries, each containing a question and its answer.
    """

    # Load the text content into a document format
    document = Document(page_content=content)

    # Create a vector store retriever for the document
    embeddings = OpenAIEmbeddings(openai_api_key="api-key-here")  # Replace with your preferred embeddings
    vector_store = FAISS.from_documents([document], embeddings)
    retriever = vector_store.as_retriever()

    # Initialize the Google Gemini LLM
    llm = VertexAI(
        model="gemini-bison-001",  # Use the specific Gemini model version
        temperature=0.7,  # Adjust for creativity
        max_output_tokens=512,  # Set based on requirements
        top_p=0.8,  # Nucleus sampling for response control
        top_k=40  # Alternative sampling control
    )

    # Create a retrieval QA chain
    qa_chain = RetrievalQA.from_llm(llm=llm, retriever=retriever)

    # Generate FAQs
    qa_pairs = []
    for query in ["What is the main topic?", "What are the key points?", "What are some potential questions and answers?"]:
        result = qa_chain.run(query)
        qa_pairs.append({"question": query, "answer": result})

    return qa_pairs
