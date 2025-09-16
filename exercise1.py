#book class

class book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self. year = year
    def describe(self):
        return f"{self.title}, by {self.author}, {self.year}"
    
book1 = book("mockingbird","smith","2012")
book2 = book("ache", "john", "1993")

print(book1.describe())
print(book2.describe())
