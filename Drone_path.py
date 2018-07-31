import pandas as pd
import simplekml

dataset = pd.read_csv('image_list.csv')
kml = simplekml.Kml()

for start,long,lat in zip(dataset['Start(s)'],dataset['Longitude'],dataset['Latitude']):
    kml.newpoint(name='{} sec'.format(start),coords=[(long,lat)])

kml.save('Drone Path.kml')