from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting
import csv
import datetime
from sightings.models import Sighting

class Command(BaseCommand):
    help = 'Import CSV file'
    
    def add_arguments(self,path):
        path.add_argument('csv_file',nargs='+',type=str)

    def handle(self,*arg,**options):
        path=str(options['csv_file'][0])
        with open(path) as csvfile:
            data=csv.reader(csvfile)
            next(data)
            counter=0
            for row in data:
                for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                    if row[i]=='true':
                        row[i]=True
                    else:
                        row[i]=False
                row[5]=datetime.datetime.strptime(row[5],"%m%d%Y").strftime("%Y-%m-%d")
                sighting=Sighting(longitude=row[0],
                                   latitude=row[1],
                                   squirrel_id=row[2],
                                   shift=row[4],
                                   date=row[5],
                                   age=row[7],
                                   primary_fur_color=row[8],
                                   location=row[12],
                                   specific_location=row[14],
                                   running=row[15],
                                   chasing=row[16],
                                   climbing=row[17],
                                   eating=row[18],
                                   foraging=row[19],
                                   other_activities=row[20],
                                   kuks=row[21],
                                   quaas=row[22],
                                   moans=row[23], 
                                   tail_flags=row[24],
                                   tail_twitches=row[25],
                                   approaches=row[26],
                                   indifferent=row[27],
                                   runs_from=row[28],)

                sighting.save()
