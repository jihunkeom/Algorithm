def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize==0:
        return 5*len(cities)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache_idx = cache.index(city)
            cache = [city] + cache[:cache_idx] + cache[cache_idx+1:]
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache = [city] + cache
            elif len(cache) >= cacheSize:
                cache = [city] + cache[:cacheSize-1]
            answer += 5
        # print(answer, city, cache)
    return answer