#!/usr/bin/python3
"""
Stacks and Queues - 3.6. Animal Shelter
"""
from Node import Node


class LinkedList:
    def __init__(self):
        self.total = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        output = str()
        current_node = self.head
        while current_node is not None:
            output += f'[{current_node}]~>'
            current_node = current_node.next
        return output + 'NULL'

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.total += 1

    def size(self):
        return self.total

    def peekFromStart(self):
        if self.head is None:
            return None
        return self.head.data

    def popFromStart(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.total -= 1
        return data

    def popFromEnd(self):
        if self.tail is None:
            return None
        data = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None

        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.total -= 1
        return data


class Animal:
    def __init__(self, name: str):
        self.id = -1
        self.name = name

    def __gt__(self, i):
        return self.id > i

    def __lt__(self, i):
        return self.id < i

    def __str__(self):
        return f'{self.id}-{self.name}'

    def getId(self):
        return self.id

    def setId(self, i):
        self.id = i


class Cat(Animal):
    def __init__(self, *args, **kwargs):
        # print('Init Cat - ', args, kwargs)
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'CAT {super().__str__()}'


class Dog(Animal):
    def __init__(self, *args, **kwargs):
        # print('Init Dog - ', args, kwargs)
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'DOG {super().__str__()}'


class AnimalQueue:
    def __init__(self):
        self.ID_SEQUENCE = 0
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def __str__(self):
        return f'DOGS  {self.dogs}\nCATS  {self.cats}'

    def enqueue(self, animal: Animal):
        self.ID_SEQUENCE += 1
        animal.setId(self.ID_SEQUENCE)

        if isinstance(animal, Cat):
            self.cats.append(animal)

        if isinstance(animal, Dog):
            self.dogs.append(animal)

    def dequeueAny(self):
        if self.cats.size() == 0:
            return self.dequeueDogs()

        if self.dogs.size() == 0:
            return self.dequeueCats()

        dog = self.dogs.peekFromStart()
        cat = self.cats.peekFromStart()
        if cat.getId() < dog.getId():
            return self.dequeueCats()
        else:
            return self.dequeueDogs()

    def dequeueCats(self):
        return self.cats.popFromStart()

    def dequeueDogs(self):
        return self.dogs.popFromStart()


if __name__ == "__main__":
    q = AnimalQueue()
    d1 = Dog('D100')
    d2 = Dog('D200')
    c1 = Cat('C100')
    d3 = Dog('D300')
    c2 = Cat('C200')
    q.enqueue(d1)
    q.enqueue(d2)
    q.enqueue(c1)
    q.enqueue(d3)
    q.enqueue(c2)

    print(q)
    v = q.dequeueCats()
    print(v)
    v = q.dequeueAny()
    print(v)
    v = q.dequeueDogs()
    print(v)
    print(q)


