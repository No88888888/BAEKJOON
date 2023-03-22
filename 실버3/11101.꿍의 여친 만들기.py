'''
문제
꿍은 나름 잘생기고 똑똑하지만 여자앞에서면 말을 잘 못하는 안타까운 학생이다. 그러던 그가 어느 날 한눈에 반한 여학생이 생겼지만 역시나 그녀에게 다가가지 못했다.

훗날 꿍은 이런 자신을 반성하며 다시 한 번 그녀에게 다가가기로 마음먹었다. 하지만 그 전에, 꿍은 그녀가 원하는 남자 스타일에 맞는 사람으로 나타나기로 하였다. 알고봤더니 그녀는 다양한 스타일의 남자를 좋아하지만 선택적인 것으로 밝혀졌다. 예를 들어, 그녀는 똑똑하고(intelligent) 세련된(cultivated) 옷을 잘 입는(welldressed) 남자 또는 오토바이를 갖고 있으며(motorcycleowner) 살짝 무뚝뚝한(rude) 남자를 좋아한다. 아니면 단순히 부자(rich)여도 된다.

꿍은 이러한 그녀의 취향에 대한 모든 정보를 적고 그 취향을 만족시키기 위한 계획을 세웠다. 꿍은 각 조건들이 걸리는 시간을 측정하여 어떠한 조합이 가장 시간이 적게 걸리는지 계산만 하면 된다. 이때 꿍은 각 조건들을 병렬적으로 만족시킬 수 있다고 생각한다.

아래 그림을 보자.



[그림: 꿍이 그녀를 정복하기 위해 해야할 것들]

위 그림에서 꿍은 intelligent, cultivated, welldressed 조합을 모두 만족시키는데 걸리는 최소의 시간은 4이다. 왜냐면 꿍은 병렬적으로 조건들을 만족시킬 수 있기 때문이다. 마찬가지 방법으로 따져보면 motorcycleowner, rude 조합을 만족시키는데는 8, rich 조합은 100의 시간이 걸린다. 이 세 가지 조합 중 가장 시간이 적게 걸리는 조합은 intelligent, cultivated, welldressed 조합이다.

입력
첫 번째 줄에는 테스트케이스의 개수가 주어진다 (최댓값=100).

각 테스트케이스는 두 줄의 문자열이 주어진다.

첫 번째 문자열은 각 조건을 만족시키는데 걸리는 시간이 ','(쉼표)에 의해 구분되어 주어지며 조건의 이름, 콜론(:), 그리고 걸리는 시간으로 구성되어 있다. 조건의 이름은 a부터 z까지로만 이루어져 있으며 길이는 1부터 20이다. 비용은 0부터 1000까지 각각 주어지며 조건의 개수는 20을 넘지 않는다.

두 번째 문자열은 그녀를 만족시키는데 필요한 조건의 조합들이 주어진다. 각 조합은 '&'기호와 '|'기호로 구분되어 주어진다. 조합의 개수는 10을 넘지 않으며 각 조합은 최소 한 가지의 조건이 포함되어 있으며 같은 조건이 두번이상 나오지 않는다.

출력
각 테스트케이스에 대해 그녀의 조건을 만족시키는데 걸리는 최소의 시간을 출력한다.
'''
# import sys
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    condition1 = list(map(str, input().split(',')))     # 조건과 조건 만족에 걸리는 시간
    taketime = {}
    for i in condition1:
        temp = i.split(':')
        taketime[temp[0]] = int(temp[1])                # 딕셔너리에 {'조건': 조건충족 시간} 형식으로 저장
        
    condition2 = list(map(str, input().split('|')))     # 여자가 원하는 조건 조합
    comb = []
    for i in condition2:
        temp = tuple(i.split('&'))                      # 조합별로 분리
        comb.append(temp)
        
    mintime = float('inf')                              # 조합 충족 걸리는 시간 최소 구하기 위한 값
    for i in range(len(comb)):
        maxtime = 0                                     # 하나의 조합을충족하는데 걸리는 시간
        for j in range(len(comb[i])):
            maxtime = max(maxtime, taketime[comb[i][j]])# 하나의 조합 내에서 가장 오래걸리는 시간이 해당 조합을 충족시키는데 걸리는 시간
        mintime = min(mintime, maxtime)                 # 조합들의 걸리는 시간 중 최소 시간을 찾는다
        
    print(mintime)