import sqlite3

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

# Command Functions

def help(arguments=None):
    print("Available commands:")
    print("FORMAT: command_name {command_argument}")
    print("FORMAT: Curly brackets are to show that it's a required argument.")
    print(" - get_members: Get all members")
    print(" - get_members_borrow_log {member_id}: Get a member's borrow log")
    print(" - help: Show this help message")
    return None  # No result to return

def get_members(arguments=None):
    cursor.execute("SELECT * FROM Member")
    return cursor

def get_members_borrow_log(arguments=None):
    # Ensure arguments are provided
    if arguments is None:
        print("Usage: get_members_borrow_log {member_id}")
        return None

    args = arguments.split(" ", 1)
    member_id = args[0] if len(args) > 0 else None

    if member_id is None: 
        print("Invalid input format. Usage: get_members_borrow_log {member_id}")
        return None

    # Query to fetch borrow log for a given member ID
    cursor.execute(f"""
        SELECT BorrowLog.*, Member.MemberName 
        FROM BorrowLog
        INNER JOIN Member ON Member.MemberID = BorrowLog.MemberID
        WHERE Member.MemberID = {member_id}
    """)
    
    return cursor

# Command map
command_map = {
    'help': help,
    'get_members': get_members,
    'get_members_borrow_log': get_members_borrow_log
}
