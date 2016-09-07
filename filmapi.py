from urllib2 import urlopen
from json import load
from movieinfo import MovieInfo

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

film_2002 = []


for film in json_obj:
	if film["release_year"] == "2002":
		if film["title"] not in film_2002:
			film_2002.append(film["title"])
			film_2002.sort()


# def getMovie():
# 	movies = []
# 	for row in movies:
# 		movies.append(getMovie(row))
# 	return movies

def getMovie_info(movies_list):
	movies = []
	for row in movies_list:
		director = row["director"]
		release_year = row["release_year"]
		title = row["title"]
		if "actor_1" in row:
			actor_1 = row["actor_1"]
		if "actor_2" in row:
			actor_2 = row["actor_2"]
		location = None
		if "location" in row:
			location = row["location"]
		movies.append(MovieInfo(director, release_year, title, actor_1,actor_2,location))
	return movies

print getMovie_info(json_obj)