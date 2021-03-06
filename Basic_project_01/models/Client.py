
from models.Book import Book
from models.Movie import Movie
from decorators import save_file, only

class Client:
    _clients = []

    def __init__(self, cc, name, email, mobile):
        self.cc = cc
        self.name = name
        self.email = email
        self.mobile = mobile
        self.books_rented = []
        self.movies_rented = []

        @only
        def comprobar(self):
            Client._clients.append(self)

        comprobar(self)
    
    def rent_Book(self, Book : Book):
        Book.rent()
        self.Books_prestados.append(Book)
    
    def rent_Movie(self, Movie : Movie):
        Movie.rent()
        self.Books_prestados.append(Movie)
    
    @save_file
    def save(self):
        return f"{self.name},{self.cc},{self.email},{self.mobile},{self.books_rented},{self.movies_rented}\n"


    @classmethod
    def get_clients(cls):
        return cls._clients
    
    def __str__(self) -> str:
        return f"{self.name},{self.email},{self.mobile}"