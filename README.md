nextbike2json
=============

Dump nextbike (i.a. Warszawskie Veturilo) stations list into json array.

(search tags: veturilo api)

Usage
-----

    wget https://www.nextbike.pl/maps/nextbike-official.xml?city=210 -O veturilo.xml
    python nextbike2json.py veturilo.xml > veturilo.json
