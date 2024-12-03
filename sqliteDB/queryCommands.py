import sqlite3

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

# Command Functions

def help(arguments=None):
    print("Available commands:")
    print("FORMAT: command_name {command_argument}")
    print("FORMAT: Arguments are required unless stated otherwise.")
    print(" - get {table}: Select all from table")
    print(" - get_members_borrow_log {member_id}: Get a member's borrow log")
    print(" - get_overdue_borrow_logs: Get all overdue borrow logs")
    print(" - help: Show this help message")
    return None  # No result to return

# Query to fetch all members
def get(arguments=None):
    if arguments is None:
        print("Usage: get {table}")
        return None

    args = arguments.split(" ", 1)
    table = args[0] if len(args) > 0 else None

    try:
        # Query to fetch all from selected table
        cursor.execute(f"""SELECT * FROM {table}""")
        return cursor
    except sqlite3.Error as e:
        # Handle any database errors, including table not existing
        print(f"Error executing query: {e}")
        return None
    
# Query to fetch members borrow logs
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

# Query to fetch overdue borrow logs
def get_overdue_borrow_logs(arguments=None):
    cursor.execute("""
        SELECT 
            BorrowLog.*,
            CASE 
                WHEN BorrowLog.CheckinDate IS NULL AND DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') < DATE('now') THEN 'Overdue'
                WHEN BorrowLog.CheckinDate IS NOT NULL AND BorrowLog.CheckinDate > DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') THEN 'Overdue'
                ELSE 'Not Overdue'
            END AS OverdueStatus
        FROM 
            BorrowLog
        WHERE
            (BorrowLog.CheckinDate IS NULL AND DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') < DATE('now'))
            OR (BorrowLog.CheckinDate IS NOT NULL AND BorrowLog.CheckinDate > DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days'))
        """)
    return cursor

# Command map
command_map = {
    'help': help,
    'get': get,
    'get_members_borrow_log': get_members_borrow_log,
    'get_overdue_borrow_logs': get_overdue_borrow_logs
}
