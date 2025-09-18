from json import *

def main():
    class Libray():
        idbook = 1
        def __init__(self, name, page, year):
            self.name = name
            self.page = page
            self.year = year
            self.idb = Libray.idbook
            Libray.idbook += 1
            

    books = {}
    indificator = 0

    def add_book(name, page, year):
        global indificator
        indificator += 1
        iterbok = indificator
        book = Libray(name, page, year)
        books[f"book{iterbok}"] = [book.name, book.page, book.year]

    add_book("name", 12, 2009)
    add_book("name", 12, 2009)
    add_book("name", 12, 2009)

    for k,v in books.items():
        print(k,v)

