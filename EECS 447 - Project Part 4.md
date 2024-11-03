```sql
CREATE TABLE Member (
    ID INT PRIMARY KEY,
    Member_Name VARCHAR(255),
    Membertype VARCHAR(10),
    Starting_date VARCHAR(40),
    Birthday VARCHAR(20)
);

CREATE TABLE Room (
    Room_number INT PRIMARY KEY,
    Room_status BOOLEAN,
    Capacity INT
);

CREATE TABLE Borrow_log (
    Borrow_ID INT PRIMARY KEY,
    Checkout_date DATE,
    Checkin_date DATE,
    Maxduration INT
);

CREATE TABLE Resource (
    ID INT PRIMARY KEY,
    Resource_status BOOLEAN
);

CREATE TABLE Equipment (
    ID INT PRIMARY KEY,
    Model VARCHAR(255)
);

CREATE TABLE Physical_book (
    ISBN VARCHAR(13),
    Title VARCHAR(255),
    Author ,
    Publication_year YEAR,
    Publisher VARCHAR(255),
    Page_count INT,
    Genre VARCHAR(255)
);

CREATE TABLE Audiobook (
    ISBN VARCHAR(13),
    Title VARCHAR(255),
    Author ,
    Publication_year YEAR,
    Publisher VARCHAR(255),
    Duration INT,
    Genre VARCHAR(255)
);

CREATE TABLE eBook (
    ISBN VARCHAR(13),
    Title VARCHAR(255),
    Author ,
    Publication_year YEAR,
    Publisher VARCHAR(255),
    Genre VARCHAR(255)
);

CREATE TABLE Magazine (
    ISSN VARCHAR(8),
    Title VARCHAR(255),
    Issue_number INT,
    Publisher VARCHAR(255),
    Publication_year YEAR,
    Publication_month VARCHAR(255),
    Page_count INT
);

CREATE TABLE Digital_disk (
    ISSN VARCHAR(8),
    Title VARCHAR(255),
    Media_type VARCHAR(255),
    Disk_type VARCHAR(255),
    Release_year YEAR,
    Distributor VARCHAR(255),
    Genre VARCHAR(255)
);

CREATE TABLE Author (
    AuthorID INT,
    First_name VARCHAR(255),
    Last_name VARCHAR(255)
);

CREATE TABLE ResourceAuthor (
    ResourceID INT,
    AuthorID INT
);
```
