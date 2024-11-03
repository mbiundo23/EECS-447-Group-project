# Introduction

## Project Overview

This project aims to develop a database to cover the borrowing and management of media items in a small library. The database will track items such as books, eBooks, audiobooks, magazines, and digital disks, including their availability and borrowing status. The database also tracks the borrowing of electronics, tools and printers and room reservations.

## Scope

The purpose of the database is to track the media items in the library; Who has a given item checked out, is it available still, etc. This is not related to higher-level administration (budgeting, payroll, etc.).

## Glossary

- **ISBN:** International Standard Book Number, a unique identifier for books.
- **ISSN:** International Standard Serial Number, a unique identifier for serial publications like magazines.
  - **Media Items:** Various types of content available for borrowing, including books, eBooks, audiobooks, magazines, and digital disks.
  - **Member:** A registered individual who can borrow media items from the library.

# Relational Schema Mapping

## Identify Relations

## Define attributes and domains

## Determine primary keys

## Establish foreign keys

# Schema Documentation

## Relational Schema Diagram

## Data Dictionary

# Generate DDL

```sql
CREATE TABLE Member (
    ID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    MiddleNnitial VARCHAR(1),
    MemberType VARCHAR(10),
    StartingDate VARCHAR(40),
    Birthday VARCHAR(20)
);

CREATE TABLE Room (
    RoomNumber INT PRIMARY KEY,
    RoomStatus BOOLEAN,
    Capacity INT
);

CREATE TABLE Borrow_log (
    BorrowID INT PRIMARY KEY,
    CheckoutDate DATE,
    CheckinDate DATE,
    Maxduration INT
);

CREATE TABLE Resource (
    ID INT PRIMARY KEY,
    ResourceStatus BOOLEAN
);

CREATE TABLE Equipment (
    ID INT PRIMARY KEY,
    Model VARCHAR(255)
);

CREATE TABLE Physical_book (
    ISBN VARCHAR(13),
    Title VARCHAR(255),
    AuthorID INT,
    PublicationYear YEAR,
    Publisher VARCHAR(255),
    PageCount INT,
    Genre VARCHAR(255)
);

CREATE TABLE Audiobook (
    ISBN VARCHAR(13),
    Title VARCHAR(255),
    AuthorID INT,
    PublicationYear YEAR,
    Publisher VARCHAR(255),
    Duration INT,
    Genre VARCHAR(255)
);

CREATE TABLE eBook (
    ISBN VARCHAR(13),
    Title VARCHAR(255),
    AuthorID INT,
    PublicationYear YEAR,
    Publisher VARCHAR(255),
    Genre VARCHAR(255)
);

CREATE TABLE Magazine (
    ISSN VARCHAR(8),
    Title VARCHAR(255),
    IssueNumber INT,
    Publisher VARCHAR(255),
    PublicationYear YEAR,
    PublicationMonth VARCHAR(255),
    PageCount INT
);

CREATE TABLE Digital_disk (
    ISSN VARCHAR(8),
    Title VARCHAR(255),
    MediaType VARCHAR(255),
    DiskType VARCHAR(255),
    ReleaseYear YEAR,
    Distributor VARCHAR(255),
    Genre VARCHAR(255)
);

CREATE TABLE Author (
    AuthorID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    MiddleInitial VARCHAR(1)
);

CREATE TABLE ResourceAuthor (
    ResourceID INT,
    AuthorID INT,
    FOREIGN KEY (ResourceID) REFERENCES Resource(ResourceID),
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);
```

# Normalization Considerations

# Appendices
