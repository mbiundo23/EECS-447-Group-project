import sys  # Importing the sys module to handle command-line arguments
import sqlite3  # Importing sqlite3 to interact with the SQLite database
from queryCommands import *  # Importing all custom commands from the `queryCommands` module

# Connect to the database
connection = sqlite3.connect('library_database.db')  # Establishing a connection to the SQLite database file
cursor = connection.cursor()  # Creating a cursor object to execute SQL commands

# Main function to handle user interactions
def main():
    arguments = sys.argv[1:]  # Reading command-line arguments (excluding the script name)
    
    # Import and call `createDatabase` if "create" is passed in command-line arguments
    if "create" in arguments:
        import createDatabase  # Dynamically importing the `createDatabase` script

    # Import and call `populateDatabase` if "pop" is passed in command-line arguments
    if "pop" in arguments:
        import populateDatabase  # Dynamically importing the `populateDatabase` script

    # Enter a command loop to handle user input until the user chooses to quit
    while True:
        # Prompt user for input
        user_input = input("Enter SQL query or custom command ('help' for commands, or 'quit' to exit): ").strip()

        # Exit the program if the user types "quit"
        if user_input.lower() == "quit":
            print("Exiting the program.")  # Inform the user
            break  # Exit the loop

        # Parse the input into a command and its arguments
        try:
            command, arguments = user_input.split(" ", 1)  # Split input into command and arguments
        except ValueError:
            command, arguments = user_input, None  # If no arguments provided, set `arguments` to None
        
        # Handle custom commands
        if command in command_map:  # Check if the command exists in the `command_map`
            command_function = command_map[command]  # Retrieve the corresponding function
            result = command_function(arguments)  # Execute the command with arguments
            
            if result:  # If the command returns a result (e.g., a database cursor)
                rows = result.fetchall()  # Fetch all rows from the result set
                for row in rows:
                    print(row)  # Print each row
        else:
            try:
                # If the command is not custom, execute it as a raw SQL query
                cursor.execute(user_input)  # Execute the SQL query
                rows = cursor.fetchall()  # Fetch all rows from the result set
                for row in rows:
                    print(row)  # Print each row
            except sqlite3.Error as e:
                # Handle errors related to SQL queries or database interactions
                print(f"Error executing query: {e}")

    # Ensure the database connection is closed before exiting the program
    connection.commit()  # Commit any pending transactions
    connection.close()  # Close the database connection

# Run the program if the script is executed directly
if __name__ == "__main__":
    main()  # Call the main function
