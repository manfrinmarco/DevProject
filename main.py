from movie_library import MovieLibrary

library = MovieLibrary('movies.json')
library.add_movie(
    'Inception', 'Christopher Nolan', 2010, ['Sci-Fi', 'Thriller']
)
titoli = library.get_movie_titles()
print(titoli)