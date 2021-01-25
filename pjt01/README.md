### Project 01 (01.22.Fri)



> ### Python을 활용한 데이터수집





#### A. 제공되는 영화 데이터의 주요내용 수집

* 데이터 :  movie.json - 쇼생크 탈출

  * 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids
    키에 해당하는 정보만 가져옵니다.

* 결과

  * 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보 가져오기
  * 가져온 정보를 새로운 dictionary 로 반환하는 함수 movie_info 를 완성하기.

  

  ```python
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
  ```
  
  > 과정
  
  사실,  a번은 movie에서 있는 정보만 잘 빼와서 결과 dict을 완성하는 문제라 어렵지는 않았다.
  
  하지만. vs code 과 bash창이랑 안친해서 애 먹었다..
  
  코드 저장을 하고 bash창에서 파이썬 돌려줘 해야하는데 그걸 까먹는다. 코드를 그냥 생각나는대로 쓰고 보니까 줄일 수 있었지만 다음 문제로 넘어갔다.
  
  
  
  

#### B. 제공되는 영화 데이터의 주요내용 수정

* 이전단계에서 만들었던 데이터 중 genre_ids 를 genre_names 로 바꿔 반환하는 함
  수를 완성합니다.

  ```python
  ef movie_info(movie, genres): # 쇼생크 / id, name
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
  ```
  
  
  
  >과정
  
  a번의 확장판으로 다른 데이터를 불러와 업데이트를 해야했다.
  
  두 데이터의 연결고리인 id 를 찾고, 업데이트를 했다.
  
  사실 이런 두 데이터를 연결하는 것은 merge 방법으로 했었는데 이렇게 for문을 짜는 것이 생소했다.
  
  또한, 데이터프레임만 주구장창 다뤄봤지 이런 list와 dict이랑 안친해서 더 친해져야 겠다. 
  
  > 저 위에 코드는 genre 두개를 불러와야하는데 마지막  하나만 불러와진다.

+ 추가(01.24 

+ ```python
  def movie_info(movie, genres): 
      pass
      # 여기에 코드를 작성합니다.  
      result = {}
      list_n =[]
      for id in movie['genre_ids']:
          for movie_dict in genres:
              if movie_dict['id'] == id:
                  list_n += [movie_dict['name']] #append랑 결과 다름
  
      result['genre_names'] = list_n # [list_n]이랑 결과 다름 
  
      result['id'] = movie['id']
      result['title'] = movie['title']
      result['poster_path'] = movie['poster_path']
      result['vote_average'] = movie['vote_average']
      result['poster_path'] = movie['poster_path']
      result['overview'] = movie['overview']
      return result  
  pprint(movie_info(movie, genres_list))   
  ```

  > 월말평가 대비로 다시 풀어보면서 이전 코드가 틀렸다는 걸 알게되었다.



####  C. 다중 데이터 분석 및 수정

T MDB 기준 평점이 높은 20 개의 영화데이터가 주어집니다. 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다 . 완성된 함수는 향후 커뮤니티 서비스에서 제공되는 영화 목록을 제공하기 위한 기능으로 사용됩니다.

```python
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
```

> 과정

얘는 이번에 b의 확장판 이었다. 역시나 list랑 dict이랑 친해지지 않았고..중간에 for문 작성할 때 배고파지고, 머리가 꼬여서 완전 애먹었다.

'b에다가 for문 하나만 추가하면돼'를 생각하며 코드를 작성했다....



#### D. 알고리즘을 통한 데이터 출력
세부적인 영화 정보 중 수익 정보 (r evenue) 를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성합니다 해당 데이터는 향후 커뮤니티 서비스에서 메인 페이지 기본정보로 사용됩니다

```python

def max_revenue(movies):
    pass
    # 여기에 코드를 작성합니다. 
     
    result = ' '                              # max_revenue movie name
    max_rev = 0                               # max_revenue

    for movie in movies:
        movie_id = movie['id']         # movies 폴더에 있는 data를 불러오기 위해 id 변수 생성
       
        movies_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')    
        movies_list = json.load(movies_json)
    
        if int(movies_list['revenue']) > max_rev :                  # find max_revenue 
            max_rev = int(movies_list['revenue'])
            result =  movies_list['original_title']
    
    return result
```

> 과정

개인적으로 c보다 얘를 더 빨리 풀 수 있었던거 같다... 폴더에 있는 것들을 불러오는 방법을 생각하는 것에 오래걸렸다. 처음에는 id =[13, ㅇㅇ,ㅇㅇㅇ] 이런식으로 폴더에 있는 숫자들을 적고 f-string으로 불렀다....ㅎㅎ



#### E. 알고리즘을 통한 데이터 출력
세부적인 영화 정보 중 개봉일 정보 release_date) 를 이용하여 모든 영화 중 12 월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다 해당 데이터는 향후 커뮤니티 서비스에서 추천기능의 정보로 사용됩니다.

```python
def dec_movies(movies):
    pass
    # 여기에 코드를 작성합니다.  
    result_list=[]

    for movie in movies:
        movie_id = movie['id']         # movies 폴더에 있는 data를 불러오기 위해 id 변수 생성
       
        movies_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')    
        movies_list = json.load(movies_json)

        if int(movies_list['release_date'][5:7]) == 12:  # 이놈의 int()안붙여서!!

            result_list.append(movies_list['original_title'])
            
    return result_list

```



> 과정

코드는 금방 짠거 같은데 자꾸 str, int 에러랑 for문으로 뽑은게 dict인걸 까먹는다....

리스트 업데이트를 += 랑 append랑 별 짓을 했는데 빈 리스트 나오네.....▷if 문에 int()!!!!!!!



