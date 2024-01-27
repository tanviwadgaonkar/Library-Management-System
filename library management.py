#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
class library:
    def __init__(self):
        self.book=[];
    def add_book(self,book):
        self.book.append(book)
        print(f"the title of the book is'{book.title}' and the author is'{book.author}  is added to library") 
    def remove_book(self,book):
        for book in self.book:
            if book.isbn==isbn:
                self.book.remove(book)
                print(f"the title of book'{book.title}'is found")
            else:
                print("book not found");
                
    def search_book(self,book):
        for book in self.book:
            if book.title.lower()==title.lower():
                print(f"the title of book'{book.title}'found")
                break;
            else:
                print("book not found")
    def display_book(self,book):
        if not  self.book:
            print("book not in library")
        else:
            print("book found in library")
            for book in self.book:
                print(f"book with title'{book.title}' found'")
library=library()
while True:
    
    print("library management")
    print("1.add book")
    print("2.remove book")       
    print("3.search book")
    print("4.display book")
    print("5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
            title=input("enter title");
            author=input("enter author name")
            isbn=int(input("enter isbn code"))
            new_book=book(title,author,isbn)
            library.add_book(new_book)
    elif choice==2:
            isbn=int(input("enter the isbn code to be removed"))
            library.remove_book(isbn)
    elif choice==3:
            title=input("enter title of the book to be found")
            library.search_book(title)

    elif choice==4:

            library.display_book(book)
    elif choice==5:
            print("exit");
    else:
            print("invalid choice")

        


# In[ ]:




