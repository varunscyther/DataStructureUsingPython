import itertools
import statistics


def get_highest_rated_movie(list_of_movies, list_of_similar_movies, user_movies_seen_list) :
    global discussability, similar_movies_adjacency_list, similar_movies_adjacency_graph, rating_dic
    discussability = {}
    rating_dic = {}
    similar_movies_adjacency_graph = [[0 for i in range(len(list_of_movies))] for j in range(len(list_of_movies))]

    for movie in list_of_movies :
        create_discussability_dataset(movie, user_movies_seen_list)

    create_similar_movies_adjacency_matrix_dataset(list_of_similar_movies, list_of_movies)
    return calculate_highest_discussability_uniqueness(list_of_movies)


def create_discussability_dataset(movie, user_movies_seen_list) :
    discussability[movie] = 0
    for seen_movie in user_movies_seen_list :
        if seen_movie == movie :
            discussability[movie] += 1


def create_similar_movies_adjacency_matrix_dataset(list_of_similar_movies, list_of_movies) :
    for similar_movies_list in list_of_similar_movies :
        e_from, e_to = list(similar_movies_list)
        similar_movies_adjacency_graph[list_of_movies.index(e_from)][list_of_movies.index(e_to)] = discussability[e_to]
        similar_movies_adjacency_graph[list_of_movies.index(e_to)][list_of_movies.index(e_from)] = discussability[
            e_from]


def calculate_highest_discussability_uniqueness(list_of_movies) :
    for i, e in enumerate(similar_movies_adjacency_graph) :
        number_list = []
        for y, x in enumerate(e) :
            if x != 0 :
                number_list.append(x)
        if number_list :
            rating_dic[list_of_movies[i]] = discussability[list_of_movies[i]] / statistics.mean(number_list)
        else :
            rating_dic[list_of_movies[i]] = 0
    return list(dict(sorted(rating_dic.items(), key=lambda item: item[1], reverse=True)).keys())[0]


def create_movies_dataset() :
    movies_list = ["Parasite", "1917", "Ford F Ferrari", "JoJo Rabbit", "Joker"]
    return movies_list


def create_similar_movies_dataset() :
    similar_movies_list = [["Parasite", "1917"],
                           ["Parasite", "JoJo Rabbit"],
                           ["Joker", "Ford F Ferrari"]]
    return similar_movies_list


def create_user_data() :
    user_list = [["Joker"],
                 ["Joker", "1917"],
                 ["Joker"],
                 ["Parasite"],
                 ["1917"],
                 ["JoJo Rabbit", "Joker"]]
    return user_list


if __name__ == "__main__" :
    global movies, similar_movies, movies_seen_by_user
    movies = create_movies_dataset()
    similar_movies = create_similar_movies_dataset()
    movies_seen_by_user = list(itertools.chain(*create_user_data()))
    assert get_highest_rated_movie(movies, similar_movies, movies_seen_by_user) == "1917", "Test case failed"
    print("Well done. Unit tests passed !!!!")
