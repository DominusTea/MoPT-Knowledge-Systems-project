.PHONY: build start_server Abox


#change paths belwoto match local folder system
PXX=python3
VIRT_PATH=../virtuoso-opensource/bin
VIRT_DIR=../virtuoso-opensource
ABOX_PATH=~/Documents/know_sys/project/MoPT_app/source/Abox

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
	$PXX source/scripts/routes-basic.py

source/scripts/stops-basic:
	$PXX source/scripts/stops-basic.py

source/scripts/trips-basic:
	$PXX source/scripts/trips-basic.py

source/scripts/arrivals:
	$PXX source/scripts/arrivals.py

Abox: source/scripts/routes-basic.py source/scripts/stops-basic source/scripts/trips-basic source/scripts/arivals

upload_stops:

	#$(VIRTU_PATH)/isql ld_dir('~/Documents/know_sys/project/MoPT_app/source/Abox', 'stops-basic.txt', 'http://localgraph.org/stops-basic')
	$(VIRT_PATH)/isql rdf_loader_run;
	#$VIRT_PATH/isql checkpoint;

upload_trips:
	#ld_dir('/home/pelopidas/Documents/know_sys/project/MoPT_app/source/Abox', 'trips-basic.ttl', 'http://localgraph.org/trips-basic')   ;




start_server:
	sudo $(VIRT_PATH)/virtuoso-t -fd -c $(VIRT_DIR)/databasevirtuoso.ini.sample


build: MoPT.owl source/Abox/routes-basic.txt source/Abox/stops-basic.txt source/Abox/trips-basic.txt source/Abox/arrivals.txt
	#python3 setup.py
