class Viite:

    # aika monta parametria, halutaanko erilliset luokat?
    # tyyppien omat parametrit oletusarvoilla none
    # inproceedings: booktitle
    # article: journal, volume, pages
    # book: publisher
    def __init__(self, type, key, author, title, year, booktitle=None, journal=None, volume=None, pages=None, publisher=None):
        self.type = type
        self.key = key
        self.author = author
        self.title = title
        self.year = year
        self.booktitle = booktitle
        self.journal = journal
        self.volume = volume
        self.pages = pages
        self.publisher = publisher

    # ei vielä osaa printata inproceedings tyyppiä, muutenkin vähän tyhmä toteutus vielä
    def print(self):
        if self.type == "Artikkeli":
            print(f"{self.type}, {self.key}, {self.author}, {self.title}, {self.year}, {self.journal}, {self.volume}, {self.pages}")
        else: 
            if self.type == "Kirja":
                print(f"{self.type}, {self.key}, {self.author}, {self.title}, {self.year}, {self.publisher}")            
            else: # jos tyyppi on "inproceedings".
                print(f"{self.type}, {self.key}, {self.author}, {self.title}, {self.year}, {self.booktitle}")