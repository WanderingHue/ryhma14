from query import Query
from viite import Viite


def main():
    actions = ["add", "remove", "edit", "list", "export"]
    viite = None

    query = Query(actions)
    query.welcome()
    action = query.ask_action(actions)
    if action == "add":
        data = query.action_add()
        viite = Viite(data[0], data[1], data[2], data[3], data[4])
        viite.print()

main()