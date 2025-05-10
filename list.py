class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkList:

    def __init__(self):
        self.head = None

    def append(self, data):

        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def getItemByIndex(self, index):
        count = 0
        current = self.head

        while current:
            if index == count:
                print(current.data)
                return
            current = current.next
            count = count + 1

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

    def removeItemAt(self, index):
        current = self.head
        prev = None
        count = 0

        if index == 0:
            if current:
                self.head = current.next
            return

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if not current:
            print("Index out of range.")
            return

        prev.next = current.next


list = linkList()

list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)
print(list.removeItemAt(0))
list.printList()
