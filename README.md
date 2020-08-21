# Knowledge system and Technologies MoPT app
This repository contains the Project required for a passing grade in the Knowledge Systems and Technologies course taken on NTUA ECE school in 2020 (spring semester).  
- The ontology is created using Protege and the database and SPARQL queries are handled by Virtuoso. The ontology is stored in source/Ontologies.   
- The data for the Public means of Transportation is open source and can be found at http://geodata.gov.gr/el/dataset/oasa .  
- The data processing into RDF triplets is done using python's rdflib library (https://rdflib.readthedocs.io/en/stable/ ) . The data is stored in source/Abox.
- The SPARQL queries are stored in source/SPARQL-queries.  

You can download the data and make the RDF triplets by running:  
```
make download  
make Abox
```
Making each RDF triplet class individually must be done by running either:
```
make source/scripts/class_name
```
or
```
python3 source/scripts/class_name
```
from the MoPT_app directory.
