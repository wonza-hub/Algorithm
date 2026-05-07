# AI 풀이
from collections import defaultdict

# 진입 진출 차수로 무관 정점을 찾는 것은 파악했으나,
# 그래프 모양들도 진입 진출 차수로 구할 수 있는 것을 놓쳤음
def solution(edges):
    out_deg = defaultdict(int)
    in_deg = defaultdict(int)
    
    for a, b in edges:
        out_deg[a] += 1
        in_deg[b] += 1
    
    # 무관 정점: 출력차수 >= 2, 진입차수 == 0
    root = -1
    for v in out_deg:
        if out_deg[v] >= 2 and in_deg[v] == 0:
            root = v
            break
    
    # 8자 그래프 중심점: 출력차수 == 2, 진입차수 >= 2
    eight_count = 0
    for v in out_deg:
        if v == root:
            continue
        if out_deg[v] == 2 and in_deg[v] >= 2:
            eight_count += 1
    
    # 막대 그래프: 출력차수 == 0인 정점 수
    bar_count = 0
    # A → B → C 인 경우:
    # out_deg에 기록되는 정점: A, B (나가는 간선이 있는 것만)
    # in_deg에 기록되는 정점: B, C (들어오는 간선이 있는 것만)
    # 막대 그래프의 끝점을 찾을 수 있음
    all_nodes = set(out_deg.keys()) | set(in_deg.keys())
    for v in all_nodes:
        if out_deg[v] == 0:
            bar_count += 1
    
    # 무관 정점의 출력차수 = 전체 그래프 수
    total = out_deg[root]
    donut_count = total - bar_count - eight_count
    
    return [root, donut_count, bar_count, eight_count]