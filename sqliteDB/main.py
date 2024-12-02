import sys
import sqlite3
from queryCommands import * # Import commands

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

def main():
    arguments = sys.argv[1:]
    
    # Import and call create/populate if specified in arguments
    if "create" in arguments:
        import createDatabase

    if "pop" in arguments:
        import populateDatabase

    # Command loop
    while True:
        user_input = input("Enter SQL query or custom command ('help' for commands, or 'quit' to exit): ").strip()

        # Exit the program if 'quit' is entered
        if user_input.lower() == "quit":
            print("Exiting the program.")
            break

        # Parse command and arguments
        try:
            command, arguments = user_input.split(" ", 1)
        except ValueError:
            command, arguments = user_input, None  # No arguments provided
        
        # Handle custom commands
        if command in command_map:
            command_function = command_map[command]
            result = command_function(arguments)

            if result:
                rows = result.fetchall()
                for row in rows:
                    print(row)
        else:
            try:
                # Execute user-entered SQL query
                cursor.execute(user_input)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except sqlite3.Error as e:
                # Handle invalid SQL query
                print(f"Error executing query: {e}")

    # Close the database connection before exiting
    connection.close()

# Run the program
if __name__ == "__main__":
    main()
