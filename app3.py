import streamlit as st


import numpy as np


import document_uploader
import model_loader
import embedding
import answer

embedding_model, qa_pipeline = model_loader.load_models()



# Function to create embeddings and store in FAISS


# Function to retrieve relevant documents
def retrieve_relevant_documents(index, documents, question, top_k=3):
    question_embedding = embedding_model.encode([question])
    distances, indices = index.search(np.array(question_embedding), top_k)
    relevant_docs = [documents[i] for i in indices[0]]
    return relevant_docs

# Function to generate a response


# Streamlit app
def main():
    st.title("AI-Powered Q&A System")
    st.write("Upload your documents (PDF or .txt) and ask questions!")

    # Step 1: Upload documents
    uploaded_files = st.file_uploader("Upload your documents", type=["pdf", "txt"], accept_multiple_files=True)
    
    if uploaded_files:
        st.write("Documents uploaded successfully!")
        documents = document_uploader. load_documents(uploaded_files)
        
        # Step 2: Create embeddings and FAISS index
        index, documents = embedding.create_faiss_index(documents,embedding_model)
        
        # Step 3: Ask a question
        question = st.text_input("Ask a question about the documents:")
        
        if question:
            # Step 4: Retrieve relevant documents
            relevant_docs = retrieve_relevant_documents(index, documents, question)
            
            # Step 5: Generate and display the answer
            answer_ = answer.generate_response(question, relevant_docs,qa_pipeline)
            
            # Display the answer
            st.write(f"**Answer:** {answer_}")
            
            # Display relevant documents (optional)
            st.write("**Relevant Documents:**")
            for doc in relevant_docs:
                st.write(f"**Source:** {doc['source']}")
                st.write(f"**Text:** {doc['text'][:500]}...")  # Show first 500 characters
                break
    else:
        st.write("Please upload documents to get started.")

if __name__ == "__main__":
    main()