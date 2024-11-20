def classify_query(query):
    # Simple placeholder for query classification (can be extended with actual NN or ML model)
    if "buy" in query or "shopping" in query:
        return "short-term"
    elif "doctor" in query or "schedule" in query:
        return "long-term"
    else:
        return "internet"
