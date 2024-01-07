from db import db
from models import Users, Movies


def add_movies():
    """
    This function is a stopgap until I add a remote postgresql instance. This just fills in the
    create sqllite db with movie values. Right now, this is hardcoded.
    """
    movies = {
        "movie1": {
            "title": "Le Voyage Dans La Lune (A Trip to the Moon)",
            "url": "https://shittynetflix-movies.s3.amazonaws.com/Le_Voyage_dans_la_Lune.mp4",
            "image_url": "/images/a_trip_to_the_moon.jpeg",
            "description": "George Melies's `A Trip to the Moon' welcomes a change in film making of the twentieth century. Combined with live action as well as models, the movie tells a story about astronauts who take a trip to the moon. The moon, having a human face captures the astronauts after they crash into its eye. They later escape the moon and it's moon-men and make it back to earth safely. Melies wrote, directed and starred in this movie. He used many important techniques in his films to make them successful. Not only did he develop editing skills and superimposed images, he also used double exposure to complete the magic behind his films. Still used today, Melies's special effects, small models, painted backgrounds, weird makeup and costumes were just some of the important things used in the movie `A Trip to the Moon.' ",
        },
        "movie2": {
            "title": "Night of the Living Dead",
            "url": "https://shittynetflix-movies.s3.amazonaws.com/night_of_the_living_dead.mp4",
            "image_url": "/images/night_of_the_living_dead.jpeg",
            "description": "In this classic yet still creepy horror film, strangers hold up in a rural Pennsylvania farmhouse and battle constant attacks from dead locals who have been brought back to life by mysterious radiation. Note: This item contains a user-contributed srt subtitle file. To use this file you must download an srt compatible player and point it at the correct video and srt files (google for srt subtitles). We include this file for advanced users who may wish to use it, however the Archive does not support any player that displays subtitles stored external to the video they are intended to be used with, nor can we vouch for the quality or completeness of the subtitling effort.",
        },
        "movie3": {
            "title": "The Cabinet of Dr. Caligari",
            "url": "https://shittynetflix-movies.s3.amazonaws.com/The_Cabinet_of_Dr._Caligari.mp4",
            "image_url": "",
            "description": "The Cabinet of Dr. Caligari is the first modern Horror Film and it influence a number of contemporary productions. A real classic! PLOT: A man named Francis relates a story about his best friend Alan and his fiancée Jane. Alan takes him to a fair where they meet Dr. Caligari, who exhibits a somnambulist, Cesare, that can predict the future. When Alan asks how long he has to live, Cesare says he has until dawn. The prophecy comes to pass, as Alan is murdered, and Cesare is a prime suspect. Cesare creeps into Jane's bedroom and abducts her, running from the townspeople and finally dying of exhaustion. Meanwhile, the police discover a dummy in Cesare's cabinet, while Caligari flees. Francis tracks Caligari to a mental asylum. He is the director! Or is he?",
        },
    }

    for movie_id, movie in movies.items():
        new_movie = Movies(
            title=movie["title"],
            url=movie["url"],
            image_url=movie["image_url"],
            description=movie["description"],
        )
        db.session.add(new_movie)
        db.session.commit()
