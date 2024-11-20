from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embedding(query):
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    # We take the mean of the last hidden layer's output as the embedding
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

# Example Usage
query = "How do I make a cup of coffee?"
embedding = get_bert_embedding(query)
print(embedding)