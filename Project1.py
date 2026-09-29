import random


movies = [

    
    {"name": "Inception", "genre": "Sci-Fi", "language": "English"},
    {"name": "Interstellar", "genre": "Sci-Fi", "language": "English"},
    {"name": "The Martian", "genre": "Sci-Fi", "language": "English"},

    
    {"name": "3 Idiots", "genre": "Comedy", "language": "Hindi"},
    {"name": "The Hangover", "genre": "Comedy", "language": "English"},
    {"name": "Hera Pheri", "genre": "Comedy", "language": "Hindi"},

    
    {"name": "The Conjuring", "genre": "Horror", "language": "English"},
    {"name": "Bhool Bhulaiyaa", "genre": "Horror", "language": "Hindi"},
    {"name": "Insidious", "genre": "Horror", "language": "English"},

    
    {"name": "Zindagi Na Milegi Dobara", "genre": "Drama", "language": "Hindi"},
    {"name": "Gangs of Wasseypur", "genre": "Drama", "language": "Hindi"},
    {"name": "Gangs of Wasseypur 2", "genre": "Drama", "language": "Hindi"},
    {"name": "Sanju", "genre": "Drama", "language": "Hindi"},

   
    {"name": "Avengers: Endgame", "genre": "Action", "language": "English"},
    {"name": "War", "genre": "Action", "language": "Hindi"},

    
    {"name": "Ajab Prem Ki Ghazab Kahani", "genre": "Rom-Com", "language": "Hindi"},
    {"name": "How to Lose a Guy in 10 Days", "genre": "Rom-Com", "language": "English"}

]



def show_options():

    print("\nAvailable Genres:")

    genres = []

    for movie in movies:

        if movie["genre"] not in genres:
            genres.append(movie["genre"])

    for genre in genres:
        print("-", genre)

    print("\nAvailable Languages:")
    print("- Hindi")
    print("- English")



def collect_preferences():

    participants = []

    while True:

        try:
            number = int(input("\nHow many friends are watching? "))

            if number > 0:
                break

            else:
                print("Please enter at least 1 participant.")

        except ValueError:
            print("Please enter a valid number.")

    for i in range(number):

        print("\n========== FRIEND", i + 1, "==========")

        name = input("Enter your name: ").strip()

        show_options()

        genre = input("\nEnter your preferred genre: ").strip().title()

        language = input("Enter your preferred language: ").strip().title()

        participant = {
            "name": name,
            "genre": genre,
            "language": language
        }

        participants.append(participant)

    return participants


def calculate_scores(participants):

    movie_scores = {}

    for movie in movies:

        score = 0

        for person in participants:

            if movie["genre"] == person["genre"]:
                score += 1

            if movie["language"] == person["language"]:
                score += 1

        movie_scores[movie["name"]] = score

    return movie_scores



def recommend_movies(participants):

    movie_scores = calculate_scores(participants)

    highest_score = max(movie_scores.values())

    recommendations = []

    for movie in movies:

        if movie_scores[movie["name"]] == highest_score:
            recommendations.append(movie)

    print("\n========== MOVIE RECOMMENDATIONS ==========")

    print("\nMovies matching your group's preferences:\n")

    for movie in recommendations:

        print("Movie:", movie["name"])
        print("Genre:", movie["genre"])
        print("Language:", movie["language"])
        print("Score:", movie_scores[movie["name"]])
        print("------------------------------------------")

    return recommendations



def conduct_voting(recommendations, participants):

    votes = {}

    print("\n========== VOTING ROUND ==========")

    print("\nChoose your favourite movie:\n")

    for i, movie in enumerate(recommendations):

        print(i + 1, ".", movie["name"])

    for person in participants:

        print("\n", person["name"], "'s turn to vote.")

        while True:

            try:

                choice = int(input("Enter your chosen movie number: "))

                if 1 <= choice <= len(recommendations):
                    break

                else:
                    print("Please select a valid movie number.")

            except ValueError:
                print("Please enter a number.")

        selected_movie = recommendations[choice - 1]["name"]

        if selected_movie not in votes:
            votes[selected_movie] = 0

        votes[selected_movie] += 1

    

    highest_votes = max(votes.values())

    winners = []

    for movie, vote_count in votes.items():

        if vote_count == highest_votes:
            winners.append(movie)

    print("\n========== VOTING RESULTS ==========")

    for movie, vote_count in votes.items():

        print(movie, ":", vote_count, "votes")

   

    if len(winners) == 1:

        selected_movie = winners[0]

        print("\nThe group has selected:", selected_movie)

    else:

        print("\nThere is a tie between:")

        for movie in winners:
            print("-", movie)

        selected_movie = random.choice(winners)

        print("\nRandom tie-breaker selected:", selected_movie)

    return selected_movie



def movie_night():

    print("\n========================================")
    print("       MOVIE NIGHT DECISION MAKER")
    print("========================================")

    participants = collect_preferences()

    recommendations = recommend_movies(participants)

    selected_movie = conduct_voting(recommendations, participants)

    print("\n========================================")
    print("          FINAL MOVIE SELECTION")
    print("========================================")

    for movie in movies:

        if movie["name"] == selected_movie:

            print("\nMovie:", movie["name"])
            print("Genre:", movie["genre"])
            print("Language:", movie["language"])

    print("\nEnjoy your movie night! 🍿")




while True:

    movie_night()

    again = input(
        "\nWould you like to organize another movie night? (yes/no): "
    )

    if again.strip().lower() != "yes":

        print("\nThank you for using Movie Night Decision Maker!")

        break
    