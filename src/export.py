from pathlib import Path
import viite


class Export:

    @staticmethod
    def writeBib(reference):

        content = f"""@{reference.type}{{{reference.name},
    author = {{{reference.author}}},
    title = {{{reference.title}}},
    year = {{{reference.year}}}
}}
"""

        # tässä varmistetaan, että viitetiedosto menee juurihakemistoon,
        # siis tarkkana, jos projektin rakenne muuttuu
        root = Path(__file__).resolve().parent.parent

        filepath = root / "viitetiedosto.bib"

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

viiteolio = viite.Viite("article", "name", "Author", "Title", 2026)

# tiedoston testiajo, poistoon myöhemmin
Export.writeBib(viiteolio)         