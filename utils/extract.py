import requests

class Extract:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_movies(self, page):
        url = 'https://api.themoviedb.org/3/discover/movie'
        params = {
            'api_key': self.api_key,
            'page': page
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return [codigo['id'] for codigo in data['results']]
        else:
            print(f"Error: Could not retrieve the list of movies. Status code: {response.status_code}")
            return []

    def get_movie_details(self, movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            'api_key': self.api_key,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            release_year = data['release_date'][:4] if 'release_date' in data else 'N/A'
            return {
                'title': data.get('title', 'N/A'),
                'vote_average': data.get('vote_average', 'N/A'),
                'year': release_year,
                'budget': data.get('budget', 'N/A'),
                'revenue': data.get('revenue', 'N/A'),
                'genres': ", ".join([genre['name'].capitalize() for genre in data.get('genres', [])])
            }
        else:
            print(f"Error: Could not retrieve movie details. Status code: {response.status_code}")
            return {}
