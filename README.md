# PDF Query Chrome Extension

A Chrome extension to answer queries based on information provided in uploaded PDF files.

## Introduction

This project introduces a Chrome extension that facilitates query-based interactions with PDF files. Users can upload PDF documents, and the extension will analyze the content to provide relevant answers to queries.

## Features

- **PDF Parsing:** Automatically extracts text and relevant information from uploaded PDF files using `PyPDFLoader`.
- **Query Handling:** Processes user queries and provides accurate responses based on the content of the PDF documents.
- **Language Processing:** Utilizes Google Generative AI embeddings and chat functionalities through `langchain_google_genai` for document analysis and question answering.
- **Seamless Integration:** Integrated directly into the Chrome browser for convenient usage.

## Input Data

- **Uploaded PDF Files:** Users can upload PDF files containing information to query.
- **Query Handling:** Queries from users are processed to generate accurate responses based on the content of the PDF documents.


## Functionality

1. **PDF Parsing:** The extension parses the uploaded PDF files to extract relevant information using `PyPDFLoader`.
2. **Query Handling:** Queries from users are processed to generate accurate responses based on the content of the PDF documents.
3. **Gemini AI Model:** Utilizes Google Generative AI model `Gemini-pro` for generating responses to user queries.
4. **Embeddings and Vector Index:** Utilizes `GoogleGenerativeAIEmbeddings` and `Chroma` from `long-chain` for creating embeddings and vector index.
5. **QA Chain:** Utilizes `RetrievalQA` from `langchain` to perform question answering based on the embeddings and vector index.

## Future Enhancements

- **Improved Query Understanding:** Enhance natural language processing capabilities for a better understanding of user queries.
- **Enhanced User Interface:** Improve the user interface for a more intuitive and user-friendly experience.
- **Support for More File Formats:** Extend support for parsing and analyzing various file formats beyond PDF.
- **Form Filling Capability:** Develop a form-filling capability to automatically fill forms based on extracted information from PDF files.

## Dependencies

- **Flask:** Micro web framework for Python.
- **langchain_community:** Library for loading documents.
- **langchain:** Library for text splitting and chains.
- **langchain_google_genai:** Library for Google Generative AI embeddings and chat functionalities.
- **google.generativeai:** Google's Generative AI library.

## Contributor
- Pramit De (email: pramitde726@gmail.com/pramit.de.cse.2021@tint.edu.in) (Department of CSE, Techno International New Town, West Bengal, India)   
   
