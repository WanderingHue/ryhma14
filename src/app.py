from query import Query
from viite import Viite
from export import Export


def main():
    actions = ["add", "remove", "edit", "list", "export", "exit"]
    ## Kovakoodattu esimerkkilista sprint reviewiä varten.
    examples = [Viite("Kirja", "avain", "Kissa", "Kissan arki", 2014, publisher="Kissa Julkaisija"),
                Viite("Artikkeli", "avain", "Matti Mallikas", "Miten saada opintopisteitä?", 2026, journal="Lehti", volume=2, pages="11-32")]
    viite = None

    # Kyselyolio
    query = Query(actions)
    query.welcome()

    # Export olio
    export = Export()

    while True:
        action = query.ask_action(actions)
        if action == "exit":
            break

        if action == "add":
            data = query.action_add()
            viite = Viite(data[0], data[1], data[2], data[3], data[4])
            examples.append(viite)

        if action == "remove":
            to_remove = query.action_remove(examples)

        if action == "edit":
            to_edit = query.action_edit(examples)

        if action == "list":
            query.action_list(examples)

        if action == "export":
            export.writeBib(Viite("Kirja", "avain", "Kissa", "Kissan arki", 2014))

main()
