# 문제
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

# 입력
2
AAA
AAA

# 출력
1998

> DICTIONARY, 쉽게 생각하자. 

# 풀이
```python
import sys
N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(N)]
words = {} # 단어별 값을 지정
for s in S: 
    x = len(s)-1 # 10의 제곱을 해줄 값
    for i in s :
        if i in words:
            words[i] += 10**x # 있으면 x만큼 제곱한걸 더하고
        else :
            words[i] = 10**x # 없으면 x만큼 제곱해서 넣자
        x -= 1

words_sort = sorted(words.values(),reverse=True) # 딕셔너리의 value만 내림차순으로 가져오자
result = 0
num = 9
for k in words_sort:
    result += k * num # 내림차순 한거에 9부터 하나씩 곱해서 더해주자
    num -= 1
print(result)
```
