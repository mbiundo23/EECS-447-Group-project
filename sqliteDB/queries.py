import sqlite3
connection = sqlite3.connect('library_database.db')
cursor = connection.cursor()

"""
we can create custom reports like


def getMembersBorrows(member_id):
    cursor.execute(IDK THE CODE BUT JOIN MEMBERID ON BORROWLOG AND GET ALL RESOURCEIDS)
    return formatted resources ids

customCommands = {
    'get_borrows_from_member {member_id}': getMembersBorrows(member_id) 
}

i can write a parser which would check terminal input if its a custom command or a query in main.py.
"""