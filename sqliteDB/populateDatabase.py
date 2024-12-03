# Import necessary modules
import sqlite3
import random 
from datetime import date, timedelta 

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

# Import all constants necessary for creating fake data
from constants import *

# All unique values to be stored
isbns = set() # Set of unique isbns
issns = set() # Set of unique issns

# Helper functions

# Generate a random date between two dates.
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Generate a random boolean.
def random_bool():
    return random.choice([True, False])

# Generate a random title.
def generate_title():
    title = f"The {random.choice(ADJECTIVES)} {random.choice(BASEWORDS)}" # Title generated
    return title

# Generate a random isbn
def generate_isbn():
    while True:
        isbn = f"978-{random.randint(100000000, 999999999)}"
        if isbn not in isbns: # Ensure isbn is unique
            isbns.add(isbn)
            return isbn
            
# Generate a random issn
def generate_issn():
    while True:
        issn = f"1234-{random.randint(100000, 999999)}"
        if issn not in issns: # Ensure issn is unique
            issns.add(issn)
            return issn

# Create all Resources 
def populate_resource(number_of_resources):
    # Populate Resource table
    for resource_id in range(1, number_of_resources+1): # Populate with given number of resources
        availability_status = True # Initialize all resources to be available. This will change as we simulate users borrowing.
        cursor.execute(f"INSERT INTO Resource VALUES ({resource_id}, {availability_status})")
        chosen_resource = random.choice(RESOURCE_TYPES)
        if chosen_resource == "PhysicalBook":
            populate_physical_book(resource_id)
        elif chosen_resource == "eBook":
            populate_ebook(resource_id)
        elif chosen_resource == "AudioBook":
            populate_audio_book(resource_id)
        elif chosen_resource == "Magazine":
            populate_magazine(resource_id)
        elif chosen_resource == "Equipment":
            populate_equipment(resource_id)
        elif chosen_resource == "DigitalDisk":
            populate_digital_disk(resource_id)

# Populate Author table
def populate_author(number_of_authors):
    for author_id in range(1, number_of_authors+1): # Populate with given number of authors
        first_name = random.choice(FIRST_NAMES) # Random first name
        last_name = random.choice(LAST_NAMES) # Random last name
        middle_initial = random.choice(MIDDLE_INITIALS) # Random niddle inital
        cursor.execute(f"""
                        INSERT INTO Author (AuthorID, FirstName, LastName, MiddleInitial) 
                        VALUES ({author_id}, '{first_name}', '{last_name}', 
                        {f"'{middle_initial}'" if middle_initial != '' else 'NULL'})
                    """)
        
# Populate PhysicalBook table
def populate_physical_book(resource_id):
    isbn = generate_isbn()
    title = generate_title() # Title generated
    publication_year = random.randint(EARLIEST_PUBLICATION_YEAR, date.today().year)
    publisher = random.choice(PUBLISHERS)
    page_count = random.randint(10, 1000)
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO PhysicalBook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', {page_count}, '{genre}'
        )
    """)

# Populate Audiobook table
def populate_audio_book(resource_id):
    isbn = generate_isbn()
    title = generate_title()
    publication_year = random.randint(EARLIEST_PUBLICATION_YEAR, date.today().year)
    publisher = random.choice(PUBLISHERS)
    duration = random.randint(60, 300)  # Duration in minutes
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO Audiobook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', {duration}, '{genre}'
        )
    """)
    
# Populate Magazine table
def populate_magazine(resource_id):
    issn = generate_issn()
    title = generate_title()
    issue_number = random.randint(1, 50)
    publication_year = random.randint(EARLIEST_PUBLICATION_YEAR, date.today().year)
    publication_month = random.randint(1, 12)
    publisher = random.choice(PUBLISHERS)
    page_count = random.randint(30, 200)
    genre = random.choice(MAGAZINE_GENRES)
    cursor.execute(f"""
        INSERT INTO Magazine VALUES (
            {resource_id}, '{issn}', '{title}', {issue_number}, {publication_year}, {publication_month}, '{publisher}', {page_count}, '{genre}'
        )
    """)

# Populate eBook table
def populate_ebook(resource_id):
    isbn = generate_isbn()
    title = generate_title()
    publication_year = random.randint(EARLIEST_PUBLICATION_YEAR, date.today().year)
    publisher = random.choice(PUBLISHERS)
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO eBook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', '{genre}'
        )
    """)

# Populate Equipment table
def populate_equipment(resource_id):
    model = random.choice(EQUIPMENT_MODELS)
    cursor.execute(f"""
        INSERT INTO Equipment VALUES (
            {resource_id}, '{model}'
        )
    """)

# Populate DigitalDisk table
def populate_digital_disk(resource_id):
    issn = generate_issn()
    title = generate_title()
    media_type = random.choice(MEDIA_TYPES)
    disk_type = random.choice(DIGITAL_DISK_TYPES)
    release_year = random.randint(EARLIEST_PUBLICATION_YEAR, date.today().year)
    distributor = random.choice(DISTRIBUTORS)
    genre = random.choice(GENRES)
    cursor.execute(f"""
        INSERT INTO DigitalDisk VALUES (
            {resource_id}, '{issn}', '{title}', '{media_type}', '{disk_type}', {release_year}, '{distributor}', '{genre}'
        )
    """)

# Populate ResourceAuthor table
def populate_resource_author(number_of_resources, number_of_authors):
    for resource_id in range(1, number_of_resources+1):
        authors_used = set() # Keep track of authors already assigned to this resource_id
        num_authors = random.randint(1, MAX_AUTHORS) # Randomly assign between 1 and MAX_AUTHORS authors to a resource
        for _ in range(num_authors):
            author_id = random.randint(1, number_of_authors) # Random author
            if author_id not in authors_used: # Ensure author is not already associated with this resource.
                cursor.execute(f"""
                    INSERT INTO ResourceAuthor (ResourceID, AuthorID) VALUES (
                        {resource_id}, {author_id}
                    )
                """)
                authors_used.add(author_id) # Mark this author_id as used for this resource_id

# Populate Member table
def populate_member(number_of_members):
    for member_id in range(1, number_of_members+1): # Populate with given number of members
        middle_initial = random.choice(MIDDLE_INITIALS)
        if middle_initial:
            member_name = f"{random.choice(FIRST_NAMES)} {middle_initial} {random.choice(LAST_NAMES)}"
        else:
             member_name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        starting_date = random_date(date(2020, 1, 1), date.today()).strftime('%Y-%m-%d')
        birth_date = random_date(date(1900, 1, 1), date.today())
        age = (date.today() - birth_date).days // 365 # Calculate approximate age
        birth_date = birth_date.strftime('%Y-%m-%d')
        if age >= SENIOR_AGE: # Automatically grant seniors Senior status.
            membership_type = "Senior"
        elif 5 <= age <= 18: # Automatically grant young people Student status.
            membership_type = "Student"
        else: # Randomly assign regular or students, since students arent always neccessarily young.
            membership_type = random.choice([type for type in MEMBERSHIP_TYPES if type != "Senior"])
        cursor.execute(f"""
        INSERT INTO Member VALUES (
                {member_id}, '{member_name}', '{membership_type}', '{starting_date}', '{birth_date}'
        )
        """)

# Populate BorrowLog table
def populate_borrow_log(number_of_borrows, number_of_members, number_of_resources):
    for borrow_id in range(1, number_of_borrows + 1):
        member_id = random.randint(1, number_of_members)
        resource_id = random.randint(1, number_of_resources)
        checkout_date = random_date(date(2023, 1, 1), date.today())
        
        # Randomly decide if the resource is returned
        is_returned = random.choice([True, False])
        checkin_date = (
            random_date(checkout_date, date.today()) if is_returned else None
        )
        max_duration = random.randint(7, 30)
        
        # Insert the borrow log
        cursor.execute(f"""
            INSERT INTO BorrowLog VALUES (
                {borrow_id}, {member_id}, {resource_id}, '{checkout_date}', 
                {f"'{checkin_date}'" if checkin_date else 'NULL'}, {max_duration}
            )
        """)

        # Update the availability status only if not returned
        if not is_returned:
            cursor.execute(f"""
                UPDATE Resource 
                SET AvailabilityStatus = False 
                WHERE ResourceID = {resource_id}
            """)

# Populate Room table
def populate_room(number_of_rooms, min_capacity, max_capacity):
    for room_number in range(1, number_of_rooms+1):
        capacity = random.randint(min_capacity, max_capacity) # Random room capacity between given min and max capacity.
        cursor.execute(f"""
            INSERT INTO Room VALUES (
                {room_number}, {capacity}
            )
        """)

# Populate ReserveRoom table
def populate_reserve_room(number_of_reservations, number_of_rooms, number_of_members):
    unique_key = set() # Unique keys
    for num in range(1, number_of_reservations + 1):
        while True:
            room_number = random.randint(1, number_of_rooms) # select a random room to be reserved for the day
            reserve_date = random_date(date.today(), date.today() + timedelta(weeks=9)) # Allow for reservations up to 9 weeks in advance
            member_id = random.randint(1, number_of_members + 1) 
            if (reserve_date, room_number) not in unique_key:
                cursor.execute(f"""
                    INSERT INTO ReserveRoom VALUES (
                        '{reserve_date}', {room_number}, {member_id}
                    )
                """)
                unique_key.add((reserve_date, room_number))
                break

# Populate database with hardcoded values
populate_resource(NUMBER_OF_RESOURCES)
populate_author(NUMBER_OF_AUTHORS)
populate_resource_author(NUMBER_OF_RESOURCES, NUMBER_OF_AUTHORS)
populate_member(NUMBER_OF_MEMBERS)
populate_borrow_log(NUMBER_OF_BORROWS, NUMBER_OF_MEMBERS, NUMBER_OF_RESOURCES)
populate_room(NUMBER_OF_ROOMS, MIN_CAPACITY, MAX_CAPACITY)
populate_reserve_room(NUMBER_OF_RESERVATIONS, NUMBER_OF_ROOMS, NUMBER_OF_MEMBERS)

# Commit and close the connection
connection.commit()
connection.close()
print("Database populated successfully.")
