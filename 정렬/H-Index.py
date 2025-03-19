def solution(citations):
  citations.sort(reverse=True)
  for index, citation in enumerate(citations, 1):
    if citation < index:
      return index-1
  return len(citations)

# 복습 풀이
def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i, ci in enumerate(citations, start = 1):
        if ci >= i:
            answer = i
        else:
            break
    
    return answer