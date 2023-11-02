문제 = `문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.`

>> string 의 각 인덱스별로 dict 타입으로 변환하고 싶을 때 사용하는 키워드 

1. dict.fromkeys(my_string)

입력값 〉
  	"people"
기댓값 〉
  	"peol"
실행 결과 〉
	실행한 결괏값 ""이 기댓값 "peol"과 다릅니다.
출력 〉
    {'p': None, 'e': None, 'o': None, 'l': None}

    -> None은 파이썬에서 존재하는 타입으로 유일 타입이다. 
    -> value 값을 conut 용도로 쓴다고 한다면 dict.fromkeys(my_string,0) 으로 초기화 해줘야 한다.

2. dict 타입을 string 타입으로 변환. ''.join()메서드 이용.



def solution(my_string): 
    answer = ""
    for i in my_string:
        if i not in answer:
            answer += i                
    return answer

    
def solution(my_string):
    return ''.join(dict.fromkeys(my_string)) 



