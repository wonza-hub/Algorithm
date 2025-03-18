from collections import Counter

def slice(string):
    tmp=[]
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            tmp.append(string[i].upper()+string[i+1].upper())
            
    return tmp

def cal_jc(ic,uc):
    if uc==0:
        return 1
    
    return ic/uc
    
def inter(d1,d2):
    inter_cnt=0
    for k in d1.keys():
        if k in d2:
            inter_cnt+=min(d1[k],d2[k])
            
    return inter_cnt
    
    
def uni(d1,d2):
    uni_cnt=0
    com=[]
    for k in d1.keys():
        if k in d2:
            uni_cnt+=max(d1[k],d2[k])
            com.append(k)
    for k in d1.keys():
        if k not in com:
            uni_cnt+=d1[k]
    for k in d2.keys():
        if k not in com:
            uni_cnt+=d2[k]
            
    return uni_cnt
    
def solution(str1, str2):
    tmp1=slice(str1)
    tmp2=slice(str2)
    ic=inter(Counter(tmp1),Counter(tmp2))
    uc=uni(Counter(tmp1),Counter(tmp2))
    
    return int(cal_jc(ic,uc)*65536)

# 다른 사람의 풀이 (집합 자료형을 사용)
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)