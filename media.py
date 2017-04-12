import webbrowser


class Videos():
    """ parent class"""

    def __init__(self, video_title, video_duration, video_storyline):
        """parent class function"""
        self.title = video_title
        self.duration = video_duration
        self.storyline = video_storyline


class Movie(Videos):

    """child class"""

    def __init__(self, video_title, video_duration, video_storyline, poster_image, trailer_youtube):
        """child class function"""
        Videos.__init__(self, video_title, video_duration, video_storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ open webbrowser """
        webbrowser.open(self.trailer_youtube_url)
