def solution(cacheSize, cities):
    answer = 0

    low_cities=[]

    #대소문자를 구분하지 않기 때문에 도시 이름을 전부 소문자로 바꿔준다
    for v in cities:
        low_cities.append(v.lower())

    #LRU: 가장 오래동안 참조되지 않은 페이지를 교체하는 방식
    LRU_cache=[]

    for city in low_cities:
        #LRU_cache가 캐시 사이즈보다 작고 cache miss면
        if len(LRU_cache)<cacheSize and city not in LRU_cache:
            LRU_cache.append(city)
            answer+=5
        #캐시 사이즈가 0인 경우
        elif cacheSize==0:
            answer+=5        

        else:
            #cache hit
            if city in LRU_cache:
                LRU_cache.remove(city)
                LRU_cache.append(city)
                answer+=1
            #cache miss
            else:
                del LRU_cache[0]
                LRU_cache.append(city)
                answer+=5
    
    return answer


print(solution(10,["Jeju", "Pangyo", "NewYork", "newyork"]))