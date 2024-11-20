from datasets import load_dataset

# Load the SQuAD dataset (v2.0 includes unanswerable questions)
dataset = load_dataset('squad_v2')
print(dataset)

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def preprocess_data(examples):
    # Tokenize questions and context
    return tokenizer(
        examples['question'], examples['context'], 
        truncation=True, padding='max_length', max_length=512
    )

# Apply the preprocessing to the dataset
train_dataset = dataset['train'].map(preprocess_data, batched=True)
val_dataset = dataset['validation'].map(preprocess_data, batched=True)

from transformers import BertForQuestionAnswering

# Load pre-trained BERT model for question answering
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

from transformers import Trainer, TrainingArguments

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',          # Output directory
    evaluation_strategy="epoch",     # Evaluate at the end of each epoch
    learning_rate=2e-5,              # Learning rate
    per_device_train_batch_size=8,   # Batch size for training
    per_device_eval_batch_size=8,    # Batch size for evaluation
    num_train_epochs=3,              # Number of training epochs
    weight_decay=0.01,               # Weight decay
)

# Define the Trainer
trainer = Trainer(
    model=model,                         # The model to train
    args=training_args,                   # Training arguments
    train_dataset=train_dataset,         # The training dataset
    eval_dataset=val_dataset,            # The evaluation dataset
    tokenizer=tokenizer,                 # The tokenizer
)

# Start training
trainer.train()

results = trainer.evaluate()
print(results)

model.save_pretrained('./trained_model')
tokenizer.save_pretrained('./trained_model')
