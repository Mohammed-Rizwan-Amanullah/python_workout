#exercise 1
def city_country(city, country):
    location = city.title() +", "+ country.title()
    return location

city = input("enter the name of the city")
country = input("enter the name of the country")
location = city_country(city,country)
print(location)
print(city_country(city,country))

#exercise 2
def make_album (artist_name, album_title, no_of_songs = None):
    album = { "artist" : artist_name,
             "title" : album_title}
    if no_of_songs:
        album["songs"] = no_of_songs
    return album

album_1 = make_album(artist_name = "AR RAHMAN", album_title = "99 SONGS")
album_2 = make_album("SANTOSH NARAYANAN", "PETTA", 8)
album_3 = make_album("anirudh", "BIGIL", 5)
print(album_1)
print(album_2)
print(album_3)

#exercise 3
def make_album (artist_name, album_title, no_of_songs = None):
    album = { "artist" : artist_name,
             "title" : album_title}
    if no_of_songs:
        album["songs"] = no_of_songs
    return album

while True:
    print("enter q anytime to exit the loop")
    artist_name = input("Enter the name of the artist")
    if artist_name == "q":
        break
    album_title = input("enter the title of the album")
    if album_title == "q":
        break
    no_of_songs = input("enter the number of songs")
    if no_of_songs == "q":
        break

    album = make_album(artist_name, album_title, no_of_songs)
    print(album)


