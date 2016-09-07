

class MovieInfo(object):
	def __init__(self, director, release_year, title, actor_1 = "",actor_2 = "",location = ""):
		self.director = director
		self.release_year = release_year 
		self.title = title
		self.actor_1 = actor_1
		self.actor_2 = actor_2
		self.location = location




if __name__ == '__main__':
	movie_1 = Movieinfos("Jasmin", "2001", "Fun at Yelp", "Meryl Streep", "Justin Timberlake", "San Francisco")
	print movie_1.__dict__
