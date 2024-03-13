from flask import Flask, request, jsonify, render_template
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"

app = Flask(__name__, template_folder='E:/Learnings/FormFiller/flask_app/templates', static_folder='E:/Learnings/FormFiller/flask_app/templates/static')

# Set the UPLOAD_FOLDER variable
app.config['UPLOAD_FOLDER'] = 'E:/Learnings/FormFiller/flask_app/uploads'

@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/answer', methods=['POST'])
def answer_query():
    # Get the query and PDF file from the request
    query = request.form['query']
    # query += "Answer the query with respect to the retriever that is being passed."
    pdf_file = request.files['pdf']

    # Save the PDF file to a temporary location
    pdf_file_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
    pdf_file.save(pdf_file_path)

    # Extract text from the PDF file
    pdf_loader = PyPDFLoader(pdf_file_path)
    pages = pdf_loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=1000)
    context = "\n\n".join(str(p.page_content) for p in pages)
    texts = text_splitter.split_text(context)
    print(texts)

    # Initialize the Gemini AI model
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=os.environ["GOOGLE_API_KEY"],convert_system_message_to_human=True)

    # Initialize the embeddings and vector index
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=os.environ["GOOGLE_API_KEY"])
    vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":5})

    # Initialize the QA chain
    qa_chain = RetrievalQA.from_chain_type(
        model,
        retriever=vector_index,
        return_source_documents=True
    )

    # Get the answer to the query
    result = qa_chain.invoke({"query": query})
    answer = result["result"]


    # Delete the uploaded file after processing
    try:
        os.remove(pdf_file_path)
    except Exception as e:
        print(f"Error deleting uploaded file: {e}")


    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
