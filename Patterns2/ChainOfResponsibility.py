class BookCollection:
    def _init(self, books):
        self.books = books

    def _iter(self):
        return BookIterator(self.books)


class BookIterator:
    def _init(self, books):
        self.books = books
        self.index = 0

    def _next(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration

collection = BookCollection(["1984", "Dune", "Foundation"])
for book in collection:
    print(book)
