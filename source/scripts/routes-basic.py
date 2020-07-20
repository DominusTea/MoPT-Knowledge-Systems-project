'''
This script produces the  Ntriples containing basic information about
the (GTFS) route data class.
routes information should be in source/data/routes.txt
output file routes-basic.(??) will be placed in source/Abox
'''

from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF , XSD
import os.path


if __name__ == '__main__':


    #MoPT = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")
    MoPT = Namespace("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#")
    route_long_name = MoPT.route_long #URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#route_long")
    print(type(MoPT))
    # Create  RDF URI nodes for every route type to use as the subject for multiple triples

    routes = MoPT.routes
    aerialLift_route = MoPT.aerialLift_route
    bus_route = MoPT.bus_route
    cableTram_route = MoPT.cableTram_route
    ferry_route = MoPT.ferry_route
    funicular_route = MoPT.funicular_route
    metro_route = MoPT.metro_route
    monorail_route = MoPT.monorail_route
    rail_route = MoPT.rail_route
    tram_route = MoPT.tram_route
    trolleyBus_route = MoPT.trolleyBus_route
    #route type list (ordered following GTFS specification)
    routeType_list = [tram_route, metro_route, rail_route, bus_route, \
                    ferry_route, cableTram_route, aerialLift_route, funicular_route, \
                    trolleyBus_route, monorail_route]



    g = Graph() #RDF graph constructor
    #read the data from routes.txt
    f = open(os.path.dirname(__file__) + '/../data/routes.txt')
    #consume first line
    line = f.readline()
    line=f.readline()
    while line:
        #split line and get data
        line = line.split(',')
        route_id = line[0]
        route_short = line[1]
        route_long=line[2][1:len(line[2])-1]
        route_type=line[4]

        #add data to RDF Graph
        #however the data do not follow exactly the GTFS route_type specifications
        #see source/data/dior8wseis.txt

        if route_type == '900':
            route_type_URI = routeType_list[2]
        elif route_type == '800':
            route_type_URI = routeType_list[0]
        elif int(route_type) < 8:
            route_type_URI = routeType_list[int(route_type)]
        else:
            route_type_URI = routeType_list[int(route_type -3)]

        this_URI = URIRef("http://www.semanticweb.org/knowsys_project/ontologies/MoPT#" + route_short)

        g.add((this_URI, RDF.type, route_type_URI))
        g.add((this_URI, route_long_name, Literal(route_long, datatype=XSD.string)))



        #read next line
        line=f.readline()

    #bind namespaces to prefices for more readable  output

    g.bind("MoPT", MoPT)

    #serialzie to file using prefered format
    g.serialize(destination="source/Abox/routes-basic.txt", format="turtle")
