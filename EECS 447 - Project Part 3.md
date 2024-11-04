# EECS 447 - Project Part 3

## Objective

Develop a comprehensive Entity-Relationship (ER) diagram that accurately represents the data requirements and relationships for your database project.

Now that you have documented the requirements of your database project, the next step is to prepare a conceptual model. This model will serve as a blueprint for your database design, capturing the essential entities, relationships, and constraints based on the requirements you have gathered.

---

## Introduction

### Project Overview

This project aims to develop a database to cover the borrowing and management of media items in a small library. The database will track items such as books, eBooks, audiobooks, magazines, and digital disks, including their availability and borrowing status. The database also tracks the borrowing of electronics, tools and printers and room reservations.

### Scope

The purpose of the database is to track the media items in the library; Who has a given item checked out, is it available still, etc. This is not related to higher-level administration (budgeting, payroll, etc.).

### Glossary

- **ISBN:** International Standard Book Number, a unique identifier for books.
- **ISSN:** International Standard Serial Number, a unique identifier for serial publications like magazines.
  - **Media Items:** Various types of content available for borrowing, including books, eBooks, audiobooks, magazines, and digital disks. 
  - **Member:** A registered individual who can borrow media items from the library.

---

## Entities

### Define Attributes

- **Resource**
  
  - ResourceID `INT` `PRIMARY KEY`
    
    - An item's primary resource ID, unique for the library's inventory.
  
  - AvailabilityStatus `BOOL`
    
    - Boolean representing whether the resource is available in the library or not.

- **Physical Book**
  
  * ResourceID `INT` `Primary Key`
    
    * An item's primary resource ID, unique for the library's inventory.
  - ISBN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify a book.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the book's name.
  - Publication Year `YEAR`
    - The year the book was published.
  - Publisher `VARCHAR(255)`
    - A publisher's name with a limit of 255 characters, showing who published the book.
  - Page Count `SMALLINT UNSIGNED`
    - The total number of pages in the book.
  - Genre `VARCHAR(100)`
    - The genre of the book, with a limit of 100 characters.

- ****eBook****
  
  * ResourceID `INT` `Primary Key`
    
    - An item's primary resource ID, unique for the library's inventory.
  - ISBN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify an eBook.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the eBook's name.
  - Publication Year `YEAR`
    - The year the eBook was published.
  - Publisher `VARCHAR(255)`
    - A publisher's name with a limit of 255 characters, showing who published the eBook.
  - Genre `VARCHAR(100)`
    - The genre of the eBook, with a limit of 100 characters.

- ****Audiobook****
  
  * ResourceID `INT` `Primary Key`
    
    - An item's primary resource ID, unique for the library's inventory.
  - ISBN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify an audiobook.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the audiobook's name.
  - Publication Year `YEAR`
    - The year the audiobook was released.
  - Publisher `VARCHAR(255)`
    - A publisher's name with a limit of 255 characters, showing who published the audiobook.
  - Duration (Seconds) `MEDIUMINT UNSIGNED`
    - The total length of the audiobook in seconds.
  - Genre `VARCHAR(100)`
    - The genre of the audiobook, with a limit of 100 characters.

- ****Magazine****
  
  * ResourceID `INT` `Primary Key`
    
    - An item's primary resource ID, unique for the library's inventory.
  - ISSN `CHAR(8)` `Primary Key`
    - An identifier with exactly 8 characters used to uniquely identify a magazine.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the magazine's name.
  - Issue Number `INT UNSIGNED`
    - The specific issue number of the magazine.
  - Publisher `VARCHAR(255)`
    - A publisher's name with a limit of 255 characters, showing who published the magazine.
  - Publication Year `YEAR`
    - The year the magazine issue was published.
  - Publication Month `TINYINT UNSIGNED`
    - The month when the magazine issue was published (1-12).
  - Page Count `SMALLINT UNSIGNED`
    - The total number of pages in the magazine.
  - Genre `VARCHAR(255)`
    - The genre of the digital disk, with a limit of 255 characters.

- ****Digital Disk****
  
  * ResourceID `INT` `Primary Key`
    
    - An item's primary resource ID, unique for the library's inventory.
  - ISSN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify a digital disk.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the digital disk's name.
  - Release Year `YEAR`
    - The year the digital disk was released.
  - Distributor `VARCHAR(255)`
    - A distributor's name with a limit of 255 characters, showing who distributed the digital disk.
  - Genre `VARCHAR(255)`
    - The genre of the digital disk, with a limit of 255 characters.
  - Disk Type `ENUM('CD', 'DVD', 'VHS', 'Other')`
    - The type of disk, indicating the medium format of the digital content.
  - Media Type `ENUM('Video Game', 'Movie', 'Other')`
    - The type of media, categorizing the digital content (e.g., video game or movie).
- **Equipment**
  - ResourceID `INT` `Primary Key` `FOREIGN KEY`
    - An item's primary resource ID, unique for the library's inventory.
  - Model `VARCHAR(255)`
    - The model name of the object with a limit of 255 characters.

- ****Author****
  
  - AuthorID `INT UNSIGNED` `Primary Key`
    - A unique identifier for each author.
  - First Name `VARCHAR(255)`
    - The author's first name with a limit of 255 characters.
  - Last Name `VARCHAR(255)`
    - The author's last name with a limit of 255 characters.
  - Middle Initial `VARCHAR(1)`
    - The author's middle name with a limit of 1 character (optional).

- ****Member****
  
  - MemberID `INT UNSIGNED` `Primary Key`
    - A unique identifier for each library member.
  - Name `VARCHAR(255)`
    - The author's name with a limit of 255 characters.
  - MembershipType `VARCHAR(255)`
    - Level of membership of the member, such as "standard", "senior", "student".
  - StartingDate `VARCHAR(50)`
    - Date representing when the membership of the given member began.
  - BirthDate `DATE`
    - Date representing the birthdate of the member.
- **BorrowLog**
  - BorrowID `INT` `PRIMARY KEY`
    - A unique identifier for each borrowed entry.
  - MemberID `INT` `FOREIGN KEY`
    - A unique identifier for each library member.
  - ResourceID `INT` `FOREIGN KEY`
    - An item's primary resource ID, unique for the library's inventory.
  - CheckoutDate `DATE`
    - Date representing when the given object was checked out.
  - CheckinDate `DATE`
    - Date representing when the given object was checked in.
  - MaxDuration `INT`
    - Int representing the maximum number of days that the item is supposed to be borrowed for.

### Relationships

- Write (Book, eBook, Audiobook) many-to-many (Author)
- Borrow (Member) zero-to-five (Resource)
- (Room) can be reserved by one-to-one (Member)

---

## ER Diagram

Diagram can be found [here](https://github.com/mbiundo23/EECS-447-Group-project/blob/main/Eecs447_Project_ERDiagram.drawio.pdf).

---

## Appendices

The entities and relationships are not final as we are still disccusing the possibility of exploring generalization for media based entities such as books, ebooks, audio books magazines, and disks belonging to a generalized entity. Another topic we discussed is the possibility of using an Author ID/Publisher ID as a foreign key to media based entities. Additionally, for room reservations, we discussed the possibility of adding a time block as a composite attribute that holds both the date and time. 
