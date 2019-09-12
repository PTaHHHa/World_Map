import folium
import pandas


def volcanos():
    data = pandas.read_excel("Volcanos.xlsx")
    lat = list(data["Latitude"])
    lon = list(data["Longitude"])
    name = list(data["Elevation (m)"])
    _map(lat, lon, name)


def _map(x1, x2, x3):
    map_img = folium.Map(location=[48, 10], zoom_start=6, tiles="Stamen Terrain")
    fg1 = folium.FeatureGroup(name="Volcanos")
    for latitude, longitude, name in zip(x1, x2, x3):
        fg1.add_child(folium.Marker(location=(latitude, longitude), popup="%sm"% name, icon=folium.Icon("blue")))

    fg2 = folium.FeatureGroup(name="Population")
    fg2.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
                                 style_function=lambda x: {
                                     'fillColor': 'red' if x['properties']['POP2005'] >= 100000000 else 'orange'
                                     if 100000000 >= x['properties']['POP2005'] > 50000000 else 'green'
                                     if x['properties']['POP2005'] < 50000000 else 'black'}))


    map_img.add_child(fg1)
    map_img.add_child(fg2)

    map_img.add_child(folium.LayerControl())
    map_img.save("bruh.html")


def main():
    volcanos()
    #UScities()


if __name__ == '__main__':
    main()
