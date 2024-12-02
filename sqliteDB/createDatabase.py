import sqlite3
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

command1 = """CREATE TABLE Room (
    RoomNumber INT PRIMARY KEY,
    AvailabilityStatus BOOL,
    Capacity INT
);"""

command2 = """CREATE TABLE ResourceAuthor (
    ResourceID INT,
    AuthorID INT,
    PRIMARY KEY (ResourceID, AuthorID),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID),
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);"""

command3 = """CREATE TABLE PhysicalBook (
    ResourceID INT PRIMARY KEY,
    ISBN VARCHAR(255) NOT NULL,
    Title VARCHAR(255) NOT NULL,
    PublicationYear INT,
    Publisher VARCHAR(255),
    PageCount INT NOT NULL,
    Genre VARCHAR(100),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);"""

command4 = """
CREATE TABLE Audiobook (
    ResourceID INT PRIMARY KEY,
    ISBN VARCHAR(255) NOT NULL,
    Title VARCHAR(255) NOT NULL,
    PublicationYear INT,
    Publisher VARCHAR(255),
    Duration INT NOT NULL,
    Genre VARCHAR(100),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);"""

command5 = """CREATE TABLE Magazine (
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
);
"""

command6 = """CREATE TABLE Resource (
    ResourceID INT PRIMARY KEY,
    AvailabilityStatus BOOL
);
"""

command7 = """CREATE TABLE Equipment (
    ResourceID INT PRIMARY KEY,
    Model VARCHAR(255),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);"""

command8 = """CREATE TABLE Author (
    AuthorID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    MiddleInitial VARCHAR(1)
);"""

command9 = """CREATE TABLE eBook (
    ResourceID INT PRIMARY KEY,
    ISBN VARCHAR(255),
    Title VARCHAR(255),
    PublicationYear INT,
    Publisher VARCHAR(255),
    Genre VARCHAR(100),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);"""

command10 = """CREATE TABLE DigitalDisk (
    ResourceID INT PRIMARY KEY,
    ISSN VARCHAR(255) NOT NULL,
    Title VARCHAR(255) NOT NULL,
    MediaType VARCHAR(255),
    DiskType VARCHAR(255),
    ReleaseYear INT NOT NULL,
    Distributor VARCHAR(255),
    Genre VARCHAR(100),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)

);"""

command11 = """CREATE TABLE Member (
    MemberID INT PRIMARY KEY,
    MemberName VARCHAR(255),
    MembershipType VARCHAR(255),
    StartingDate VARCHAR(50),
    BirthDate DATE
);
"""

command12 = """
CREATE TABLE BorrowLog (
    BorrowID INT PRIMARY KEY,
    MemberID INT,
    ResourceID INT,
    CheckoutDate DATE,
    CheckinDate DATE,
    MaxDuration INT,
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID)
);"""

command13 = """CREATE TABLE ReserveRoom (
    ReserveDate DATE,
    RoomNumber INT,
    MemberID INT,
    PRIMARY KEY (ReserveDate, RoomNumber, MemberID),
    FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
);"""

command14 = """CREATE TABLE Write (
    Date DATE,
    ResourceID INT,
    AuthorID INT,
    PRIMARY KEY (Date, ResourceID, AuthorID),
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID),
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);
"""

#cursor.execute(command1)


cursor.execute(command2)
cursor.execute(command3)
cursor.execute(command4)
cursor.execute(command5)
cursor.execute(command6)
cursor.execute(command7)
cursor.execute(command8)
cursor.execute(command9)
cursor.execute(command10)
cursor.execute(command11)
cursor.execute(command12)
cursor.execute(command13)
cursor.execute(command14)
print("Finished executing")


