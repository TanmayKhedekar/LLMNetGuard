from sklearn.metrics import classification_report
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the fine-tuned model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("./fine_tuned_model")
tokenizer = AutoTokenizer.from_pretrained("./fine_tuned_model")

# Unseen test data (replace with actual unseen data)
unseen_texts = [
    "Ether / IP / TCP 192.168.218.160:50536 > 54.254.188.33:http PA / Raw",
    "Ether / IP / UDP 192.168.218.160:50536 > 54.254.188.33:http PA / Raw",
]
true_labels = [1, 0]  # Replace with the actual labels for unseen data

# Tokenize test data
inputs = tokenizer(unseen_texts, truncation=True, padding=True, max_length=128, return_tensors="pt")

# Make predictions
outputs = model(**inputs)
predicted_labels = torch.argmax(outputs.logits, dim=-1).tolist()

# Generate evaluation report
print("Classification Report:")
print(classification_report(true_labels, predicted_labels))
