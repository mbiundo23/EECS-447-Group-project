
# EECS 447 - Project Part 3

## Objective

Develop a comprehensive Entity-Relationship (ER) diagram that accurately represents the data requirements and relationships for your database project.

Now that you have documented the requirements of your database project, the next step is to prepare a conceptual model. This model will serve as a blueprint for your database design, capturing the essential entities, relationships, and constraints based on the requirements you have gathered.

---

## Introduction

### Project Overview

*Write a brief paragraph summarizing the purpose and primary functions of your database. This should align with the overall goals and objectives outlined in your requirements document.*

This project should cover the borrowing aspect of a small library's functionality.

### Scope

*Provide a concise paragraph defining the boundaries of your project. Mention what aspects will be covered and what will be excluded, ensuring consistency with your initial project scope.*

The purpose of the database is to track the media items in the library; Who has a given item checked out, is it available still, etc. This is not related to higher-level administration (budgeting, payroll, etc.).

### Glossary

*Create a list of key terms and acronyms used in your project. Define each term clearly to ensure that all stakeholders have a common understanding of the terminology.*

## Review Requirements

Use the requirements document you have already prepared. Ensure that all team members understand the initial data entities, their attributes, and the relationships between them.

---

## Get Ready for ER Modeling

### Identify Entities

*List all the major entities that will be part of your database. This includes the initial entities in the project description, the ones you identified during the requirements engineering, and the additional ones during your team brainstorming.*

### Define Attributes

*For each entity, list its attributes and specify the data types or constraints. For example, the Books entity might have attributes such as ISBN, Title, Author, Genre, Price, and Stock Quantity.*

- ****Book****
  - ISBN `CHAR(13)` `Primary Key`
  - Title `VARCHAR(255)`
  - Author `VARCHAR(255)`
  - Publication Year `YEAR`
  - Publisher `VARCHAR(255)`
  - Page Count `SMALLINT UNSIGNED`
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`
  - Quantity `TINYINT UNSIGNED`
  - Genre `VARCHAR(100)`

- ****eBook****
  - ISBN `CHAR(13)` `Primary Key`
  - Title `VARCHAR(255)`
  - Author `VARCHAR(255)`
  - Publication Year `YEAR`
  - Publisher `VARCHAR(255)`
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`
  - Quantity `TINYINT UNSIGNED`
  - Genre `VARCHAR(100)`

- ****Audiobook****
  - ISBN `CHAR(13)` `Primary Key`
  - Title `VARCHAR(255)`
  - Author `VARCHAR(255)`
  - Publication Year `YEAR`
  - Publisher `VARCHAR(255)`
  - Duration (Seconds) `MEDIUMINT UNSIGNED` 
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`
  - Quantity `TINYINT UNSIGNED`
  - Genre `VARCHAR(100)`

- ****Magazine****
  - ISSN `CHAR(8)` `Primary Key`
  - Title  `VARCHAR(255)`
  - Issue Number `INT UNSIGNED` 
  - Publisher `VARCHAR(255)`
  - Publication Year `YEAR`  
  - Publication Month `TINYINT UNSIGNED`
  - Page Count `SMALLINT UNSIGNED`
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`
  - Quantity `TINYINT UNSIGNED`

- ****Digital Disk****
  - ISSN `CHAR(13)` `Primary Key`
  - Title `VARCHAR(255)`
  - Creator `VARCHAR(255)`
  - Release Year `YEAR`  
  - Distributor `VARCHAR(255)`
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`
  - Genre `VARCHAR(255)`
  - Disk Type  `ENUM('CD', 'DVD', 'VHS', 'Other')`
  - Media Type `ENUM('Video Game', 'Movie', 'Other')`
  - Quantity `TINYINT UNSIGNED`

- ****Author****
  - ID `INT UNSIGNED` `Primary Key`
  - First Name `VARCHAR(255)`
  - Middle Name `VARCHAR(255)`
  - Last Name `VARCHAR(255)`

- ****Member****
  - ID `INT UNSIGNED` `Primary Key`
  - First Name `VARCHAR(255)`
  - Middle Name `VARCHAR(255)`
  - Last Name `VARCHAR(255)`
  - Level of Membership `ENUM('Regular', 'Student, 'Senior')`
  - Date Membership Began `DATE`
  - Birthday `DATE`

- ****3D Printer****
  - ID `INT UNSIGNED` `Primary Key`
  - Filament Type `VARCHAR(255)`
  - Model `VARCHAR(255)`
  - Print Volume `INT UNSIGNED`
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`

- ****Wi-Fi Hotspot****
  - ID `INT UNSIGNED` `Primary Key`
  - Model `VARCHAR(255)`
  - Carrier `VARCHAR(255)`
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`

- ****Tool****
  - ID `INT UNSIGNED` `Primary Key`
  - Type `VARCHAR(255)`
  - Model `VARCHAR(255)`
  - Brand `VARCHAR(255)`
  - Availability Status `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`

- ****Room****
  - ID `INT UNSIGNED` `Primary Key`
  - Availability Status  `ENUM('Available', 'Unavailable', 'Lost', 'On Hold')`
  - Capacity `TINYINT UNSIGNED`
  
- ****Librarian****
  - ID  `INT UNSIGNED` `Primary Key`
  - First Name `VARCHAR(255)`
  - Middle Name `VARCHAR(255)`
  - Last Name `VARCHAR(255)`

### Establish Relationships

*Determine how the entities are related to each other. Define the cardinality (one-to-one, one-to-many, many-to-many) and any constraints. For example, a Book can be written by one or more Authors, and a Sale can include multiple Books.*

- (Book, eBook, Audiobook, Magazine) many-to-many (Authors)

- Member can Borrow/Checked-Out one or more items (Book, eBook, Audiobook, Tool, Wi-Fi hotspot)

- Room can be reserved by one-to-one Members

- 3D printer can be reserved by one Member

---

## Create the ER Diagram

*Use a diagramming tool (such as draw.io, Lucidchart, or any other ER diagram tool) to create your ER diagram. Ensure that your diagram includes:*

- *All identified entities and their attributes*
- *Primary keys for each entity*
- *Relationships between entities with appropriate cardinality in `min..max` format*
- *Any additional constraints or notes that are relevant (but not directly presented in the ER model)*

---

## Validate Your Model

*Review your ER diagram to ensure it accurately reflects the requirements. Check for completeness and consistency. Make sure all entities, attributes, and relationships are clearly represented.*

---

## Appendices

*You are welcome to use appendices to provide additional information, e.g., your design choices, explain why you chose certain entities, how you determined the relationships, and any assumptions you made during the modeling process.*
