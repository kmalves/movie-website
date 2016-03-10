import fresh_tomatoes
import media
king_speech = media.Movie("The King's Speech",
                        "The story of King George VI of the United Kingdom of Great Britain and Northern Ireland, his impromptu ascension to the throne and the speech therapist who helped the unsure monarch become worthy of it.",
                        'September 6, 2010',
                        'http://t0.gstatic.com/images?q=tbn:ANd9GcSxnFajw-bNDE0E9VXDWL9A7wgX84YPG_A7XXgqMeZZIG6M5u1c',
                        'https://www.youtube.com/watch?v=pzI4D6dyp_o')
million_baby = media.Movie('Million Dollar Baby', 'A determined woman works with a hardened boxing trainer to become a professional.',
                           'December 15, 2004',
                     'http://www.gstatic.com/tv/thumb/movieposters/35226/p35226_p_v7_ae.jpg',
                     'https://www.youtube.com/watch?v=DmYI5-M_foE')
imitation_game = media.Movie('The Imitation Game',
                             'During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians.',
                             'January 7, 2015',
                             'http://t0.gstatic.com/images?q=tbn:ANd9GcQQ5vi9xgRkP0nk5aRn8tcGEGRnOQyM-aAS1ldqfQSi_69V1yfU',
                             'https://www.youtube.com/watch?v=S5CjKEFb-sM')
hangover = media.Movie('The Hangover', 'Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.',
                     'June 5, 2009',
                     'http://www.gstatic.com/tv/thumb/movieposters/192248/p192248_p_v7_aa.jpg',
                     'https://www.youtube.com/watch?v=vhFVZsk3XEs')
inception = media.Movie('Inception', 'A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.',
                     'July 13, 2010',
                     'https://trailers.apple.com/trailers/wb/inception/images/poster-large.jpg?lastmod=1',
                     'https://www.youtube.com/watch?v=66TuSJo4dZM')
sophie_choice = media.Movie("Sophie's Choice", 'A mother has to make a very difficult decision.',
                     'December 8, 1982',       
                     'https://31.media.tumblr.com/6e185068a23c28026b69078d7fa73079/tumblr_inline_n6izy8fGMp1qbcy4m.jpg',
                     'https://www.youtube.com/watch?v=-eiud6lixkE')
movies = [king_speech, million_baby, imitation_game, hangover, inception, sophie_choice]

#Generates an HTML page to display a list of movies (instances listed above of the class Movie contained in media.py)
fresh_tomatoes.open_movies_page(movies)

