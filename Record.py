class Node:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, student_id, name, marks):
        nn = Node(student_id, name, marks)

        if self.head is None:
            self.head = nn
            return

        nn.next = self.head
        self.head = nn

    def insert_end(self, student_id, name, marks):
        nn = Node(student_id, name, marks)

        if self.head is None:
            self.head = nn
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = nn

    def id_exists(self, student_id):
        temp = self.head

        while temp is not None:
            if temp.student_id == student_id:
                return True

            temp = temp.next

        return False

    def insert_at_pos(self, pos, student_id, name, marks):
        if pos <= 0:
            print("Invalid position")
            return

        if self.id_exists(student_id):
            print("Student ID already exists")
            return

        if pos == 1:
            self.insert_begin(student_id, name, marks)
            return

        temp = self.head
        i = 1

        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
            return

        nn = Node(student_id, name, marks)
        nn.next = temp.next
        temp.next = nn

    def delete_by_id(self, student_id):
        if self.head is None:
            print("Student list is empty")
            return

        if self.head.student_id == student_id:
            self.head = self.head.next
            print("Student deleted")
            return

        temp = self.head
        prev = None

        while temp is not None and temp.student_id != student_id:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Student ID not found")
            return

        prev.next = temp.next
        print("Student deleted")

    def search(self, student_id):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.student_id == student_id:
                print("Student found")
                print("Student ID:", temp.student_id)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                print("Position:", pos)
                return

            temp = temp.next
            pos += 1

        print("Student ID not found")

    def display(self):
        if self.head is None:
            print("Student list is empty")
            return

        temp = self.head

        while temp is not None:
            print("ID:", temp.student_id,
                  "| Name:", temp.name,
                  "| Marks:", temp.marks)
            temp = temp.next

    def count(self):
        temp = self.head
        c = 0

        while temp is not None:
            c += 1
            temp = temp.next

        return c

    def highest_marks(self):
        if self.head is None:
            print("Student list is empty")
            return

        temp = self.head
        highest = self.head

        while temp is not None:
            if temp.marks > highest.marks:
                highest = temp

            temp = temp.next

        print("Student with highest marks:")
        print("Student ID:", highest.student_id)
        print("Name:", highest.name)
        print("Marks:", highest.marks)


ll = SinglyLinkedList()

while True:
    print("\nSTUDENT RECORD MANAGER")
    print("1. Register student at beginning")
    print("2. Register student at end")
    print("3. Register student at position")
    print("4. Remove student using Student ID")
    print("5. Search student using Student ID")
    print("6. Display all students")
    print("7. Display total number of students")
    print("8. Display student with highest marks")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_id = int(input("Enter Student ID: "))

        if ll.id_exists(student_id):
            print("Student ID already exists")
        else:
            name = input("Enter student name: ")
            marks = float(input("Enter marks: "))
            ll.insert_begin(student_id, name, marks)

    elif choice == 2:
        student_id = int(input("Enter Student ID: "))

        if ll.id_exists(student_id):
            print("Student ID already exists")
        else:
            name = input("Enter student name: ")
            marks = float(input("Enter marks: "))
            ll.insert_end(student_id, name, marks)

    elif choice == 3:
        pos = int(input("Enter position: "))
        student_id = int(input("Enter Student ID: "))
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        ll.insert_at_pos(pos, student_id, name, marks)

    elif choice == 4:
        student_id = int(input("Enter Student ID to delete: "))
        ll.delete_by_id(student_id)

    elif choice == 5:
        student_id = int(input("Enter Student ID to search: "))
        ll.search(student_id)

    elif choice == 6:
        ll.display()

    elif choice == 7:
        print("Total number of students:", ll.count())

    elif choice == 8:
        ll.highest_marks()

    elif choice == 9:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
