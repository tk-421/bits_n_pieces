import webbrowser

class Movie():

    def __init__(self, movie_title, storyline, poster_image_url, youtube_url):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.youtube_url = youtube_url

    def show_trailer(self):
        webbrowser.open(self.youtube_url)
