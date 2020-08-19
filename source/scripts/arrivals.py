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
    arrivals = MoPT.arrivals #URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#arrivals")
    arrival_arrTime_URI = MoPT.arrival_time
    arrival_depTime_URI = MoPT.departure_time
    arrival_seq_URI = MoPT.arrival_seq
    arrival_ArrType_URI = MoPT.arrival_arrivalType
    arrival_DropType_URI = MoPT.arrival_dropOffType

    arrivalHasTrip_URI = MoPT.arrivalHasTrip
    arrivalHasStop_URI = MoPT.arrivalHasStop


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

        #find URIs of corresponding trip and stop
        corresp_stop_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#stop_" + stop_id)
        corresp_trip_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#trip_" + trip_id)

        #add data to RDF Graph
        this_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#arrival_" + stop_id+ '_' + trip_id)

        g.add((this_URI, RDF.type, arrivals))
        g.add((this_URI, arrivalHasStop_URI, corresp_stop_URI ))
        g.add((this_URI, arrivalHasTrip_URI, corresp_trip_URI))


        g.add((this_URI, arrival_arrTime_URI, Literal(arrival_time, datatype=XSD.time)))
        g.add((this_URI, arrival_depTime_URI, Literal(departure_time, datatype=XSD.time)))
        g.add((this_URI, arrival_seq_URI, Literal(stop_seq, datatype=XSD.nonNegativeInteger)))
        g.add((this_URI, arrival_ArrType_URI, Literal(PickupType, datatype=XSD.int)))
        g.add((this_URI, arrival_DropType_URI, Literal(DropOffType, datatype=XSD.int)))

        #read next line
        i+=1
        line=f.readline()

        #print progress
        if(i%10000==0):
            print("line is ", i, " progress: ", round(100*i/numLines,3), "%")

    #bind namespaces to prefices for more readable  output
    g.bind("MoPT", MoPT)
    f.close()

    #serialzie to file using prefered format
    print("starting turtle serialization. This will take a long time.")
    g.serialize(destination="source/Abox/arrivals.txt", format="turtle")

    ff = open(os.path.dirname(__file__) + '/../Abox/arrivals.graph', "w+")
    ff.write("http://localgraph.org/arrivals")
    ff.close()
