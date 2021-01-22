import json


def max_revenue(movies):
    pass
    # 여기에 코드를 작성합니다. 
     
    result = ' '                              # max_revenue movie name
    max_rev = 0                               # max_revenue

    for movie in movies:
        movie_id = movie['id']                # movies 폴더에 있는 data를 불러오기 위해 id 변수 생성
       
        movies_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')    
        movies_list = json.load(movies_json)
    
        if int(movies_list['revenue']) > max_rev :                             # find max_revenue 
            max_rev = int(movies_list['revenue'])
            result =  movies_list['original_title']
    
    return result


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

print(movies_list)