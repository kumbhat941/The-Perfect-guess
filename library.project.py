class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("The available books are : ")
        for book in self.books:
            print(" *" +book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} book.Please return it before 30 days.")             
            self.books.remove(bookName)
            return True
        else:
             print(f"Sorry,{bookName} is either not available or already has been borrowed")       
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thanks for using Central Library, hope you enjoyed reading {bookName}.")

class student:
    def requestBook(self):
        self.book = input("Enter the name of the book, which you want to borrow : ")
        return self.book
        

    def returnBook(self):
        self.book = input("Enter the name of the book, which you want to return : ")   
        return self.book

if __name__=="__main__":
    centralLibrary = Library(["Physics", "Math", "Grammar", "Chemistry", "Philosophy"])        
    student = student()
    while True:
        welcomeMsg = '''\n ****Herzlich Willkommen in der Zentral Bibliothek****
        Please choose an option:
        1. List all books 
        2. Request a book 
        3. Add/return a book 
        4. Exit the Library  
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")