'''
This script produces the  Ntriples containing basic information about
the stopsOfTrips data class.
Stop information should be in source/data/stops.txt
Trip information should be in source/data/trips.txt
Stop time information should be in source/data/stoptimes.txt
Output file: stops_time.txt will be placed in source/Abox
'''

from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import  XSD
import os.path


if __name__ == '__main__':

    numLines =1739180
    #MoPT = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")

    #define namespaces and URIs
    MoPT = Namespace("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")
    stopsOfTrips = MoPT.stopsOfTrips #URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#stops")
    stop_id_URI = MoPT.stop_id
    trip_id_URI = MoPT.trip_id
    stopOfTrip_arrTime_URI = MoPT.arrival_time
    stopOfTrip_depTime_URI = MoPT.departure_time
    stopOfTrip_seq_URI = MoPT.stopOfTrip_seq
    stopOfTrip_ArrType_URI = MoPT.stopOfTrip_arrivalType
    stopOfTrip_DropType_URI = MoPT.stopOfTrip_dropOffType

    i=2

    #RDF graph constructor
    g = Graph()
    #read the data from stoptimes.txt
    f = open(os.path.dirname(__file__) + '/../data/stoptimes.txt')
    #consume first line
    line = f.readline()
    #read next line
    line=f.readline()
    while line:
        #split line and get data
        line = line.split(',')
        trip_id, arrival_time, departure_time, stop_id, stop_seq, PickupType, DropOffType= line

        #split trip_id and keep unique id (exactly as we do in trips-basic.py)
        trip_id = trip_id.split('-')[0]

        #add data to RDF Graph


        this_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#stopOfTrip_" + stop_id+ '_' + trip_id)

        g.add((this_URI, RDF.type, stopsOfTrips))
        g.add((this_URI, stop_id_URI, Literal(stop_id, datatype=XSD.int)))
        g.add((this_URI, trip_id_URI, Literal(trip_id, datatype=XSD.int)))
        g.add((this_URI, stopOfTrip_arrTime_URI, Literal(arrival_time, datatype=XSD.time)))
        g.add((this_URI, stopOfTrip_depTime_URI, Literal(departure_time, datatype=XSD.time)))
        g.add((this_URI, stopOfTrip_seq_URI, Literal(stop_seq, datatype=XSD.nonNegativeInteger)))
        g.add((this_URI, stopOfTrip_ArrType_URI, Literal(PickupType, datatype=XSD.int)))
        g.add((this_URI, stopOfTrip_DropType_URI, Literal(DropOffType, datatype=XSD.int)))


        #read next line
        i+=1
        line=f.readline()

        #print progress
        if(i%10000==0):
            print("line is ", i, " progress: ", round(i/numLines,3), "%")

    #bind namespaces to prefices for more readable  output
    g.bind("MoPT", MoPT)

    #serialzie to file using prefered format
    g.serialize(destination="source/Abox/stopsOfTrips.txt", format="turtle")
