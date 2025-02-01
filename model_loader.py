
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from transformers import pipeline

load_dotenv()
model_name = os.getenv("MODEL_NAME")

def load_models():
    try:
        embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        qa_pipeline = pipeline("question-answering", model=model_name)
        return embedding_model, qa_pipeline
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None