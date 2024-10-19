# EECS 447 - Project Part 2

## Introduction

### Project Overview:

This project should cover the borrowing aspect of a small library's functionality.

### Scope

The purpose of the database is to track the media items in the library; Who has a given item checked out, is it available still, etc. This is not related to higher-level administration (budgeting, payroll, etc.).

### Glossary

- ISBN -- International Standard Book Number. Standardized identification value for commercial books as given by the International ISBN Agency.

- ISSN -- International Standard Serial Number. Standardized eight-digit serial number used to uniquely identify a serial publication, such as a magazine.

## Stakeholders

Customers, administrative people like Librarians.

Initially thought of this, but decided it would be unnecessary: Possibly city and city members; tax payers, schools (administrators, teachers, students).

## Requirements

### Functional Requirements

- Users (Members and Librarians) should be able to view the library's catalogue. This will include viewing all available books, eBooks, audiobooks, rooms available, tools, 3D printers, etc. as well as some of their attributes (Titles, Authors/Creators, Availability, etc.).

- Members should be able to add, remove, and update reservations they have made themselves (for rooms or 3D printers). A given member should not be able to modify any other member's reservations.

- Members should be able to borrow eBooks, as they are accessible online after borrowing.
  
  - Members should also be able to return borrowed eBooks when they are finished with them.

- Librarians should be able to add, remove, and update entries within the catalogue. This will include adding new items, removing items, and editing a given item's individual attributes.

- Librarians should be able to generate reports. This includes a printout of all items in the catalogue, a printout of all current borrowings and reservations, and a printout of all members.

- Librarians should be able to add new borrowing and reservation relations, indicating that a Member has checked out an item or reserved a room/printer.

- Librarians should be able to add or remove Members, as well as view their information (such as type of membership).

### Non-Functional Requirements (Optional)

- Security (level of access to the database; (ex: Password protection)

- Librarians should be able to view performance metrics about the system's usage.

## Data Requirements

### Data Entities

Repeated attributes should be assumed to include the description of that attribute's first instance in the list unless otherwise described.

- Book -- A physical copy of a specific literature.
  
  - Title -- The title of the given literature.
  
  - Author/Creator -- The Author(s) of the literature.
  
  - ISBN -- The standardized identification number for the literature.
  
  - Publication Year -- The year the literature was published.
  
  - Publisher -- The publisher of the literature.
  
  - Page Count -- The number of pages within the literature.
  
  - Availability -- The number of this item available.
  
  - Quantity -- The total number of this item within the library's catalogue.
  
  - Genre -- The category of the literature (Fiction, Non-Fiction, etc.)

- eBook -- A digital copy of a specific literature. Accessible instantly online upon borrowing.
  
  - Title
  
  - Author/Creator
  
  - ISBN
  
  - Publication Year
  
  - Publisher
  
  - Availability
  
  - Quantity
  
  - Genre

- Audiobook -- A digital audio recording of a specific literature being read aloud.
  
  - Title
  
  - Author/Creator
  
  - ISBN
  
  - Publication Year
  
  - Publisher
  
  - Duration -- The duration of the audio file in minutes.
  
  - Availability
  
  - Quantity
  
  - Genre

- Magazine -- A single issue of a periodical publication.
  
  - Title
  
  - Issue Number -- The magazine's numerical place within it's publication's set.
  
  - ISSN -- A standardized identification number for a non-book item.
  
  - Publisher
  
  - Publication Date
    
    - Month
    
    - Year
  
  - Page Count
  
  - Availability Status

- Digital Disk -- Digital media stored on a physical device (CD, DvD, Blu-Ray, etc.).
  
  - Title
  
  - Creator
  
  - ID -- A library-specific identification number.
  
  - Release Year
  
  - Distributor -- The distributor of the media, similar to a book's publisher.
  
  - Availability Status
  
  - Genre
  
  - Disk Type -- The type of physical device the media is stored on. (CDs, DvDs, Blu-Ray, etc.)
  
  - Media Type -- The type of media stored on the device. (Video game, Movie, TV series, etc.)

- Author -- The creator/writer of a one or more media.
  
  - ID

- Name -- A composite name of an individual's first and last name.
  
  - First Name
  
  - Last Name

- Member -- A library-goer who has signed up for a specific membership.
  
  - ID
  
  - Name
    
    - First Name
    
    - Last Name
  
  - Membership Type -- The type/level of membership of a given member. (ex: Regular, Student, Senior). This can come with certain benefits, such as priority when reserving items, rooms, or 3D printers.
  
  - Date Membership Began -- The date that a member signed up for their membership with the library.
    
    - Month
    
    - Day
    
    - Year
  
  - Birthday -- The member's date of birth.
    
    - Month
    
    - Day
    
    - Year

- 3D Printer -- An additive manufacturing device that can construct objects from digital Computer Assisted Design (CAD) model files using filament (usually plastics). These can be rented for a limited duration by members.
  
  - Filament Type -- The type of material that is used by the printer to construct objects.
  
  - Model -- The model of the printer itself.
  
  - ID
  
  - Print Volume -- The maximum volume in cubic centimeters that the 3D printer can print. Also known as a "build volume."
  
  - Availability Status -- Whether the printer is currently reserved or not. [Boolean]

- Wi-Fi Hotspot -- A portable Wi-Fi access point that uses cellular data as an internet connection source.
  
  - Model -- The model of hotspot.
  
  - ID
  
  - Carrier -- The cellular data providor for the device's internet connection.
  
  - Availability Status

- Tool -- A hand or power tool. Various types would be stored, from screwdrivers to power drills.
  
  - Type -- The type of tool. (ex: screwdriver, wrench, power drill, etc.)
  
  - Model
  
  - ID
  
  - Brand -- The brand that made the tool.
  
  - Availability Status

- Room -- Rooms within the library's building, designated for reservation and use by Members for a limited duration.
  
  - ID
  
  - Availability Status
  
  - Capacity -- The maximum capacity of people allowed in the given room.

- Librarian -- A staff member of the library who has full access to the library database, capable of managing the items within it.
  
  - ID
  
  - Name
    
    - First Name
    
    - Last Name

## User Requirements

- Views:
  
  - Librarian administration (middle-view)
    
    - Check book/media information (status, holder, etc.)
    
    - View user account information
  
  - General view (for end-users)
    
    - Current and Past checkouts
    
    - Check current media availabilities

## Hardware and Software Requirements

- Regular SQLite

- Cross-platform (Linux, MacOS, Windows)
