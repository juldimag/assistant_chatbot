# Personal AI Assistant

The **Personal AI Assistant** is a chatbot-style application designed to help individuals organize their lives. It manages personal notes, stores important information, and retrieves general knowledge, all within a simple, text-based interface. The assistant operates on three layers of memory to provide personalized and context-aware support.

## Project Overview

The project aims to create a versatile, self-contained personal assistant with the following core functionalities:

1. **Personal Memory**: Store temporary or short-term information (e.g., "What I need to buy next time I'm shopping").
2. **Long-Term Memory**: Retain recurring or important details (e.g., schedules, phone numbers, key dates).
3. **General Knowledge**: Access non-personal information like recipes, quick facts, or study resources.

This project focuses on modular design and simplicity, allowing for easy expansion and customization. The assistant is built using Python and primarily relies on user inputs to learn and adapt.

---

## Rough To-Do List

### **Phase 1: Foundations**
- [X] **Set up the project environment**:.
  - Create a project folder and initialize necessary files.
- [ ] **Create memory storage**:
  - Design JSON files (`shortterm_memory.json`, `longterm_memory.json`) for storing data.
  - Write functions to save and load information from these files.

---

### **Phase 2: Core Functionalities**
- [ ] **Implement memory layers**:
  - Create functions to store personal (short-term) and long-term data.
  - Write a retrieval system for recalling information based on keywords or queries.
- [ ] **Develop user interaction**:
  - Build a basic text-based chat interface for testing.
  - Enable commands like `remember`, `important`, and `recall`.
  
---

### **Phase 3: Advanced Features**
- [ ] **Enhance retrieval capabilities**:
  - Add keyword or tag-based search.
  - Allow listing all stored items by category (short-term, long-term).
- [ ] **Automate data organization**:
  - Implement rules to promote short-term memory items to long-term if they recur.
  - Add a priority system for task or information management.

---

### **Phase 4: Optional Enhancements**
- [ ] **Web Integration**:
  - Add the ability to retrieve general knowledge from the internet (e.g., via APIs like OpenAI or Google).
- [ ] **Natural Language Processing (NLP)**:
  - Improve input interpretation for more natural interactions.
- [ ] **Customizable Assistant Personality**:
  - Add user-defined settings for tone, style, and behavior.

---

### **Phase 5: Testing and Finalization**
- [ ] **Test core features**:
  - Ensure all storage and retrieval functions work as intended.
  - Test user interaction for smooth functionality.
- [ ] **Prepare documentation**:
  - Finalize the README and include usage instructions.
  - Document code for clarity and future development.

