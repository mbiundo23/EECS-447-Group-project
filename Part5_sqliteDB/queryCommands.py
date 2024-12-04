import sqlite3  # Importing the SQLite3 module for interacting with the database

# Connect to the database
connection = sqlite3.connect('library_database.db')  # Establish connection to the SQLite database
cursor = connection.cursor()  # Create a cursor object to execute SQL commands

# Command Functions

# Function to display available commands and their usage
def help(arguments=None):
    print("Available commands:")  # Header for available commands
    print("FORMAT: command_name {command_argument}")  # General format of commands
    print("FORMAT: Arguments are required unless stated otherwise.")  # Note about arguments
    # List of commands and their descriptions
    print(" - get {table}: Select all from table")  
    print(" - get_members_borrow_log {member_id}: Get a member's borrow log")
    print(" - get_overdue_borrow_logs: Get all overdue borrow logs")
    print(" - get_overdue_members: Get all members with an overdue borrow log")
    print(" - get_author_books: {authorID} Get all books by a specified author")
    print(" - add_member: {MemberName} {MembershipType} {StartingDate} {BirthDate} Add a member")
    print(" - reserve_room: {ReserveDate} {RoomNumber} {MemberID} Reserve a room")
    print(" - borrow_resource: {MemberID} {ResourceID} {CheckoutDate} {MaxDuration} Borrow a resource")
    print(" - return_resource: {BorrowID} {CheckinDate} Return a resource")
    print(" - get_available_resources: Get all available resources")
    print(" - help: Show this help message")
    return None  # No result is returned, just prints help information

# Function to fetch all records from a specified table
def get(arguments=None):
    # Check if arguments are provided
    if arguments is None:
        print("Usage: get {table}")  # Display usage if no arguments are passed
        return None

    # Split the arguments to get the table name
    args = arguments.split(" ", 1)  # Split arguments by space, taking the first word as the table name
    table = args[0] if len(args) > 0 else None  # Assign the first argument as the table name

    try:
        # Execute a query to select all records from the specified table
        cursor.execute(f"""SELECT * FROM {table}""")
        return cursor  # Return the cursor to the result set
    except sqlite3.Error as e:
        # Handle errors such as invalid table name
        print(f"Error executing query: {e}")  # Print the error message
        return None  # Return None if an error occurs

# Function to fetch the borrow log for a specific member
def get_members_borrow_log(arguments=None):
    # Check if arguments are provided
    if arguments is None:
        print("Usage: get_members_borrow_log {member_id}")  # Display usage if no arguments are passed
        return None

    # Split the arguments to extract the member ID
    args = arguments.split(" ", 1)  # Split arguments by space, taking the first word as the member ID
    member_id = args[0] if len(args) > 0 else None  # Assign the first argument as the member ID

    # Check if member ID is provided
    if member_id is None: 
        print("Invalid input format. Usage: get_members_borrow_log {member_id}")  # Display usage if no member ID
        return None

    # Execute a query to fetch borrow logs for the given member ID
    cursor.execute(f"""
        SELECT BorrowLog.*, Member.MemberName  -- Select all columns from BorrowLog and MemberName
        FROM BorrowLog
        INNER JOIN Member ON Member.MemberID = BorrowLog.MemberID  -- Join BorrowLog and Member tables on MemberID
        WHERE Member.MemberID = {member_id}  -- Filter records where MemberID matches the provided argument
    """)
    
    return cursor  # Return the cursor to the result set


# Query to fetch overdue borrow logs
def get_overdue_borrow_logs(arguments=None):
    # Execute a query to identify overdue borrow logs
    cursor.execute("""
        SELECT 
            BorrowLog.*,  -- Select all columns from BorrowLog
            CASE 
                WHEN BorrowLog.CheckinDate IS NULL AND DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') < DATE('now') THEN 'Overdue'
                -- Mark as 'Overdue' if the book is not checked in and the due date has passed
                WHEN BorrowLog.CheckinDate IS NOT NULL AND BorrowLog.CheckinDate > DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') THEN 'Overdue'
                -- Mark as 'Overdue' if the book is returned but the check-in date exceeds the due date
                ELSE 'Not Overdue'  -- Otherwise, mark as 'Not Overdue'
            END AS OverdueStatus  -- Alias for the status of the borrow log
        FROM 
            BorrowLog
        WHERE
            (BorrowLog.CheckinDate IS NULL AND DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') < DATE('now'))
            -- Include logs where the book is not returned and the due date has passed
            OR (BorrowLog.CheckinDate IS NOT NULL AND BorrowLog.CheckinDate > DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days'))
            -- Include logs where the book is returned but past the due date
        """)
    return cursor  # Return the cursor to the result set

# Command map to link command strings to their corresponding functions

# Function to add a new member to the Member table
def add_member(arguments=None):
    # Check if arguments are provided
    if arguments is None:
        print("Usage: add_member {MemberName} {MembershipType} {StartingDate} {BirthDate}")
        return None

    # Split the arguments to extract member details
    args = arguments.split(" ", 3)  # Split arguments into 4 parts: name, type, start date, birth date
    if len(args) < 4:
        print("Invalid input. Usage: add_member {MemberName} {MembershipType} {StartingDate} {BirthDate}")
        return None

    member_name, membership_type, starting_date, birth_date = args  # Assign extracted values to variables

    try:
        # Insert the new member into the Member table
        cursor.execute("""
            INSERT INTO Member (MemberName, MembershipType, StartingDate, BirthDate)
            VALUES (?, ?, ?, ?)
        """, (member_name, membership_type, starting_date, birth_date))
        connection.commit()  # Commit the transaction
        print(f"New member {member_name} added successfully.")  # Confirm successful addition
    except sqlite3.Error as e:
        # Handle errors such as invalid inputs or database issues
        print(f"Error adding member: {e}")  # Print the error message
    return None  # No return value

# Function to reserve a room for a member
def reserve_room(arguments=None):
    # Check if arguments are provided
    if arguments is None:
        print("Usage: reserve_room {ReserveDate} {RoomNumber} {MemberID}")
        return None

    # Split the arguments to extract reservation details
    args = arguments.split(" ", 2)  # Split arguments into 3 parts: reserve date, room number, member ID
    if len(args) < 3:
        print("Invalid input. Usage: reserve_room {ReserveDate} {RoomNumber} {MemberID}")
        return None

    reserve_date, room_number, member_id = args  # Assign extracted values to variables

    try:
        # Insert the room reservation into the ReserveRoom table
        cursor.execute("""
            INSERT INTO ReserveRoom (ReserveDate, RoomNumber, MemberID)
            VALUES (?, ?, ?)
        """, (reserve_date, room_number, member_id))
        connection.commit()  # Commit the transaction
        print(f"Room {room_number} reserved for member {member_id} on {reserve_date}.")  # Confirm successful reservation
    except sqlite3.Error as e:
        # Handle errors such as invalid inputs or database issues
        print(f"Error reserving room: {e}")  # Print the error message
    return None  # No return value


# Function to borrow a resource
def borrow_resource(arguments=None):
    # Check if arguments are provided
    if arguments is None:
        print("Usage: borrow_resource {MemberID} {ResourceID} {CheckoutDate} {MaxDuration}")
        return None

    # Split the arguments into components
    args = arguments.split(" ", 3)  # Split into 4 parts: MemberID, ResourceID, CheckoutDate, MaxDuration
    if len(args) < 4:
        print("Invalid input. Usage: borrow_resource {MemberID} {ResourceID} {CheckoutDate} {MaxDuration}")
        return None

    member_id, resource_id, checkout_date, max_duration = args  # Assign extracted values to variables

    try:
        # Insert the borrow record into the BorrowLog table
        cursor.execute("""
            INSERT INTO BorrowLog (MemberID, ResourceID, CheckoutDate, MaxDuration)
            VALUES (?, ?, ?, ?)
        """, (member_id, resource_id, checkout_date, max_duration))

        # Update the resource's availability status
        cursor.execute("""
            UPDATE Resource
            SET AvailabilityStatus = False
            WHERE ResourceID = ?
        """, (resource_id,))

        connection.commit()  # Commit the transaction
        print(f"Resource {resource_id} borrowed by member {member_id} on {checkout_date}.")  # Confirm success
    except sqlite3.Error as e:
        # Handle any database errors, such as constraint violations or invalid inputs
        print(f"Error borrowing resource: {e}")  # Print error message
    return None  # No return value

# Function to return a borrowed resource
def return_resource(arguments=None):
    # Check if arguments are provided
    if arguments is None:
        print("Usage: return_resource {BorrowID} {CheckinDate}")
        return None

    # Split the arguments into components
    args = arguments.split(" ", 1)  # Split into 2 parts: BorrowID and CheckinDate
    if len(args) < 2:
        print("Invalid input. Usage: return_resource {BorrowID} {CheckinDate}")
        return None

    borrow_id, checkin_date = args  # Assign extracted values to variables

    try:
        # Fetch the ResourceID associated with the BorrowID
        cursor.execute("""
            SELECT ResourceID FROM BorrowLog WHERE BorrowID = ?
        """, (borrow_id,))
        result = cursor.fetchone()
        if not result:
            print(f"No borrow record found with ID {borrow_id}.")
            return None

        resource_id = result[0]

        # Update the borrow record with the check-in date
        cursor.execute("""
            UPDATE BorrowLog
            SET CheckinDate = ?
            WHERE BorrowID = ?
        """, (checkin_date, borrow_id))

        # Update the resource's availability status
        cursor.execute("""
            UPDATE Resource
            SET AvailabilityStatus = True
            WHERE ResourceID = ?
        """, (resource_id,))

        connection.commit()  # Commit the transaction
        print(f"Resource returned successfully with borrow ID {borrow_id} on {checkin_date}.")  # Confirm success
    except sqlite3.Error as e:
        # Handle any database errors, such as invalid BorrowID
        print(f"Error returning resource: {e}")  # Print error message
    return None  # No return value

# Function to fetch available resources
def get_available_resources(arguments=None):
    # Query to fetch resources that are available
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
        WHERE Resource.AvailabilityStatus = 1  -- Only include resources marked as available
    """)
    available_resources = cursor.fetchall()  # Fetch all available resources

    # Check if any resources are available
    if available_resources:
        for resource in available_resources:
            # Print resource details, including ID, status, and title (from the first non-NULL title field)
            print(f"Resource ID: {resource[0]}, Availability: {resource[1]}, Title: {resource[2] or resource[3] or resource[4] or resource[5] or resource[6]}")
    else:
        # If no resources are available, notify the user
        print("No available resources found.")
    return None  # No return value


# Function to get members with overdue borrow logs
def get_overdue_members(arguments=None):
    # SQL query to find members with overdue borrow logs
    cursor.execute("""
        SELECT DISTINCT Member.MemberID, Member.MemberName
        FROM BorrowLog
        INNER JOIN Member ON BorrowLog.MemberID = Member.MemberID
        WHERE 
            (BorrowLog.CheckinDate IS NULL AND DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days') < DATE('now'))  
            OR 
            (BorrowLog.CheckinDate IS NOT NULL AND BorrowLog.CheckinDate > DATE(BorrowLog.CheckoutDate, '+' || BorrowLog.MaxDuration || ' days'))  
    """)
    overdue_members = cursor.fetchall()  # Fetch all results of overdue members

    # If there are overdue members, print their details
    if overdue_members:
        for member in overdue_members:
            print(f"Member ID: {member[0]}, Member Name: {member[1]}")
    else:
        # If no overdue members are found, notify the user
        print("No overdue members found.")
    return None

# Function to get books by a specific author
def get_author_books(arguments=None):
    # Check if arguments (AuthorID) are provided
    if arguments is None:
        print("Usage: get_author_books {AuthorID}")
        return None

    author_id = arguments.strip()  # Sanitize the input for author ID

    try:
        # SQL query to fetch books written by the given author ID
        cursor.execute("""
            SELECT PhysicalBook.Title, Audiobook.Title, eBook.Title
            FROM ResourceAuthor
            LEFT JOIN PhysicalBook ON ResourceAuthor.ResourceID = PhysicalBook.ResourceID
            LEFT JOIN Audiobook ON ResourceAuthor.ResourceID = Audiobook.ResourceID
            LEFT JOIN eBook ON ResourceAuthor.ResourceID = eBook.ResourceID
            WHERE ResourceAuthor.AuthorID = ? 
        """, (author_id,))
        author_books = cursor.fetchall()  # Fetch all books associated with the author

        # If books by the author are found, print their titles
        if author_books:
            for book in author_books:
                # Print the first non-null book title (PhysicalBook, Audiobook, or eBook)
                print(f"Book Title: {book[0] or book[1] or book[2]}")
        else:
            # If no books are found, notify the user
            print(f"No books found for Author ID {author_id}.")
    except sqlite3.Error as e:
        # Handle any database errors, such as invalid AuthorID or connection issues
        print(f"Error fetching author books: {e}")
    return None

command_map = {
    'help': help,  # Map 'help' command to the help function
    'get': get,  # Map 'get' command to the get function
    'get_members_borrow_log': get_members_borrow_log,  # Map 'get_members_borrow_log' to its function
    'get_overdue_borrow_logs': get_overdue_borrow_logs,  # Map 'get_overdue_borrow_logs' to its function
    'add_member': add_member,
    'reserve_room': reserve_room,
    'return_resource': return_resource,
    'borrow_resource': borrow_resource,
    'get_available_resources': get_available_resources,
    'get_overdue_members': get_overdue_members,
    'get_authors_books': get_author_books
}
