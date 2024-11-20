import sqlite3
import time

class Memory:
    def __init__(self):
        self.short_term = {}
        self.long_term_db = "long_term_memory.db"
        self.create_long_term_db()

    def create_long_term_db(self):
        # Set up the SQLite database for long-term memory
        conn = sqlite3.connect(self.long_term_db)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS memory (
                        id INTEGER PRIMARY KEY,
                        query TEXT,
                        response TEXT,
                        timestamp INTEGER)''')
        conn.commit()
        conn.close()

    def store_in_memory(self, user_input, response, memory_type="short-term"):
        if memory_type == "short-term":
            # Store in short-term memory with an expiry time (example: 1 hour)
            self.short_term[user_input] = {'response': response, 'timestamp': time.time()}
        elif memory_type == "long-term":
            # Store in long-term memory (in SQLite)
            conn = sqlite3.connect(self.long_term_db)
            c = conn.cursor()
            c.execute("INSERT INTO memory (query, response, timestamp) VALUES (?, ?, ?)", 
                      (user_input, response, int(time.time())))
            conn.commit()
            conn.close()

    def retrieve_from_memory(self, query, memory_type="short-term"):
        if memory_type == "short-term":
            # Retrieve from short-term memory (check if it exists and not expired)
            if query in self.short_term:
                memory_data = self.short_term[query]
                if time.time() - memory_data['timestamp'] < 3600:  # Expiry of 1 hour
                    return memory_data['response']
                else:
                    del self.short_term[query]  # Remove expired memory
        elif memory_type == "long-term":
            # Retrieve from long-term memory (SQLite)
            conn = sqlite3.connect(self.long_term_db)
            c = conn.cursor()
            c.execute("SELECT response FROM memory WHERE query = ? ORDER BY timestamp DESC LIMIT 1", (query,))
            result = c.fetchone()
            conn.close()
            if result:
                return result[0]
        return None
