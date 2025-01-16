import json


class MovieLibrary:

    class MovieNotFoundError(Exception):
        """
        Exception raised when a movie is not found in the collection.
        """
        def __init__(self, message="Movie was not found"):
            self.message = message
            super().__init__(self.message)

    def __init__(self, json_file):

        """
        Initialize the MovieLibrary instance.
        :param json_file: Absolute path to the movies.json file.
        """
        self.json_file = json_file
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.json_file}")

    def _save_to_file(self):
        """
        Save the current state of the movies collection to the JSON file.
        """
        try:
            with open(self.json_file, 'w', encoding='utf-8') as file:
                json.dump(self.movies, file, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.json_file}")

    def get_movies(self):
        """
        Retrieve the entire collection of movies.
        :return: List of all movies in the collection.
        """
        return self.movies

    def add_movie(self, title, director, year, genres):
        """
        Add a new movie to the collection.
        :param title: Title of the movie.
        :param director: Director of the movie.
        :param year: Year of the movie.
        :param genres: List of genres for the movie.
        """
        new_movie = {
            'title': title,
            'director': director,
            'year': year,
            'genres': genres
        }
        self.movies.append(new_movie)
        try:
            self._save_to_file()
            print(f"Movie '{title}' added successfully.")
            return True
        finally:
            return False

    def remove_movie(self, title):
        """
        Remove a movie from the collection.
        :param title: Title of the movie to be removed.
        """
        for movie in self.movies:
            if movie['title'] == title:
                self.movies.remove(movie)
                self._save_to_file()
                print(f"Movie '{title}' removed successfully.")
                return True
            else:
                print(f"Movie '{title}' not removed.")
                return False
        raise self.MovieNotFoundError()

    def update_movie(self, title, director=None, year=None, genres=None):
        """
        Update an existing movie in the collection.
        :param title: Title of the movie to be updated.
        :param director: New director of the movie.
        :param year: New year of the movie.
        :param genres: New list of genres for the movie.
        """
        for movie in self.movies:
            if movie['title'] == title:
                if director:
                    movie['director'] = director
                if year:
                    movie['year'] = year
                if genres:
                    movie['genres'] = genres
                self._save_to_file()
                print(f"Movie '{title}' updated successfully.")
                return movie
        raise self.MovieNotFoundError()

    def get_movie_titles(self):
        """
        Retrieve a list of all movie titles in the collection.
        :return: List of all movie titles.
        """
        return [movie['title'] for movie in self.movies]

    def count_movies(self):
        """
        Count the number of movies in the collection.
        :return: Number of movies in the collection.
        """
        return len(self.movies)

    def get_movie_by_title(self, title):
        """
        Retrieve a movie by its title.
        :param title: Title of the movie to retrieve.
        :return: Movie with the specified title.
        """
        for movie in self.movies:
            if movie[title] == title:
                return movie
        print(f"'{title}' not found in the movie list.")

    def get_movies_by_title_substring(self, substring):
        """
        Retrieve a list of movies whose title contains the specified substring.
        :param substring: Substring to search for in movie titles.
        """
        result = []
        for movie in self.movies:
            if substring in movie['title']:
                result.append(movie)
        return result

    def get_movies_by_year(self, year):
        """
        Retrieve a list of movies released in the specified year.
        :param year: Year to search for in movie release years.
        """
        result = []
        for movie in self.movies:
            if self.year == year:
                result.append(year)
        return result

    def count_movies_by_director(self, director):
        """
        Retrieve the number of movies directed by the specified director.
        :param director: Director to search for in movie directors.
        """
        total = 0
        for movie in self.movies:
            if self.director == director:
                total += 1
        return total

    def get_movie_by_genre(self, genre):
        """
        Retrieve a list of movies with the specified genre.
        :param genre: Genre to search for in movie
        """
        result = []
        for movie in self.movies:
            if genre in movie['genres']:
                result.append(movie)
        return result

    def get_oldest_movie_title(self):
        """
        Retrieve the title of the oldest movie in the collection.
        """
        oldest = None
        for movie in self.movies:
            if not oldest or movie['year'] < oldest['year']:
                oldest = movie

    def get_average_release_year(self):
        """
        Calculate the average release year of all movies in the collection.
        """
        total = 0
        for movie in self.movies:
            total += movie['year']
        return total / len(self.movies)

    def get_longest_title(self):
        """
        Retrieve the title of the movie with the longest title.
        """
        longest = None
        for movie in self.movies:
            if not longest or len(movie['title']) > len(longest['title']):
                longest = movie
        return longest['title']

    def get_titles_between_years(self, start_year, end_year):
        """
        Retrieve a list of movie titles released between the specified years.
        :param start_year: Start year of the range.
        :param end_year: End year of the range.
        """
        result = []
        for movie in self.movies:
            if start_year <= movie['year'] <= end_year:
                result.append(movie['title'])
        return result

    def get_most_common_year(self):
        """
        Retrieve the most common year among all movies in the collection.
        """
        years = {}
        for movie in self.movies:
            if movie['year'] in years:
                years[movie['year']] += 1
            else:
                years[movie['year']] = 1
        most_common_year = None
        most_common_year_count = 0
        for year, count in years.items():
            if count > most_common_year_count:
                most_common_year = year
                most_common_year_count = count
        return most_common_year
