# program_files
# SINGLY LINKED LIST 
Scenario-Based Implementation :
Question 1: Build a Music Playlist Manager Scenario You are developing a music player application for a college cultural fest. The application maintains the user's current playlist in the order in which songs will be played. Since songs may be added or removed frequently, the development team has decided to represent the playlist using a Singly Linked List. Each node represents one song. The node should contain only a data field for the song name and a next field pointing to the next song. Your Task Develop a menu-driven Python program that allows the user to manage the playlist using a Singly Linked List. 
The user should be able to perform the following operations:
1. Add a song to the beginning of the playlist
2. 2. Add a song to the end of the playlist
3. Insert a song at a specified position
4. Remove the first song from the playlist
5. Remove the last song from the playlist
6. Remove the song at a specified position
7. Search for a song and display its position
8. Display the total number of songs
9. Display the complete playlist
10. Reverse the playlist order
11. Exit the application
Scenario Example When the application starts, the playlist is empty. The user performs the following actions: Add at end: Believer Add at end: Perfect Add at beginning: Havana Insert at position 3: Faded The playlist should now be: Havana → Believer → Faded → Perfect → None If the user searches for Faded, the program should report that it is at position 3. If the user then removes the song at position 2, the playlist becomes: Havana → Faded → Perfect → None
Special Cases to Handle
• Trying to delete from an empty playlist.
• Trying to delete or insert at an invalid position.
• Adding the first song when the playlist is empty.
• Deleting the only song in the playlist.
• Searching for a song that does not exist.
Implementation Rules
• Use a Singly Linked List. Do not use Python's built-in list to store songs.
• Each node must contain only data and next.
• Do not use another data structure to maintain the playlist.
• All operations must be implemented using linked-list traversal and pointer manipulation.
• Use match-case for the menu.
• Positions are 1-based. Singly Linked List – Scenario-Based Implementation | 

Scenario-Based Implementation 
Question 2: Build a Student Record Manager Scenario A college department currently maintains student records manually. The department wants a simple console-based system that can maintain students in the order in which they are registered for a departmental event. You have been asked to implement the system using a Singly Linked List. Each node represents one student and stores the student's ID, name, marks, and next reference. Your Task Develop a menu-driven Python application that manages the student records using a Singly Linked List. 
The application must support the following operations:
1. Register a student at the beginning
2. Register a student at the end
3. Register a student at a specified position
4. Remove a student using the Student ID
5. Search for a student using the Student ID
6. Display all registered students
7. Display the total number of registered students
8. Find and display the student who has the highest marks
9. Reverse the registration order
10. Exit the application
Scenario Example Suppose the following students are registered: 101 → Arun → 78 102 → Priya → 92 103 → Rahul → 85 A new student, Karthik (ID 104, marks 88), registers at position 2. The list should become: 101 → Arun → 78 104 → Karthik → 88 102 → Priya → 92 103 → Rahul → 85 If the department searches for Student ID 102, the program should display the student's details and position in the list. If the department asks for the student with the highest marks, the program should identify Priya with 92 marks. If Student ID 104 is deleted, the linked list should reconnect the surrounding nodes correctly.
Special Cases to Handle
• Trying to operate on an empty student list.
• Registering the first student.
• Deleting the only student.
• Searching for a Student ID that does not exist.
• Deleting a Student ID that does not exist.
• Inserting at an invalid position.
• Handling students with the same marks.
Implementation Rules
• Use a Singly Linked List instead of Python's built-in list.
• Do not use dictionaries, sets, arrays, or other data structures to store the student records.
• Each node should store the student information and a next reference.
• All operations must use linked-list traversal and pointer manipulation.
• Use match-case for the menu.
• Student IDs should be unique.
• Positions are 1-based.
