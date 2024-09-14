class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []
        
    def contracts(self):
        return self._contracts
    
    def books(self):
        return [contract._book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract
    
    def total_royalties(self):
        return sum(contract._royalties for contract in self._contracts)
                
    

class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []

    def contracts(self):
        return self._contracts
    
    def authors(self):
        return  [contract._author for contract in self._contracts]
    

    
#Create a Contract class that has the following properties: author (Author object), book (Book object), date (string), and royalties (int).

class Contract:

    all=[]

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author object")
        if not isinstance(book, Book):
            raise Exception("book must be a Book object")  # Corrected message
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all.append(self)

        

    @property 
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must by an Author Object")
        self._author = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an object of Book")
        self._book = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, target_date):
        # Filter contracts by target_date and return the sorted list of contracts
        return sorted(
            [contract for contract in cls.all if contract._date == target_date],
            key=lambda contract: contract._date
        )



