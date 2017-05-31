import movie
import movie_page

toy_story = movie.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://s-media-cache-ak0.pinimg.com/originals/ee/9f/21/ee9f21432dac3689d2d3100d2055f151.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = movie.Movie("Avatar", "A marine on an alien planet",
                    "https://s-media-cache-ak0.pinimg.com/originals/f7/bc/7b/f7bc7b19e7f8555ba0f36aa3f2bc5dcd.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
star_wars = movie.Movie("Star Wars: A New Hope", "A young farmboy gets embroiled in an intergalactic war",
                        "https://s-media-cache-ak0.pinimg.com/originals/38/a9/0d/38a90daee5d85f17c99553da40c051f0.jpg",
                        "https://www.youtube.com/watch?v=sPyp-GVsoOo&feature=youtu.be")
empire_strikes_back = movie.Movie("The Empre Strikes Back", "The Galactic Empire delivers a blow to the Rebel Alliance",
                                "http://posterwire.com/wp-content/uploads/empire_strikes_back_style_a.jpg",
                                "https://www.youtube.com/watch?v=96v4XraJEPI")
return_of_the_jedi = movie.Movie("Return of the Jedi", "The Rebel Alliance faces a desparate battle against the Empire",
                                "http://www.impawards.com/1983/posters/return_of_the_jedi_ver2_xlg.jpg",
                                "https://www.youtube.com/watch?v=5UfA_aKBGMc")
rogue_one = movie.Movie("Rogue One: A Star Wars Story", "A small group of Rebels attempt to steal plans critical to the empire",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")
movies = [toy_story, avatar, star_wars, empire_strikes_back, return_of_the_jedi, rogue_one]
movie_page.open_movies_page(movies)
