from xml.dom import minidom
import sys
import json

if len(sys.argv) < 2:
    print >>sys.stderr, 'usage: python %s data.xml' % sys.argv[0]
    print >>sys.stderr, '\nWarsaw Veturilo: https://nextbike.net/maps/nextbike-official.xml?city=210'
    exit(1)

if sys.argv[1] == '-':
    tree = minidom.parse(sys.stdin)
else:
    tree = minidom.parse(sys.argv[1])
places_list = {}
for place_elm in tree.childNodes[0].getElementsByTagName("place"):
    place = {"lat": place_elm.getAttribute("lat"),
             "lng": place_elm.getAttribute("lng"),
             "name": place_elm.getAttribute("name").strip(),
             "uid": int(place_elm.getAttribute("uid"))}

    places_list[place['uid']] = place

print json.dumps(places_list)
