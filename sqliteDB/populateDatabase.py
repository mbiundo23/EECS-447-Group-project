import sqlite3
import random
from datetime import date, timedelta

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

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
for resource_id in range(1, 21):  # 20 resources
    availability_status = random_bool()
    cursor.execute(f"INSERT INTO Resource VALUES ({resource_id}, {availability_status})")

# Populate Author table
for author_id in range(1, 11):  # 10 authors
    first_name = f"AuthorFirst{author_id}"
    last_name = f"AuthorLast{author_id}"
    middle_initial = random.choice(["A", "B", "C", "D", None])
    cursor.execute(f"INSERT INTO Author VALUES ({author_id}, '{first_name}', '{last_name}', '{middle_initial}')")

# Populate PhysicalBook table
for resource_id in range(1, 6):  # 5 physical books
    isbn = f"978-{random.randint(100000000, 999999999)}"
    title = f"BookTitle{resource_id}"
    publication_year = random.randint(2000, 2024)
    publisher = f"Publisher{resource_id}"
    page_count = random.randint(100, 1000)
    genre = random.choice(["Fiction", "Non-Fiction", "Sci-Fi", "Fantasy"])
    cursor.execute(f"""
        INSERT INTO PhysicalBook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', {page_count}, '{genre}'
        )
    """)

# Populate Audiobook table
for resource_id in range(6, 11):  # 5 audiobooks
    isbn = f"978-{random.randint(100000000, 999999999)}"
    title = f"AudiobookTitle{resource_id}"
    publication_year = random.randint(2000, 2024)
    publisher = f"Publisher{resource_id}"
    duration = random.randint(60, 300)  # Duration in minutes
    genre = random.choice(["Fiction", "Non-Fiction", "Sci-Fi", "Fantasy"])
    cursor.execute(f"""
        INSERT INTO Audiobook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', {duration}, '{genre}'
        )
    """)

# Populate Magazine table
for resource_id in range(11, 16):  # 5 magazines
    issn = f"1234-{random.randint(100000, 999999)}"
    title = f"MagazineTitle{resource_id}"
    issue_number = random.randint(1, 50)
    publication_year = random.randint(2000, 2024)
    publication_month = random.randint(1, 12)
    publisher = f"Publisher{resource_id}"
    page_count = random.randint(30, 200)
    genre = random.choice(["Science", "Art", "Technology"])
    cursor.execute(f"""
        INSERT INTO Magazine VALUES (
            {resource_id}, '{issn}', '{title}', {issue_number}, {publication_year}, {publication_month}, '{publisher}', {page_count}, '{genre}'
        )
    """)

# Populate eBook table
for resource_id in range(16, 21):  # 5 eBooks
    isbn = f"978-{random.randint(100000000, 999999999)}"
    title = f"eBookTitle{resource_id}"
    publication_year = random.randint(2000, 2024)
    publisher = f"Publisher{resource_id}"
    genre = random.choice(["Fiction", "Non-Fiction", "Romance", "Adventure"])
    cursor.execute(f"""
        INSERT INTO eBook VALUES (
            {resource_id}, '{isbn}', '{title}', {publication_year}, '{publisher}', '{genre}'
        )
    """)

# Populate Member table
for member_id in range(1, 11):  # 10 members
    member_name = f"MemberName{member_id}"
    membership_type = random.choice(["Standard", "Premium", "Student"])
    starting_date = random_date(date(2020, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
    birth_date = random_date(date(1980, 1, 1), date(2005, 12, 31)).strftime('%Y-%m-%d')
    cursor.execute(f"""
        INSERT INTO Member VALUES (
            {member_id}, '{member_name}', '{membership_type}', '{starting_date}', '{birth_date}'
        )
    """)

# Populate BorrowLog table
for borrow_id in range(1, 11):  # 10 borrow logs
    member_id = random.randint(1, 10)
    resource_id = random.randint(1, 20)
    checkout_date = random_date(date(2023, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
    checkin_date = random_date(date(2024, 1, 1), date(2024, 12, 31)).strftime('%Y-%m-%d')
    max_duration = random.randint(7, 30)  # in days
    cursor.execute(f"""
        INSERT INTO BorrowLog VALUES (
            {borrow_id}, {member_id}, {resource_id}, '{checkout_date}', '{checkin_date}', {max_duration}
        )
    """)

# Commit and close the connection
connection.commit()
connection.close()

print("Database populated successfully.")
