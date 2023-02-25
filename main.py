import csv
with open("books.csv",'r',newline = '\n') as readlistofbooks: #opening csv file 
    reader = csv.reader(readlistofbooks,delimiter=",") #reading the data
    csvlist=[]                                        
    for row in reader: #storing the data into a list
        csvlist.append(row)
readlistofbooks.close()
class Book: 
    def __init__(self, title, author): #initialising class Book
        self.title = title
        self.author = author
        self.borrowed = False
    def borrow_book(self): #defining borrowed function for the book
            if not book.borrowed:
                book.borrowed = True
                print(f"Success! Book {book.title} by {book.author} has been borrowed.")
            else:
                print(f"Book {book.title} by {book.author} is already borrowed.")
    def return_book(self): #defining returned function for the book
        if book.borrowed:
            book.borrowed = False
            print(f" Book {book.title} by {book.author} has been returned.")
        else:
            print(f"Book {book.title} by {book.author} is not currently borrowed.")


class Library:
    def __init__(self): #initialising library class
        self.librarylist = [] #creating a list 
        for a in csvlist: #adding data from csv list to library list
            self.librarylist.append(Book(a[0],a[1]))
    def add_book(self, book): #defining add book function to the library
        self.librarylist.append(book)
        print(f"Book '{book.title}' by {book.author} has been added to the library.")

    def list_books(self): #defining list books available function to the library
        print("List of books in the library:")
        if len(self.librarylist) > 0:
            for book in self.librarylist:
                print(f" {book.title} by {book.author}")
        else:
            print("Library is Empty!")



# create library by calling the class
library = Library()

def update_library(btitle,bauthor): #defining an update list function that adds data to csv file
    with open("books.csv",'a',newline='\n') as writelistofbooks: #opening csv file 
        writer = csv.writer(writelistofbooks)
        writer.writerow([btitle,bauthor]) #new data added
    writelistofbooks.close()
print("Hello, Welcome to the most efficient Library Management System!")
print("You can do the following: \n 1. List of Books Available \n 2. Add A book \n 3. Borrow a book \n 4. Return a book")
anss = "Y"
while True: #input validation to ensure programs keep running until user stops it
    if anss in "yY":
        ans = int(input("Enter number: "))
        
        if ans==1: # list books in library
            library.list_books()

        elif ans==2: #adding a book to the library
            btitle = input("Enter title of the book to add: ")
            bauthor = input("Enter author of the book to add: ")
            library.add_book(Book(btitle,bauthor)) #add books to library
            update_library(btitle,bauthor) #update the csv file directly
        elif ans==3: #borrowing a book
            bbtitle = input("Enter title of book to be borrowed: ")
            bbauthor = input("Enter author of the book to be borrowed: ")
            val1=False
            for book in library.librarylist:
                if book.title == bbtitle: #finding the book entered by user
                    val1 = True
                    break
                else:
                    val1 = False
            if val1 == True: #if book found, run borrow book function
                book1 = Book(bbtitle,bbauthor)
                Book.borrow_book(book1)
            else:
                    print("Book isn't in the library, consider adding it!")
        elif ans==4: #returning books 
            brtitle = input("enter title of book to be returned: ")
            brauthor = input("enter author of book to be returned: ")
            val1=False
            for book in library.librarylist: #finding the book entered by user
                if book.title == brtitle:
                    val1 = True
                    break
                else:
                    val1 = False
            if val1 == True: #if book found, run return book function
                book1 = Book(brtitle,brauthor)
                Book.return_book(book1)
            else:
                print("Book isn't in the library, consider adding it!")
        else:
            print("Unknown Case.")
                
    elif anss.lower() == "n":
        print("Exiting Program...")
        break
    else:
        print("Input Invalid")

    anss= input("do you want to continue? enter Y for yes, N for no: ")


