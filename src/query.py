### Luokka, joka vuorovaikuttaa käyttäjän kanssa ja kerää syötteet. Ei validoi.
class Query:

    def __init__(self, actions):
        self.actions = actions

    def welcome(self):
        print("Welcome user, \n")

    def ask_action(self, actions):
        query = f"What would you like to do?\n {self.actions}\n"
        action = input(query)

        if action not in self.actions:
            print("Unknown action")
            return False
        return action

    def action_add(self):
        data = []

        data.append(input("Reference Type: "))
        data.append(input("Key: "))
        data.append(input("Author: "))
        data.append(input("Title: "))
        data.append(input("Publication Year: "))

        return data