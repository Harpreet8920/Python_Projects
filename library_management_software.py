class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showinfo(self):
        print(f"The library has {self.nobooks} books. The books are :-  ")
        for book in self.books:
            print(book)


l1 = Library()

no = int(input("Enter the number of books  = "))
for i in range(no):
    name = input("Enter the name of the book = ")
    l1.books.append(name)
l1.nobooks = len(l1.books)
l1.showinfo()
print("List of Books are = ", l1.books)
