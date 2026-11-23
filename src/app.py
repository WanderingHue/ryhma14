from query import Query


def main():
    actions = ["add", "remove", "edit", "list", "export"]

    query = Query(actions)
    query.welcome()

    action = query.ask_action(actions)

    if action == "add":
        print(query.action_add())



main()