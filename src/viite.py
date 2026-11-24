class Viite:

    def __init__(self, type, key, author, title, year):
        self.type = type
        self.key = key
        self.author = author
        self.title = title
        self.year = year

    def print(self):
        print(f"{self.type}, {self.key}, {self.author}, {self.title}, {self.year}")