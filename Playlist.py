class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, song):
        nn = Node(song)

        if self.head is None:
            self.head = nn
            return

        nn.next = self.head
        self.head = nn

    def insert_end(self, song):
        nn = Node(song)

        if self.head is None:
            self.head = nn
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = nn

    def insert_at_pos(self, pos, song):
        if pos <= 0:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_begin(song)
            return

        temp = self.head
        i = 1

        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
            return

        nn = Node(song)
        nn.next = temp.next
        temp.next = nn

    def delete_begin(self):
        if self.head is None:
            print("Playlist is empty")
            return

        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Playlist is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        prev = None

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None

    def delete_at_pos(self, pos):
        if pos <= 0:
            print("Invalid position")
            return

        if self.head is None:
            print("Playlist is empty")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head
        prev = None
        i = 1

        while i < pos and temp is not None:
            prev = temp
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid position")
            return

        prev.next = temp.next

    def search(self, song):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.data == song:
                print("Song found at position:", pos)
                return

            temp = temp.next
            pos += 1

        print("Song not found")

    def count(self):
        temp = self.head
        c = 0

        while temp is not None:
            c += 1
            temp = temp.next

        return c

    def display(self):
        if self.head is None:
            print("Playlist is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

ll = SinglyLinkedList()

while True:
    print("\nMUSIC PLAYLIST MANAGER")
    print("1. Add song at beginning")
    print("2. Add song at end")
    print("3. Insert song at position")
    print("4. Remove first song")
    print("5. Remove last song")
    print("6. Remove song at position")
    print("7. Search for a song")
    print("8. Display total number of songs")
    print("9. Display complete playlist")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        song = input("Enter song name: ")
        ll.insert_begin(song)

    elif choice == 2:
        song = input("Enter song name: ")
        ll.insert_end(song)

    elif choice == 3:
        pos = int(input("Enter position: "))
        song = input("Enter song name: ")
        ll.insert_at_pos(pos, song)

    elif choice == 4:
        ll.delete_begin()

    elif choice == 5:
        ll.delete_end()

    elif choice == 6:
        pos = int(input("Enter position: "))
        ll.delete_at_pos(pos)

    elif choice == 7:
        song = input("Enter song name to search: ")
        ll.search(song)

    elif choice == 8:
        print("Total number of songs:", ll.count())

    elif choice == 9:
        ll.display()

    elif choice == 10:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
