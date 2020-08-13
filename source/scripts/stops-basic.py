'''
This script produces the  Ntriples containing basic information about
the (GTFS) stops data class.
Stop information should be in source/data/stops.txt
Output file stops-basic.(txt) will be placed in source/Abox
'''

from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import  XSD
import os.path


if __name__ == '__main__':


    #MoPT = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")

    #define namespaces and URIs
    MoPT = Namespace("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")
    stops = MoPT.stops #URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#stops")
    stop_name_URI = MoPT.stop_name
    stop_address_URI = MoPT.stop_address
    stop_location_URI = MoPT.stop_location

    LinkedGeoData = Namespace("http://www.openlinksw.com/schemas/virtrdf#")

    # Create  RDF URI nodes for every stop type to use as the subject for multiple triples

    station_stop = MoPT.station_stop
    genericNode_stop = MoPT.genericNode_stop
    boardingArea_stop = MoPT.boardingArea_stop
    entranceExit_stop = MoPT.entranceExit_stop
    stopPlatform_stop = MoPT.stopPlatform_stop

    #stop type list (ordered following GTFS specification)
    stopType_list = [stopPlatform_stop, station_stop, entranceExit_stop,\
                    genericNode_stop, boardingArea_stop]

    g = Graph() #RDF graph constructor
    #read the data from stops.txt
    f = open(os.path.dirname(__file__) + '/../data/stops.txt')
    #consume first line
    line = f.readline()
    #read next line
    line=f.readline()
    while line:
        #split line and get data
        line = line.split(',')
        stop_id, _, stop_name, stop_address, stop_lan, stop_lon, stop_type = line

        #add data to RDF Graph

        stop_type_URI = stopType_list[int(stop_type)]


        #name URI for this route using its short name (i.e stop with id 13101 will have
        #URI: http://www.semanticweb.org/knowsys_project/ontologies/MoPT#stop_13101)
        this_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#stop_" + stop_id)

        g.add((this_URI, RDF.type, stop_type_URI))
        g.add((this_URI, stop_name_URI, Literal(stop_name, datatype=XSD.string)))
        g.add((this_URI, stop_address_URI, Literal(stop_address, datatype=XSD.string)))
        g.add((this_URI, stop_location_URI, Literal("POINT(" + stop_lan + ' ' + stop_lon + ")" , datatype=LinkedGeoData.Geometry )))

        #since no Reasoning takes place we also have to assert that this particular stop_type stop is also a stop
        g.add((this_URI, RDF.type, stops))


        #read next line
        line=f.readline()

    #bind namespaces to prefices for more readable  output
    g.bind("MoPT", MoPT)
    g.bind("LinkedGeoData", LinkedGeoData)
    f.close()
    #serialzie to file using prefered format
    g.serialize(destination="source/Abox/stops-basic.txt", format="turtle")
    ff = open(os.path.dirname(__file__) + '/../Abox/stops-basic.graph', "w+")
    ff.write("http://localgraph.org/stops-basic")
    ff.close()
