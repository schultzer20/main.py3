def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    if count == 0:
        return 42
    return count


print(count_vowels("SchoOl"))


def hamming(text1, text2):
    hammingdistance = 0
    a = len(text1)
    b = len(text2)
    if a != b:
        return 0
    if a == b:
        for i in range(a):
            if text1[i] != text2[i]:
                hammingdistance += 1
        return hammingdistance


print(hamming("blue", "green"))


class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        color = "Color:"
        var1 = self.color
        fuel_type = "Fuel Type:"
        var2 = self.fuel_type
        doors = "Doors:"
        var3 = str(self.doors)
        return color + var1 + ", " + fuel_type + var2 + ", " + doors + var3


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        color = "Color:"
        var1 = self.color
        fuel_type = "Fuel Type:"
        var2 = self.fuel_type
        passengers = "Passengers:"
        var3 = str(self.passengers)
        return color + var1 + ", " + fuel_type + var2 + ", " + passengers + var3


car1 = Car("green", "gasoline", 4)
print(car1)

bus1 = Bus("red", "diesel", 55)
print(bus1)


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        print(self.name, ",", self.author)


book1 = Book("Dune", "Frank Herbert")
book2 = Book("Harry Potter", "J. K. Rowling")
book3 = Book("City of Bones", "Cassandra Clare")


class BookShelf:
    def add_book_list(self, books):
        self.books = books
        book_list = []
        for i in books:
            if books == books(Book):
                book_list.append(i)
        print(book_list)


#book4 = Book("Dune", "Frank Herbert")
#book5 = Book("Harry Potter", "J. K. Rowling")
#book6 = Book("City of Bones", "Cassandra Clare")
#book7 = 456
#book8 = "hallo"
#books = [book3, book4, book5, book7, book8]
