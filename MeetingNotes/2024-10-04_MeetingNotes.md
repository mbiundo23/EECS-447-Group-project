# MEETING NOTES

## Meeting Information

**Date**: 2024-10-04 @ 06:00 pm (virtual via Discord)

**Purpose**: Discuss General Project Info and discuss Project Part 2

**Attendence**: Andrew Vander, Max Biundo, Samuel Buehler, Karsten Wolter, Mario Simental (12 min. late), Humza Qureshi (17 min. late)

## Meeting Contents

Went over Project Part 2, began outlining it. The following is what we contributed to Project Part 2 today.

**Note**: This is not the finalized version of Project Part 2, only a record of what we contributed to it during this meeting specifically.

### Project Part 2 Contribution

#### Introduction

This project should cover the borrowing aspect of a small library's functionality. The purpose of the database is to track the media items in the library; Who has a given item checked out, is it available still, etc. This is not related to higher-level administration (budgeting, payroll, etc.).

#### Stakeholders

Customers, Admin people like Librarians. Possibly city and city members; tax payers, schools (administrators, teachers, students)

#### Requirements

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

#### Functional Requirements

- Should be able to see the library

- Enter new books/items

- Delete books no longer available

- Data Entry

- Generate Reports

- Reservations (books, other media, rooms, tools, computers)

#### Non-Functional Requirements (Optional)

* Security (level of access to the database; (ex: Password protection)

* Performance Metrics

#### User Requirements

* Views:
  
  - Librarian administration (middle-view)
  
  - General view (for end-users)
    
    - Current and Past checkouts
    
    - Check current media availabilities

#### Hardware and Software Requirements

* Regular SQLite

* Cross-platform (Linux, MacOS, Windows)

### Meeting Continuation

* We had an extensive discussion over the platform and framework we'd use for this project, and how Operating System comes in to play with that.

* We discussed that we may continue working on Project Part 2 next week during our meeting.

* Max had to leave at 7:00 pm. Andrew left shortly after, and the meeting officially ended.
