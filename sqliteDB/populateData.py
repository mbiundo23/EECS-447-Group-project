import sqlite3
import random
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

"""
ResourceID INT PRIMARY KEY,
    ISBN VARCHAR(255) NOT NULL,
    Title VARCHAR(255) NOT NULL,
    PublicationYear INT,
    Publisher VARCHAR(255),
    PageCount INT NOT NULL,
    Genre VARCHAR(100),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
"""

adjectives = ["Epic", "The", "Tale", "Red", "Orange"]
words = ["Car", "House", "Man"]
genres = ["Fantasy", "Sci-Fi", "Fiction", "Autobiography"]


for ID in range(1,10):

  isbn = ID
  title = random.choice(adjectives) + random.choice(words)
  publicationYear = random.randint(2000,2024)
  publisher = random.choice(adjectives) + random.choice(words)
  pagecount = random.randint(1,1000)
  genre = random.choice(genres)
  
  cursor.execute(f'''INSERT INTO PhysicalBook VALUES({isbn}, '{title}', 
                     {publicationYear}, '{publisher}', {pagecount}, '{genre}', NULL)''')
  
cursor.execute("SELECT * From PhysicalBook")
results = cursor.fetchall()
print(results)
  
