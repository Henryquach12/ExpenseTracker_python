import random
class Library():
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    num_book = 0
    def __init__(self):
        self.books_store = []
        self.reading_schedule = {}
    def add_book(self, title, author):
        Library.num_book += 1
        book = f"#{Book.num_book} '{title}' by '{author}'"
        self.books_store.append(book)
    def show_book(self):
        print()
        print("--------Available books--------")
        for book in self.books_store:
            print(book)
        print("-------------------------------\n")
    def find_book(self, title, author):
        for book in self.books_store:
            if title in book and author in book:
                print(f"=> '{title}' by '{author}' is found\n")
                return
        print("=> '{title}' by '{author}' is not found.\n")
    def remove_book(self, title, author):
        found = False
        for book in self.books_store:
            if title in book and author in book:
                self.books_store = [books for books in self.books_store if books != book]
                print(f"=> '{title}' by '{author}' is successfully removed\n")
                found = True
        if not found:
            print("=> '{title}' by '{author}' is not found.\n")
    def random_book(self):
        chosen_book = random.choice(self.books_store)
        print(f"The book that you need to read today is {chosen_book}\n")
    def schedule(self, title, author, day):
        if day not in Library.week_days:
            print("Invalid days of week!\n")
            return
        for book in self.books_store:
            if title in book and author in book:
                self.reading_schedule[day] = book 
                print(f"=> '{title}' by '{author}' is scheduled to read on {day}\n")
                return
        print("=> Book not found.\n")
    def show_schedule(self):
        print()
        print("-----------To-read list-----------")
        for day in Library.week_days:
            if day in self.reading_schedule:
                print(f"{day} - {self.reading_schedule[day]}")
        print("--------------------------------\n")        
class main():
    running = True
    library = Library()
    while running:
        print("Welcome to magic library!")
        print("-------------------------")
        print("1) Add new book")
        print("2) Available book")
        print("3) Find book")
        print("4) Remove book")
        print("5) Choose a random book")
        print("6) Schedule your books for the week")
        print("7) Check ur schedule")
        print("8) Exit")
        choice = input("Enter the number(1-8): ").strip()
        if choice == "1":
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            library.add_book(title, author)
            print("=> Book added!")
            print()
        elif choice == "2":
            if not book.books_store:
                print("=> The list of books is empty.\n")
                continue
            library.show_book()
        elif choice == "3":
            if not book.books_store:
                print("=> The list of books is empty.\n")
                continue        
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            library.find_book(title, author)
        elif choice == "4":
            if not book.books_store:
                print("=> The list of books is empty.\n")
                continue
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            library.remove_book(title, author)
        elif choice == "5":
            if not book.books_store:
                print("=> The list of books is empty.\n")
                continue            
            library.random_book()
        elif choice == "6":
            if not book.books_store:
                print("=> The list of books is empty.\n")
                continue
            title = input("Enter the book title: ").strip()
            author = input("Enter the book author: ").strip()
            day = input("Enter the day of the week that you want to read the book: ").strip()
            library.schedule(title, author, day)
        elif choice == "7":
            if not book.books_store:
                print("=> The list of books is empty.\n")
                continue            
            library.show_schedule()        
        elif choice == "8":
            print("Thank you! have a good day!")
            running = False
        else:
            print("=> That's not a valid number.")
            print()
if __name__ == "__main__":
    main()
