from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.email}"

class Member(Person):

    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.member_id = member_id

    def role_info(self):
        return f"Member: {self.name}, ID: {self.member_id}"

    def __str__(self):
        return f"Member {self.member_id}: {self.name}"

class Librarian(Person):

    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id

    def role_info(self):
        return f"Librarian: {self.name}, Employee ID: {self.employee_id}"

    def __str__(self):
        return f"Librarian {self.employee_id}: {self.name}"


class Book:

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self._available = True

    @property
    def available(self):
        return self._available

    def borrow(self):
        if not self._available:
            raise ValueError("Book is already borrowed")
        self._available = False

    def return_book(self):
        self._available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class Loan:

    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.loan_date = date.today()
        self.returned = False

    def return_book(self):
        if self.returned:
            print("Book has already been returned.")
            return

        self.book.return_book()
        self.returned = True

    def __str__(self):
        status = "Returned" if self.returned else "Active"
        return f"{self.book.title} -> {self.member.name} ({status})"


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        if member not in self.members:
            raise ValueError("Member is not registered.")

        if book not in self.books:
            raise ValueError("Book is not in the library.")

        book.borrow()

        loan = Loan(member, book)
        self.loans.append(loan)

        return loan

    def return_book(self, loan):
        loan.return_book()

    def __str__(self):
        return (
            f"Library: {self.name}\n"
            f"Books: {len(self.books)}\n"
            f"Members: {len(self.members)}\n"
            f"Loans: {len(self.loans)}"
        )


library = Library("Kabul University Library")

book1 = Book("978", "Python Programming", "Khaliqyar")
book2 = Book("977", "Object Oriented Programming", "David Brown")

member1 = Member(
    "Aryan",
    "rahimullaharyan2006@gmail.com",
    "M001"
)

librarian1 = Librarian(
    "Ahmad",
    "ahmad@library.com",
    "L001"
)


library.add_book(book1)
library.add_book(book2)
library.add_member(member1)


people = [member1, librarian1]

for person in people:
    print(person.role_info())


print("\n" + str(library))

print("\nBooks:")
for book in library.books:
    print(book)


loan1 = library.borrow_book(member1, book1)

print("\nLoan:")
print(loan1)

print("\nAfter borrowing:")
print(book1)


library.return_book(loan1)

print("\nAfter returning:")
print(book1)