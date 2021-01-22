import json
from pprint import pprint


def movie_info(movies, genres):   # list 안에 dict 20개 / list 안에 id, name 19개 dict
    pass
    # 여기에 코드를 작성합니다.  
    result = []                                        # empty list
    for movie in movies:                               # list 안에 있는 dict 1개

        result_dict = {}                               # result list에 들어갈 dict
        result_dict['id'] = movie['id']                # update result from movie
        result_dict['title'] = movie['title']
        result_dict['poster_path'] = movie['poster_path']
        result_dict['vote_average'] = movie['vote_average']
        result_dict['overview'] = movie['overview']
        
        result_dict['genre_names'] =[]                  # 추가함..

        for g_id in movie['genre_ids']:                 # movie에 있는 id  / (for compare with ids in genres)
            for g_dict in genres:                       # genres에 있는 1개의 dict
                if g_dict['id'] == g_id:
                    result_dict['genre_names'] += [g_dict['name']]   # update 

        result += [result_dict]                         # final update 
    return result              



# # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))