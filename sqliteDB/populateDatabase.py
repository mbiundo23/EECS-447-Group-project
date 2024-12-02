# Import necessary modules
import sqlite3
import random 
from datetime import date, timedelta 

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

# Import all constants necessary for creating fake data
from constants import *

# Helper functions
def random_date(start, end):
    """Generate a random date between two dates."""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def random_bool():
    """Generate a random boolean."""
    return random.choice([True, False])

# Populate Resource table
for resource_id in range(1, 201): # Populate with 200 resources
    availability_status = random_bool()
    cursor.execute(f"INSERT INTO Resource VALUES ({resource_id}, {availability_status})")

# Populate Author table
for author_id in range(1, 51): # Populate with 50 authors
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    middle_initial = random.choice(MIDDLE_INITIALS) 
    middle_initial = None if middle_initial == "" else middle_initial
    cursor.execute(f"INSERT INTO Author VALUES ({author_id}, '{first_name}', '{last_name}', '{middle_initial}')")

# Populate PhysicalBook table
for resource_id in range(1, 26): # Populate with 25 physical books
    isbn = f"978-{random.randint(100000000, 999999999)}"
    title = "The" + " " + random.choice(ADJECTIVES) + " " + random.choice(BASEWORDS)
    publication_year = random.randint(2000, 2024)
    publisher = random.choice(PUBLISHERS)
    page_count = random.randint(100, 1000)
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO PhysicalBook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', {page_count}, '{genre}'
        )
    """)

# Populate Audiobook table
for resource_id in range(26, 51): # Populate with 25 audiobooks
    isbn = f"978-{random.randint(100000000, 999999999)}"
    title = "The" + " " + random.choice(ADJECTIVES) + " " + random.choice(BASEWORDS)
    publication_year = random.randint(2000, 2024)
    publisher = random.choice(PUBLISHERS)
    duration = random.randint(60, 300)  # Duration in minutes
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO Audiobook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', {duration}, '{genre}'
        )
    """)

# Populate Magazine table
for resource_id in range(51, 76): # Populate with 25 magazines
    issn = f"1234-{random.randint(100000, 999999)}"
    title = "The" + " " + random.choice(ADJECTIVES) + " " + random.choice(BASEWORDS)
    issue_number = random.randint(1, 50)
    publication_year = random.randint(2000, 2024)
    publication_month = random.randint(1, 12)
    random.choice(PUBLISHERS)
    page_count = random.randint(30, 200)
    genre = random.choice(MAGAZINE_GENRES)
    cursor.execute(f"""
        INSERT INTO Magazine VALUES (
            {resource_id}, '{issn}', '{title}', {issue_number}, {publication_year}, {publication_month}, '{publisher}', {page_count}, '{genre}'
        )
    """)

# Populate eBook table
for resource_id in range(76, 101): # Populate with 25 eBooks
    isbn = f"978-{random.randint(100000000, 999999999)}"
    title = "The" + " " + random.choice(ADJECTIVES) + " " + random.choice(BASEWORDS)
    publication_year = random.randint(2000, 2024)
    publisher = random.choice(PUBLISHERS)
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO eBook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', '{genre}'
        )
    """)

# Populate Equipment table
for resource_id in range(101, 126): # Populate with 25 equipment
    model = random.choice(EQUIPMENT_MODELS)
    cursor.execute(f"""
        INSERT INTO Equipment VALUES (
            {resource_id}, '{model}'
        )
    """)

# Populate DigitalDisk table
for resource_id in range(126, 151): # Populate with 25 digital disks
    issn = f"1234-{random.randint(100000, 999999)}"
    title = "The" + " " + random.choice(ADJECTIVES) + " " + random.choice(BASEWORDS)
    media_type = random.choice(MEDIA_TYPES)
    disk_type = random.choice(DIGITAL_DISK_TYPES)
    release_year = random.randint(2000, 2024)
    distributor = f"Publisher{resource_id}"
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO DigitalDisk VALUES (
            {resource_id}, '{issn}', '{title}', '{media_type}', '{disk_type}', {release_year}, '{distributor}', '{genre}'
        )
    """)

# Populate Member table
for member_id in range(1, 51): # Populate with 50 members
    member_name = random.choice(FIRST_NAMES) + " " + random.choice(MIDDLE_INITIALS) + " " + random.choice(LAST_NAMES)
    membership_type = random.choice(["Regular", "Student", "Senior"])
    starting_date = random_date(date(2020, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
    birth_date = random_date(date(1900, 1, 1), date(2005, 12, 31)).strftime('%Y-%m-%d')
    cursor.execute(f"""
        INSERT INTO Member VALUES (
            {member_id}, '{member_name}', '{membership_type}', '{starting_date}', '{birth_date}'
        )
    """)

# Populate BorrowLog table
for borrow_id in range(1, 101): # Populate with 100 borrow logs
    member_id = random.randint(1, 50)  # Updated member_id range (should be from 1 to 50)
    resource_id = random.randint(1, 200)  # Updated resource_id range (should be from 1 to 200)
    checkout_date = random_date(date(2023, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
    checkin_date = random_date(date(2024, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
    max_duration = random.randint(7, 30) # duration in days
    cursor.execute(f"""
        INSERT INTO BorrowLog VALUES (
            {borrow_id}, {member_id}, {resource_id}, '{checkout_date}', '{checkin_date}', {max_duration}
        )
    """)

# Populate Room table
for room_number in range(1, 21):  # Populate with 20 rooms
    availability_status = random_bool()
    capacity = random.randint(5, 50)  # Random room capacity between 5 and 50
    cursor.execute(f"""
        INSERT INTO Room VALUES (
            {room_number}, {availability_status}, {capacity}
        )
    """)

# Populate ResourceAuthor table
for resource_id in range(1, 201): # Link resources with authors
    authors_used = set() # Keep track of authors already assigned to this resource_id
    num_authors = random.randint(1, 3) # Randomly assign between 1 and 3 authors to a resource
    for _ in range(num_authors):
        author_id = random.randint(1, 51) # Random author
        # Skip if this author_id has already been assigned to the current resource_id
        if author_id not in authors_used:
            cursor.execute(f"""
                INSERT INTO ResourceAuthor (ResourceID, AuthorID) VALUES (
                    {resource_id}, {author_id}
                )
            """)
            authors_used.add(author_id) # Mark this author_id as used for this resource_id

# Populate ReserveRoom table
for room_number in range(1, 21):  # For each room
    for member_id in range(1, 51):  # For each member
        reserve_date = random_date(date(2024, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
        cursor.execute(f"""
            INSERT INTO ReserveRoom VALUES (
                '{reserve_date}', {room_number}, {member_id}
            )
        """)

# Populate Write table
for resource_id in range(1, 201):  # For each resource
    num_authors = random.randint(1, 3)  # Randomly assign between 1 and 3 authors
    for _ in range(num_authors):
        author_id = random.randint(1, 51)  # Random author
        write_date = random_date(date(2000, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
        cursor.execute(f"""
            INSERT INTO Write VALUES (
                '{write_date}', {resource_id}, {author_id}
            )
        """)

# Commit and close the connection
connection.commit()
connection.close()

print("Database populated successfully.")
