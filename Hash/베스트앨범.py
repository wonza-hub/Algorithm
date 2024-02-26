from collections import defaultdict

def solution(genres, plays):
    answer = []
    data = dict()
    play_sums = defaultdict(int)
    for idx, genre, play in zip(range(len(genres)), genres, plays):
        data[idx] = [play, genre]                        
        play_sums[genre] += play
    play_sums = dict(sorted(play_sums.items(), key = lambda x: -x[1]))
    data = dict(
        sorted(data.items(), key = lambda x: (-x[1][0], x[0]))
    )
    for g in play_sums.keys():
        cnt = 0
        for key, value in data.items():
            if cnt == 2:
                break
            if value[1] == g:
                answer.append(key)
                cnt += 1
                
    return answer