from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_count = defaultdict(int)
    genre_music = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_count[g] += p
        genre_music[g].append([i, p])
        
    sorted_genre_count = sorted(genre_count, key = lambda x: genre_count[x], reverse=True)
    
    for genre in sorted_genre_count:
        sorted_genre_music = sorted(genre_music[genre], key = lambda x: (-x[1], x[0]))
        
        answer.extend([music[0] for music in sorted_genre_music][:2])

    return answer
