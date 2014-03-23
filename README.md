nextbike2json
=============

Dump nextbike (i.a. Warszawskie Veturilo) stations list into json array.

(search tags: veturilo api)

Usage
-----

    wget https://nextbike.net/maps/nextbike-official.xml?city=210 -O veturilo.xml
    python nextbike2json.py veturilo.xml > veturilo.json
