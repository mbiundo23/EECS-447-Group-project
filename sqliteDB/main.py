import sqlite3

import createDatabase
import populateDatabase
import queries

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

# Function to execute SQL commands and handle user input
def main():
    while True:
        # Get user input (SQL query)
        user_input = input("Enter SQL query (or 'quit' to exit): ").strip()

        # If the user wants to quit
        if user_input.lower() == "quit":
            print("Exiting the program.")
            break
        
        try:
            # Execute the query entered by the user
            cursor.execute(user_input)
            
            # Fetch and display the results
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            
        except sqlite3.Error as e:
            # Print error if SQL query is invalid
            print(f"Error executing query: {e}")

# Run the program
if __name__ == "__main__":
    main()
