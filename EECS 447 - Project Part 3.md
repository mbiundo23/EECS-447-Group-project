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

- ****Book****
  
  - ISBN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify a book.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the book's name.
  - Author `VARCHAR(255)`
    - An author's name with a limit of 255 characters, indicating who wrote the book.
  - Publication Year `YEAR`
    - The year the book was published.
  - Publisher `VARCHAR(255)`
    - A publisher's name with a limit of 255 characters, showing who published the book.
  - Page Count `SMALLINT UNSIGNED`
    - The total number of pages in the book.
  - Available Quantity `TINYINT UNSIGNED`
    - The number of copies of the book currently available for borrowing.
  - Total Quantity `TINYINT UNSIGNED`
    - The total number of copies of the book in the library.
  - Genre `VARCHAR(100)`
    - The genre of the book, with a limit of 100 characters.

- ****eBook****
  
  - ISBN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify an eBook.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the eBook's name.
  - Author `VARCHAR(255)`
    - An author's name with a limit of 255 characters, indicating who wrote the eBook.
  - Publication Year `YEAR`
    - The year the eBook was published.
  - Publisher `VARCHAR(255)`
    - A publisher's name with a limit of 255 characters, showing who published the eBook.
  - Available Quantity `TINYINT UNSIGNED`
    - The number of copies of the eBook currently available for download or access.
  - Total Quantity `TINYINT UNSIGNED`
    - The total number of copies of the eBook in the library.
  - Genre `VARCHAR(100)`
    - The genre of the eBook, with a limit of 100 characters.

- ****Audiobook****
  
  - ISBN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify an audiobook.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the audiobook's name.
  - Author `VARCHAR(255)`
    - An author's name with a limit of 255 characters, indicating who narrated or created the audiobook.
  - Publication Year `YEAR`
    - The year the audiobook was released.
  - Publisher `VARCHAR(255)`
    - A publisher's name with a limit of 255 characters, showing who published the audiobook.
  - Duration (Seconds) `MEDIUMINT UNSIGNED`
    - The total length of the audiobook in seconds.
  - Available Quantity `TINYINT UNSIGNED`
    - The number of copies of the audiobook currently available for borrowing.
  - Total Quantity `TINYINT UNSIGNED`
    - The total number of copies of the audiobook in the library.
  - Genre `VARCHAR(100)`
    - The genre of the audiobook, with a limit of 100 characters.

- ****Magazine****
  
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
  - Available Quantity `TINYINT UNSIGNED`
    - The number of copies of the magazine currently available for borrowing.
  - Total Quantity `TINYINT UNSIGNED`
    - The total number of copies of the magazine in the library.

- ****Digital Disk****
  
  - ISSN `CHAR(13)` `Primary Key`
    - An identifier with exactly 13 characters used to uniquely identify a digital disk.
  - Title `VARCHAR(255)`
    - A title with a limit of 255 characters representing the digital disk's name.
  - Creator `VARCHAR(255)`
    - A creator's name with a limit of 255 characters, indicating who produced or developed the digital disk content.
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
  - Available Quantity `TINYINT UNSIGNED`
    - The number of copies of the digital disk currently available for borrowing.
  - Total Quantity `TINYINT UNSIGNED`
    - The total number of copies of the digital disk in the library.

- ****Author****
  
  - ID `INT UNSIGNED` `Primary Key`
    - A unique identifier for each author.
  - First Name `VARCHAR(255)`
    - The author's first name with a limit of 255 characters.
  - Middle Name `VARCHAR(255)`
    - The author's middle name with a limit of 255 characters (optional).
  - Last Name `VARCHAR(255)`
    - The author's last name with a limit of 255 characters.

- ****Member****
  
  - ID `INT UNSIGNED` `Primary Key`
    - A unique identifier for each library member.

### Relationships

- Written (Book, eBook, Audiobook, Magazine) many-to-many (Authors)
- Borrow (Member) zero-to-five (Book, eBook, Audiobook, Tool, Wi-Fi hotspot)
- Room can be reserved by one-to-one Members
- One 3D printer can be reserved by one Member
- One Tool can be reserved by one Member
- One Hotspot can be reserved by one Member

---

## ER Diagram

Diagram can be found [here](https://github.com/mbiundo23/EECS-447-Group-project/blob/main/Eecs447_Project_ERDiagram.drawio.pdf).

---

## Appendices

The entities and relationships are not final as we are still disccusing the possibility of exploring generalization for media based entities such as books, ebooks, audio books magazines, and disks belonging to a generalized entity. Another topic we discussed is the possibility of using an Author ID/Publisher ID as a foreign key to media based entities. Additionally, for room reservations, we discussed the possibility of adding a time block as a composite attribute that holds both the date and time. 
