'''
문제
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

출력
계산 결과를 소숫점 둘째 자리까지 출력한다.
'''

def cal(word, stack):
    for i in word:
        if not i in '+-*/':
            stack.append(i)
        else:
            x = float(stack.pop())  # 소수점 표현위해 float
            y = float(stack.pop())
            
            if i == '+':
                stack.append(y + x)
            if i == '-':
                stack.append(y - x)
            if i == '*':
                stack.append(y * x)
            if i == '/':
                stack.append(y / x)
    return stack[-1]

N = int(input())
sik = list(input())
ABC = []
dic = {}

for i in range(len(sik)):           # 후위표기식에서 중복된 글자 제거
    if sik[i] in '+-*/':
        continue
    else:
        if not sik[i] in ABC:       # ABC에 저장
            ABC += sik[i]
    
for i in ABC:
    dic[i] = input()                # 중복제거된 글자와 대응되는 정수 딕셔너리로 저장

for i in range(len(sik)):
    if not sik[i] in '+-*/':
        sik[i] = dic[sik[i]]        # sik에서 dic 참고하여 숫자로 변경

print(f'{cal(sik, []):.2f}')