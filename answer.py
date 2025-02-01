def generate_response(question, relevant_docs,qa_pipeline):
    context = " ".join([doc["text"] for doc in relevant_docs])
    result = qa_pipeline(question=question, context=context)
    return result["answer"]