# ryhma14

Ohjelma viitteiden hallintaan

[Backlogit](https://docs.google.com/spreadsheets/d/1U37ivyz8P0ueKd8qt5LT_HxdaDD0JnOFDHfKsftNthg/edit?usp=sharing)

## Definition of done
 - Ohjelma ei kaadu asiakkaan edessä,
 - Ohjelmaa on ainakin käyttäjätestattu, sekä on kirjoitettu yksikkötestejä, yksikkötestit automatisoitu,
 - Ohjelman osat integroitu

[![CI](https://github.com/WanderingHue/ryhma14/actions/workflows/main.yml/badge.svg)](https://github.com/WanderingHue/ryhma14/actions/workflows/main.yml)

## Asennus/käyttöohje

1. Asenna [uv](https://docs.astral.sh/uv/)
2. Kloonaa repositorio
3. Asenna riippuvuudet (uv sync)
4. Käynnistä sovellus (uv run python src/app.py)

Kun ohjelma käynnistyy tulee ruudulle tervetuloviesti ja ohjelma kysyy minkä toiminnon haluat suorittaa:

 - "add" lisää viitteen (toimii, listaa annettuihin kenttiin tiedot ja ohjelma tulostaa lisätyn liitteen)
 - "remove" poistaa viitteen (ei vielä toteutettu)
 - "edit" muokkaa viitettä (ei vielä toteutettu)
 - "list" listaa viitteet (ei vielä toteutettu)
 - "export" vie viitteet tiedostoon (ei vielä toteutettu)
 - "exit" poistuu ohjelmasta

