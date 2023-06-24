'''
문제


아무래도 우리 팀 다리우스가 고수인 것 같다. 그의 
$K/D/A$를 보고 그가 「진짜」인지 판별해 보자.

 
$K+A < D$이거나, 
$D = 0$이면 그는 「가짜」이고, 그렇지 않으면 「진짜」이다.

입력
 
$K/D/A$가 주어진다.

출력
그가 「진짜」이면 gosu, 「가짜」이면 hasu를 출력한다.

제한
 
$0 \le K, D, A \le 20$ 
'''

K,D,A = map(int, input().split('/'))
if K+A < D or D == 0:
    print('hasu')
else : 
    print('gosu')