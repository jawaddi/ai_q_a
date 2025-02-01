import faiss
import numpy as np

# import streamlit as st

#@st.cache_resource
def create_faiss_index(documents,embedding_model):
    try:
        document_texts = [doc["text"] for doc in documents]
        document_embeddings = embedding_model.encode(document_texts)
        
        dimension = document_embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(document_embeddings))
        
        return index, documents
    except Exception as e:
        #st.error(f"Error creating FAISS index: {e}")
        return None, documents