.PHONY: build

PXX=python3

download:
	#wget http://geodata.gov.gr/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/d94179a0-a2bd-432f-8c5e-e05eae2886cf/download/googletransit.zip -P temp
	#unzip -o googletransit.zip -d source/data
	#rm temp/*.zip*
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/e2d3bcba-8e10-40fa-ae13-48b995282318/download/agency.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/f2ecf841-d064-4e2c-b03b-c995cef7ab4a/download/calendardates.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/07144eae-6a5d-4862-8861-686765dfcb4c/download/calendar.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/66ebe575-3327-4cb4-8ecf-4813d3b534b2/download/feedinfo.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/982a6e65-4f41-4b76-b1a7-c02d3b80b94a/download/routes.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/4a3206e1-9434-49ef-97c3-c85df2487456/download/shapes.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/ccbe71dc-35a8-4643-a563-84ae4fc52f18/download/stoptimes.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/420c6996-6714-4d85-96bb-ed85fd721c9c/download/stops.txt -P source/data
	wget http://geodata.gov.gr/el/dataset/244cfb87-21a0-4f9f-90af-25e9a232af41/resource/f59908e0-fda5-4914-818f-ae427a97ce73/download/trips.txt  -P source/data

clear:
	rm temp/*

source/scripts/routes-basic.py:
	python3 source/scripts/routes-basic.py

source/scripts/stops-basic: 
	python3 source/scripts/stops-basic.py

build: source/scripts/routes-basic.py source/scripts/stops-basic.py
	#python3 setup.py
