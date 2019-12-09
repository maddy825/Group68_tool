# Group68 Squirrel Tracker
- Group 68, Section 2 
- UNIs: [mh3992, yw3410] 
- [Here is the link to the server](https://tools-255500.appspot.com/sightings/)
## Introduction 
This is an application to track squirrels in the central park. Users can view squirrels' location on map, update, add and view general statistics on this web. 
## Import and export data 
Users can run command line to import and export data. The file path should be specified at the command line after the name of the management command. 

    #import data  
    $ python manage.py import_squirrel_data /path/to/file.csv  
    #export data  
    $ python manage.py export_squirrel_data /path/to/file.csv   
    
## Map 
The map displays the location of the squirrel sightings on an OpenStreets map. 
[Here is the link to the map](https://tools-255500.appspot.com/map/)
## Sightings 
The signtings page shows the data for all the squirrel sightings. On the top of this page, you can click on the buttons "add a new sighting" and "click to see the stats", which will direct you to the pages to add sightings and view general statistics. Also, you can click on the squirrels' id to update the data.
[Here is the link to the sightings page](https://tools-255500.appspot.com/sightings/) 
