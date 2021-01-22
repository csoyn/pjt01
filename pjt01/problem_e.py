import json


def dec_movies(movies):
    pass
    # 여기에 코드를 작성합니다.  
    result_list=[]

    for movie in movies:
        movie_id = movie['id']                # movies 폴더에 있는 data를 불러오기 위해 id 변수 생성
       
        movies_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')    
        movies_list = json.load(movies_json)

        if int(movies_list['release_date'][5:7]) == 12:

            result_list.append(movies_list['original_title'])
            
    return result_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
