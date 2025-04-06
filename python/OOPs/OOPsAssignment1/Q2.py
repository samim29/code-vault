'''2.Develop a lython program for managing library resources efficiently. Design a class named `LibraryBook`
with attributes like book name, author, and availability status. Implement methods for borrowing and
returning books while ensuring proper encapsulation of attributes.'''

class LibraryBook:
    def __init__(self, book_name, author, availability):
        self.__book_name=book_name
        self.__author=author
        self.__availability=availability
    
    def get_book_name(self):
       return  self.__book_name
    def get_author(self):
        return self.__author
    def get_availability(self):
        return self.__availability
    
    def set_book_name(self,new_name):
        self.__book_name=new_name
    def set_author(self,new_author):
        self.__author=new_author
    def set_availability(self,new_availability):
        self.__availability=new_availability
    
    def borrow_book(self):
        if self.__availability:
            print(f"{self.__book_name} is borrowed")
            self.set_availability(False)
        else:
            print("Sorry! This book is not available")
    def return_book(self):
        if not self.__availability:
            self.set_availability(True)
            print(f"{self.__book_name} has been returned")

book1 = LibraryBook("Half GirlFriend", "Chetan Baghat", True)
book2 = LibraryBook("Five Point Someone", "Chetan Baghat", True)
book3 = LibraryBook("12th fail", "Anurag Pathak", True)


book1.borrow_book()
book2.borrow_book()
book3.borrow_book()
print()
book1.return_book()
book2.return_book()
book3.return_book()

