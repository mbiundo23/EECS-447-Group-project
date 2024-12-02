# Import necessary modules
import sqlite3

# Connect to the database
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

commands = [
    """CREATE TABLE Room (
        RoomNumber INT PRIMARY KEY,
        Capacity INT
    );""",
    """CREATE TABLE ResourceAuthor (
        ResourceID INT,
        AuthorID INT,
        PRIMARY KEY (ResourceID, AuthorID),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID),
        FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
    );""",
    """CREATE TABLE PhysicalBook (
        ResourceID INT PRIMARY KEY,
        ISBN VARCHAR(255) NOT NULL,
        Title VARCHAR(255) NOT NULL,
        PublicationYear INT,
        Publisher VARCHAR(255),
        PageCount INT NOT NULL,
        Genre VARCHAR(100),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
    );""",
    """CREATE TABLE Audiobook (
        ResourceID INT PRIMARY KEY,
        ISBN VARCHAR(255) NOT NULL,
        Title VARCHAR(255) NOT NULL,
        PublicationYear INT,
        Publisher VARCHAR(255),
        Duration INT NOT NULL,
        Genre VARCHAR(100),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
    );""",
    """CREATE TABLE Magazine (
        ResourceID INT PRIMARY KEY,
        ISSN VARCHAR(255) NOT NULL,
        Title VARCHAR(255) NOT NULL,
        IssueNumber INT NOT NULL,
        PublicationYear INT NOT NULL,
        PublicationMonth INT CHECK (PublicationMonth BETWEEN 1 AND 12),
        Publisher VARCHAR(255) NOT NULL,
        PageCount INT NOT NULL,
        Genre VARCHAR(100),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
    );""",
    """CREATE TABLE Resource (
        ResourceID INT PRIMARY KEY,
        AvailabilityStatus BOOL
    );""",
    """CREATE TABLE Equipment (
        ResourceID INT PRIMARY KEY,
        Model VARCHAR(255),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
    );""",
    """CREATE TABLE Author (
        AuthorID INT PRIMARY KEY,
        FirstName VARCHAR(255),
        LastName VARCHAR(255),
        MiddleInitial VARCHAR(1)
    );""",
    """CREATE TABLE eBook (
        ResourceID INT PRIMARY KEY,
        ISBN VARCHAR(255),
        Title VARCHAR(255),
        PublicationYear INT,
        Publisher VARCHAR(255),
        Genre VARCHAR(100),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
    );""",
    """CREATE TABLE DigitalDisk (
        ResourceID INT PRIMARY KEY,
        ISSN VARCHAR(255) NOT NULL,
        Title VARCHAR(255) NOT NULL,
        MediaType VARCHAR(255),
        DiskType VARCHAR(255),
        ReleaseYear INT NOT NULL,
        Distributor VARCHAR(255),
        Genre VARCHAR(100),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
    );""",
    """CREATE TABLE Member (
        MemberID INT PRIMARY KEY,
        MemberName VARCHAR(255),
        MembershipType VARCHAR(255),
        StartingDate VARCHAR(50),
        BirthDate DATE
    );""",
    """CREATE TABLE BorrowLog (
        BorrowID INT PRIMARY KEY,
        MemberID INT,
        ResourceID INT,
        CheckoutDate DATE,
        CheckinDate DATE,
        MaxDuration INT,
        FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
        FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
    );""",
    """CREATE TABLE ReserveRoom (
        ReserveDate DATE,
        RoomNumber INT,
        MemberID INT,
        PRIMARY KEY (ReserveDate, RoomNumber),
        FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber),
        FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
    );"""
]

# Execute all commands
for command in commands:
    cursor.execute(command)

print("Finished executing")
