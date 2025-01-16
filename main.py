from movie_library import MovieLibrary

library = MovieLibrary('movies.json')

print("All Movies:", library.get_movies())
print()

print("Add New Movie:", library.add_movie(
	"The Prestige", "Christopher Nolan", 2006, ["Drama", "Thriller"]))
print()
try: 
	removed_movie=library.remove_movie("The Matrix") 
	print("Removed Movie:", removed_movie)
except Exception as e: 
	print("Exeption trown:", e)
print()

print("Updated Movie:", library.update_movie(
	"The Prestige", director="Christopher Nolan", year=2006, 
	genres=["Drama", "Thriller", "Mystery"]))
print()

print("Movie Titles:", library.get_movie_titles())
print()

print("Count of Movies:", library.count_movies())
print()

print("Movie by Title (Inception):", library.get_movie_by_title("Inception"))
print()

print("Movies by substring (cep):", library.get_movies_by_title_substring("cep"))
print()

print("Movies by Year (2010):", library.get_movies_by_year(2010))
print()

print("Movies by Director (Christopher Nolan):", 
	  library.count_movies_by_director("Christopher Nolan"))
print()

print("Movies by Genre (Sci-Fi):", library.get_movies_by_genre("Sci-Fi"))
print()

print("Oldest Movie:", library.get_oldest_movie_title())
print()

print("Average Release Year:", library.get_average_release_year())
print()

print("Longest Title:", library.get_longest_title())
print()

print("Titles between 1999 and 2014:", 
	library.get_titles_between_years(1999, 2014))
print()

print("Most Common Year:", library.get_most_common_year())
print()
