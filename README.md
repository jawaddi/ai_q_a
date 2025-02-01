models:
 -MiniLM (all-MiniLM-L6-v2):Transformer-based LLM,Used for generating sentence embeddings
 -DistilBERT (distilbert-base-cased-distilled-squad):Transformer-based LLM ,used for question answering

FAISS:
A vector database used for storing and searching document embeddings. It enables fast similarity search by using efficient nearest neighbor algorithms.


1-load the models localy
model_loader.py take care of loading the models
  embedding_model:for embedding model for semantic tasks 
  qa_pipeline:model for answering questions

2- retrieve_relevant_documents in app3.py

   a - Question to Embedding: The question is converted into an embedding (vector) using the pre-trained(all-MiniLM-L6-v2) embedding model.
   b- Search Index: The question’s embedding is compared to the document embeddings stored in the index using a nearest neighbor search algorithm
   c - Retrieve Document: The document corresponding to the closest embeddings are retrieved

3- in the main function guide for the user to upload the docs(pdf,txt) where the document_loader.py used to let the user upload the docs

4- after we upload the documents we will use the embedding .
  we will pass the documtens and embedding_model (embedding.create_faiss_index(doc,model))
   --  Generate Embeddings for Documents
   --  Create a FAISS Index

5 we get the user question 
   - we get the document the most relevant to the question

6- we generate an answer by passing the question, document and qa_model to the answer model



===========================================================
I initially tried using the OpenAI API, but found it to be expensive due to usage costs.
I also attempted to use TinyLlama/TinyLlama-1.1B-Chat-v1.0, but it requires significant computational resources, which was challenging to handle.






