class Vector:
    
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __add__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x + other.x,self.y + other.y)
        
        return Exception("Not Implemented")
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    


class Book:

    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        

class Car:

    _instances = {} 

    def __new__(cls, brand, model, year):
        identifier = (brand, model, year)
        if identifier not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[identifier] = instance
        return cls._instances[identifier]

    def __init__(self, brand, model, year) -> None:
        self.__brand = brand
        self.__model = model
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string.")
        if not value:
            raise ValueError("Brand cannot be empty.")
        self.__brand = value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        if not value:
            raise ValueError("Model cannot be empty")
        self.__model = value

    @property 
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be a integer")
        if value < 1886:
            raise ValueError("Year cannot be before 1886")
        self.__year = value
    

