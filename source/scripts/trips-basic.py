'''
This script produces the  Ntriples containing basic information about
the (GTFS) trips data class.
Trips information should be in source/data/trips.txt
Output file trips-basic.txt will be placed in source/Abox
'''

from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import  XSD
import os.path


if __name__ == '__main__':

    #true iff trip data correspond to OASA transportation provider
    is_OASA_DATA = True
    if(is_OASA_DATA):
        trip_agency_id=20
    else:
        trip_agency_id=21

    trip_agency_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#agency_"+str(trip_agency_id))

    #MoPT = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")

    #define namespaces and URIs
    MoPT = Namespace("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")
    trips = MoPT.trips #URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#trips")
    trip_direction_URI = MoPT.trip_direction
    trip_headsign_URI = MoPT.trip_headsign
    trip_id_URI = MoPT.trip_id
    trip_service_id_URI = MoPT.trip_service_id
    trip_route_id_URI = MoPT.trip_route_id
    trip_day_URI = MoPT.trip_day
    providesTrip_URI = MoPT.providesTrip
    providedBy_URI = MoPT.providedBy
    hasRoute_URI = MoPT.hasRoute
    hasTrip_URI = MoPT.hasTrip


    #RDF graph constructor
    g = Graph()
    #read the data from trips.txt
    f = open(os.path.dirname(__file__) + '/../data/trips.txt')
    #consume first line
    line = f.readline()
    #read next line
    line=f.readline()
    while line:
        #split line and get data
        line = line.split(',')
        trip_route_id = line[0]
        trip_service_id = line[1]
        trip_id = line[2].split('-')[0]
        trip_headsign = line[3]
        trip_direction = line[4]
        
        if (len(line[1].split('-')) == 4 ):
            trip_day = line[1].split('-')[2]
        else:
            trip_day = line[1].split('-')[2]+'-'+line[1].split('-')[3]
        #get URIRef of corresponding route
        corresponding_route_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#route_" + trip_route_id)


        #add data to RDF Graph

        #name URI for this route using its short name (i.e trip with trip_id 98765 will have
        #URI: http://www.semanticweb.org/knowsys_project/ontologies/MoPT#trip_98765)
        this_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#trip_" + trip_id)

        g.add((this_URI, RDF.type, trips))
        g.add((this_URI, trip_route_id_URI, Literal(trip_route_id, datatype=XSD.string)))
        g.add((this_URI, trip_service_id_URI, Literal(trip_service_id, datatype=XSD.string)))
        g.add((this_URI, trip_id_URI, Literal(trip_id, datatype=XSD.integer)))
        g.add((this_URI, trip_headsign_URI, Literal(trip_headsign, datatype=XSD.string)))
        g.add((this_URI, trip_direction_URI, Literal(trip_direction, datatype=XSD.integer)))
        g.add((this_URI, trip_day_URI, Literal(trip_day, datatype=XSD.string)))
        #data about corresponding agency
        g.add((this_URI, providedBy_URI, trip_agency_URI))
        g.add((trip_agency_URI, providesTrip_URI, this_URI))

        #data about corresponding route
        g.add((this_URI, hasRoute_URI, corresponding_route_URI))
        g.add((corresponding_route_URI, hasTrip_URI, this_URI))

        #read next line
        line=f.readline()

    #bind namespaces to prefices for more readable  output
    g.bind("MoPT", MoPT)
    f.close()
    #serialzie to file using prefered format
    g.serialize(destination="source/Abox/trips-basic.ttl", format="turtle")
    ff = open(os.path.dirname(__file__) + '/../Abox/trips-basic.graph', "w+")
    ff.write("http://localgraph.org/trips-basic")
    ff.close()
