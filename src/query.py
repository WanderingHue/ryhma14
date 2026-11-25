### Luokka, joka vuorovaikuttaa käyttäjän kanssa ja kerää syötteet. Ei validoi.
class Query:

    def __init__(self, actions):
        self.actions = actions


    def welcome(self):
        print("Welcome user, \n")


    def ask_action(self, actions):
        query = f"What would you like to do? {self.actions}\n> "
        action = input(query)

        if action not in self.actions:
            print("Unknown action")
            return False
        return action


    ## Funktio viitteen valintaan
    def action_choose(self, action, ref_list):
        self.action_list(ref_list)
        user_input = input(f"Which would you like to {action}: ")
        return user_input


    ## Funktio lisäämistoiminnolle
    def action_add(self):
        data = []
        print("\nInput required information of the reference...")

        ## Ei kapitalisoida. Voidaan tehdä viitetietojen käsittelystä
        ## case-insensitive.
        data.append(input("Reference Type: "))
        if data[0] == "inproceedings":
            data.append(input("Key: "))
            data.append(input("Author: "))
            data.append(input("Title: "))
            data.append(input("Publication Year: "))
            data.append(input("Booktitle: "))        
        else:
            if data[0] == "book":
                data.append(input("Key: "))
                data.append(input("Author: "))
                data.append(input("Title: "))
                data.append(input("Publication Year: "))
                data.append(input("Publisher: "))
            else:
                data.append(input("Key: "))
                data.append(input("Author: "))
                data.append(input("Title: "))
                data.append(input("Publication Year: "))
                data.append(input("Journal: "))
                data.append(input("Volume: "))
                data.append(input("Pages: "))

        return data


    ## Funktio poistamis toiminnolle
    def action_remove(self, ref_list):
        return self.action_choose("remove", ref_list)


    ## Funktio listaus toiminnolle.
    def action_list(self, ref_list):
        print("-----------------------------------\n")
        # Tulostetaan kukin viite kerrallaan
        i = 1
        for ref in ref_list:
            print(f"{i}|")
            ref.print()
            print("\n")
            i += 1

    ## Funktio editoinnille
    def action_edit(self, ref_list):
        return self.action_choose("edit", ref_list)


    ## Tarkistaa, että vastaus on kokonaisluku.
    ## Jos ei, niin kysyy uutta kokonaislukua
    ## Palauttaa hyväksytyn kokonaisluvun
    def validate_integer(self, user_input, ref_list):

        tmp = user_input
        accepted = tmp.isnumeric(tmp)

        while not accepted:
            tmp = input("Input must be an integer. Type a new answer:\n> ")
            if user_input.isnumeric():
               accepted = True
        return int(tmp)

