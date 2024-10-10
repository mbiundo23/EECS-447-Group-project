# EECS 447 - Project Part 2

## Introduction

This project should cover the borrowing aspect of a small library's functionality. The purpose of the database is to track the media items in the library; Who has a given item checked out, is it available still, etc. This is not related to higher-level administration (budgeting, payroll, etc.).

## Stakeholders

Customers, Admin people like Librarians. Possibly city and city members; tax payers, schools (administrators, teachers, students)

## Requirements

- Book and Digital Media (general entity):
  
  - Title
  
  - Author/Creator
  
  - ISBN
  
  - Publication Year
  
  - Publisher
  
  - Availability Status
  
  - Genre

- Magazines
  
  - Title
  
  - Issue Number
  
  - Publication Date
  
  - Availability Status

- User and account numbers on record (membership)
  
  - Library cards
  
  - Different levels of memberships (regular, students, senior)
  
  - Membership ID, name
  
  - Difference between Member and Membership

- Checked-Out Entity (What's checked out, by who, when, etc.)

- ~~Budget*~~

## Functional Requirements

- Should be able to see the library

- Enter new books/items

- Delete books no longer available

- Data Entry

- Generate Reports

- Reservations (books, other media, rooms, tools, computers)

### Non-Functional Requirements (Optional)

- Security (level of access to the database; (ex: Password protection)

- Performance Metrics

## User Requirements

- Views:
  
  - Librarian administration (middle-view)
  
  - General view (for end-users)
    
    - Current and Past checkouts
    
    - Check current media availabilities

## Hardware and Software Requirements

- Regular SQLite

- Cross-platform (Linux, MacOS, Windows)
