import json
from pprint import pprint


def movie_info(movie):
    pass
    # 여기에 코드를 작성합니다.    
    result = { }                                    # empty dict 생성
   
    m_id = movie_dict['id']                         # 필요한 정보들 가져오기
    m_title = movie_dict['title']
    m_poster_path = movie_dict['poster_path']
    m_vote_average = movie_dict['vote_average']
    m_overview = movie_dict['overview']
    m_genre_ids = movie_dict['genre_ids']


    result['id'] = m_id                             # result에 추가하기
    result['title'] = m_title
    result['poster_path'] = m_poster_path
    result['vote_average'] = m_vote_average
    result['overview'] = m_overview
    result['genre_ids'] = m_genre_ids

    return result




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))