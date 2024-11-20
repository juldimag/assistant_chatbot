import sys
import random
from memory import Memory
from search import internet_search
from neural_network import classify_query

def assistant_loop():
    print("AI Assistant is ready! Type 'exit' to end the session.")
    
    memory = Memory()  # Create an instance of the Memory class
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Classify the query
        query_type = classify_query(user_input)
        
        # Check short-term memory first
        response = memory.retrieve_from_memory(user_input, memory_type="short-term")
        
        if not response:
            # If not found in short-term, check long-term memory
            response = memory.retrieve_from_memory(user_input, memory_type="long-term")
        
        if not response:
            # If no match in memory, perform an internet search
            print("I couldn't find that in my memory, searching the web...")
            response = internet_search(user_input)
        
        print(f"AI: {response}")

if __name__ == "__main__":
    assistant_loop()

