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
def add_member(arguments=None):
    if arguments is None:
        print("Usage: add_member {MemberName} {MembershipType} {StartingDate} {BirthDate}")
        return None

    args = arguments.split(" ", 3)
    if len(args) < 4:
        print("Invalid input. Usage: add_member {MemberName} {MembershipType} {StartingDate} {BirthDate}")
        return None

    member_name, membership_type, starting_date, birth_date = args

    try:
        cursor.execute("""
            INSERT INTO Member (MemberName, MembershipType, StartingDate, BirthDate)
            VALUES (?, ?, ?, ?)
        """, (member_name, membership_type, starting_date, birth_date))
        connection.commit()
        print(f"New member {member_name} added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding member: {e}")
    return None

def reserve_room(arguments=None):
    if arguments is None:
        print("Usage: reserve_room {ReserveDate} {RoomNumber} {MemberID}")
        return None

    args = arguments.split(" ", 2)
    if len(args) < 3:
        print("Invalid input. Usage: reserve_room {ReserveDate} {RoomNumber} {MemberID}")
        return None

    reserve_date, room_number, member_id = args

    try:
        cursor.execute("""
            INSERT INTO ReserveRoom (ReserveDate, RoomNumber, MemberID)
            VALUES (?, ?, ?)
        """, (reserve_date, room_number, member_id))
        connection.commit()
        print(f"Room {room_number} reserved for member {member_id} on {reserve_date}.")
    except sqlite3.Error as e:
        print(f"Error reserving room: {e}")
    return None

def borrow_resource(arguments=None):
    if arguments is None:
        print("Usage: borrow_resource {MemberID} {ResourceID} {CheckoutDate} {MaxDuration}")
        return None

    args = arguments.split(" ", 3)
    if len(args) < 4:
        print("Invalid input. Usage: borrow_resource {MemberID} {ResourceID} {CheckoutDate} {MaxDuration}")
        return None

    member_id, resource_id, checkout_date, max_duration = args

    try:
        cursor.execute("""
            INSERT INTO BorrowLog (MemberID, ResourceID, CheckoutDate, MaxDuration)
            VALUES (?, ?, ?, ?)
        """, (member_id, resource_id, checkout_date, max_duration))
        connection.commit()
        print(f"Resource {resource_id} borrowed by member {member_id} on {checkout_date}.")
    except sqlite3.Error as e:
        print(f"Error borrowing resource: {e}")
    return None

def return_resource(arguments=None):
    if arguments is None:
        print("Usage: return_resource {BorrowID} {CheckinDate}")
        return None

    args = arguments.split(" ", 1)
    if len(args) < 2:
        print("Invalid input. Usage: return_resource {BorrowID} {CheckinDate}")
        return None

    borrow_id, checkin_date = args

    try:
        cursor.execute("""
            UPDATE BorrowLog
            SET CheckinDate = ?
            WHERE BorrowID = ?
        """, (checkin_date, borrow_id))
        connection.commit()
        print(f"Resource returned successfully with borrow ID {borrow_id} on {checkin_date}.")
    except sqlite3.Error as e:
        print(f"Error returning resource: {e}")
    return None

def get_available_resources(arguments=None):
    cursor.execute("""
        SELECT Resource.ResourceID, Resource.AvailabilityStatus, 
               PhysicalBook.Title, Audiobook.Title, Magazine.Title, 
               eBook.Title, DigitalDisk.Title
        FROM Resource
        LEFT JOIN PhysicalBook ON Resource.ResourceID = PhysicalBook.ResourceID
        LEFT JOIN Audiobook ON Resource.ResourceID = Audiobook.ResourceID
        LEFT JOIN Magazine ON Resource.ResourceID = Magazine.ResourceID
        LEFT JOIN eBook ON Resource.ResourceID = eBook.ResourceID
        LEFT JOIN DigitalDisk ON Resource.ResourceID = DigitalDisk.ResourceID
        WHERE Resource.AvailabilityStatus = 1
    """)
    available_resources = cursor.fetchall()
    if available_resources:
        for resource in available_resources:
            print(f"Resource ID: {resource[0]}, Availability: {resource[1]}, Title: {resource[2] or resource[3] or resource[4] or resource[5] or resource[6]}")
    else:
        print("No available resources found.")
    return None

def get_overdue_members(arguments=None):
    cursor.execute("""
        SELECT DISTINCT Member.MemberID, Member.MemberName
        FROM BorrowLog
        INNER JOIN Member ON BorrowLog.MemberID = Member.MemberID
        WHERE (BorrowLog.CheckinDate IS NULL AND DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') < DATE('now'))
        OR (BorrowLog.CheckinDate IS NOT NULL AND BorrowLog.CheckinDate > DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days'))
    """)
    overdue_members = cursor.fetchall()
    if overdue_members:
        for member in overdue_members:
            print(f"Member ID: {member[0]}, Member Name: {member[1]}")
    else:
        print("No overdue members found.")
    return None

def get_author_books(arguments=None):
    if arguments is None:
        print("Usage: get_author_books {AuthorID}")
        return None

    author_id = arguments.strip()

    try:
        cursor.execute("""
            SELECT PhysicalBook.Title, Audiobook.Title, eBook.Title
            FROM ResourceAuthor
            LEFT JOIN PhysicalBook ON ResourceAuthor.ResourceID = PhysicalBook.ResourceID
            LEFT JOIN Audiobook ON ResourceAuthor.ResourceID = Audiobook.ResourceID
            LEFT JOIN eBook ON ResourceAuthor.ResourceID = eBook.ResourceID
            WHERE ResourceAuthor.AuthorID = ?
        """, (author_id,))
        author_books = cursor.fetchall()
        if author_books:
            for book in author_books:
                print(f"Book Title: {book[0] or book[1] or book[2]}")
        else:
            print(f"No books found for Author ID {author_id}.")
    except sqlite3.Error as e:
        print(f"Error fetching author books: {e}")
    return None

