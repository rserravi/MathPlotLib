import json
import urllib.request
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#explore data structure

with urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson") as url:
    original_data = json.load(url)
    tm_dicc = original_data['features']

    mags = []
    lons, lats = [], []
    hover_texts = []
    for entry in tm_dicc: 
        mag = entry['properties']['mag']
        lon = entry['geometry']['coordinates'][0]
        lat = entry['geometry']['coordinates'][1]
        hover = entry['properties']['title']
        if mag >=0:
            mags.append(mag)
        else:
            mags.append(0)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(hover)

# Building the map
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Today Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')



