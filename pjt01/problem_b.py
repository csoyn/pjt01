import json
from pprint import pprint


def movie_info(movie, genres): # 쇼생크 / id, name
    pass
    # 여기에 코드를 작성합니다.  
        
    result = {} # empty dict

    result['id'] = movie['id']                     # update result from movie
    result['title'] = movie['title']
    result['poster_path'] = movie['poster_path']
    result['vote_average'] = movie['vote_average']
    result['overview'] = movie['overview']
    
    for g_id in movie['genre_ids']:                 # movie에 있는 id  / (for compare with ids in genres)
        for g_dict in genres:                       # genres에 있는 1개의 dict
            if g_dict['id'] == g_id:   
                                                    # 두 id를 비교
                g_name = []                         # empty list for update result
                g_name += [g_dict['name']]           

    result['genres_names'] =  g_name                # result update

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))