#!/usr/bin/python
# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "196min",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

The_Pursuit_of_Happyness = media.Movie("The Pursuit of Happyness",
                                       "177min",
                                       "is a 2006 American biographical drama film based on entrepreneur Chris Gardner's nearly one-year struggle being homeless. Directed by Gabriele Muccino, the film features Will Smith as Gardner, a homeless salesman. Smith's son Jaden Smith co-stars, making his film debut as Gardner's son, Christopher Jr...",
                                       "https://upload.wikimedia.org/wikipedia/pt/1/1e/The_Pursuit_of_Happyness.jpg",
                                       "https://www.youtube.com/watch?v=89Kq8SDyvfg")

The_Silence_of_the_Lambs = media.Movie("The Silence of the Lambs",
                                       "111min",
                                       "he Silence of the Lambs is a 1991 American horror-thriller film directed by Jonathan Demme and starring Jodie Foster, Anthony Hopkins, and Scott Glenn.[3] Adapted by Ted Tally from the 1988 novel of the same name by Thomas Harris, his second to feature the character of Dr. Hannibal Lecter; a brilliant psychiatrist and cannibalistic serial killer, the film was the second adaptation of a Harris novel featuring Lecter, preceded by the Michael Mann-directed Manhunter in 1986. In the film, Clarice Starling, a young U.S. FBI trainee, seeks the advice of the imprisoned Dr. Lecter to apprehend another serial killer, known only as 'Buffalo Bill'.",
                                       "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",
                                       "https://www.youtube.com/watch?v=lQKs169Sl0I")

The_Road = media.Movie("The Road",
                       "111min",
                       "The Road is a 2009 American post-apocalyptic drama film directed by John Hillcoat from a screenplay written by Joe Penhall, based on the Pulitzer Prize-winning 2006 novel of the same name by the American author Cormac McCarthy. Principal photography took place in Pennsylvania, Louisiana, West Virginia, and Oregon. The film stars Viggo Mortensen and Kodi Smit-McPhee as a father and his son in a post-apocalyptic wasteland.The Road received a limited release in North American cinemas from November 25, 2009, and was released in United Kingdom cinemas on January 4, 2010.[3][4] The film received generally positive reviews from critics; the performances of Mortensen and Smit-McPhee garnered praise. It also received numerous nominations, including a BAFTA nomination for Best Cinematography.",
                       "https://upload.wikimedia.org/wikipedia/en/a/a7/The_Road_movie_poster.jpg",
                       "https://www.youtube.com/watch?v=bO8EqMsxOiU")

Get_Out = media.Movie("Get Out",
                      "104min",
                      "Get Out is a 2017 American comedy horror film[2][3][4] written, produced and directed by Jordan Peele, in his directorial debut. The film stars Daniel Kaluuya, Allison Williams, Bradley Whitford, Caleb Landry Jones, Stephen Root and Catherine Keener, and follows a young interracial couple who visit the mysterious estate of the woman's parents.Get Out premiered at Sundance Film Festival on January 24, 2017, and was theatrically released in the United States on February 24 by Universal Pictures.[5] The film received acclaim from critics and has grossed $177 million worldwide, against its $4.5 million budget.",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=DzfpyUB60YY")


A_Dogs_Purpose = media.Movie("A Dog's Purpose",
                             "196min",
                             "A Dog's Purpose is a 2017 American comedy-drama film directed by Lasse Hallström and written by W. Bruce Cameron, Cathryn Michon, Audrey Wells, Maya Forbes and Wally Wolodarsky, based on the 2010 novel of the same name by Cameron. The film stars Britt Robertson, KJ Apa, Juliet Rylance, John Ortiz, Kirby Howell-Baptiste, Peggy Lipton, Dennis Quaid and Josh Gad.The film was subjected to scrutiny after a video from the set was leaked of a dog being forced into running water, then submerged and requiring human rescue. Resulting investigations concluded that the video images were authentic, but had been edited.[4][5] The film is co-production between Amblin Entertainment, Reliance Entertainment, Walden Media, and Pariah Entertainment Group.[6][7] It was released by Universal Pictures on January 27, 2017 and grossed $181 million worldwide.",
                             "https://upload.wikimedia.org/wikipedia/en/b/bf/A_Dog%27s_Purpose_%28film%29.jpg",
                             "https://www.youtube.com/watch?v=1jLOOCADTGs")

movies = [toy_story, A_Dogs_Purpose, The_Pursuit_of_Happyness,
          The_Silence_of_the_Lambs, The_Road, Get_Out]
fresh_tomatoes.open_movies_page(movies)
