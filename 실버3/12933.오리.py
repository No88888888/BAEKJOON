'''
문제
오리의 울음 소리는 "quack"이다. 올바른 오리의 울음 소리는 울음 소리를 한 번 또는 그 이상 연속해서 내는 것이다. 예를 들어, "quack", "quackquackquackquack", "quackquack"는 올바른 오리의 울음 소리이다.

영선이의 방에는 오리가 있는데, 문제를 너무 열심히 풀다가 몇 마리의 오리가 있는지 까먹었다.

갑자기 영선이의 방에 있는 오리가 울기 시작했고, 이 울음소리는 섞이기 시작했다. 영선이는 일단 울음소리를 녹음했고, 나중에 들어보면서 총 몇 마리의 오리가 있는지 구해보려고 한다.

녹음한 소리는 문자열로 나타낼 수 있는데, 한 문자는 한 오리가 낸 소리이다. 오리의 울음 소리는 연속될 필요는 없지만, 순서는 "quack"이어야 한다. "quqacukqauackck"과 같은 경우는 두 오리가 울었다고 볼 수 있다.

영선이가 녹음한 소리가 주어졌을 때, 영선이 방에 있을 수 있는 오리의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 영선이가 녹음한 소리가 주어진다. 소리의 길이는 5보다 크거나 같고, 2500보다 작거나 같은 자연수이고, 'q','u','a','c','k'로만 이루어져 있다.

출력
영선이 방에 있을 수 있는 오리의 최소 수를 구하는 프로그램을 작성하시오. 녹음한 소리가 올바르지 않은 경우에는 -1을 출력한다.
'''

duck = list(input())
stack = []
for i in range(len(duck)):
    if duck[i] == 'q':
        if stack == []:
            stack.append([duck[i]])
        else:
            for j in range(len(stack)):
                if stack[j][-1] == 'k':
                    stack[j].append(duck[i])
                    break
            else:
                stack.append([duck[i]])
    elif duck[i] == 'u':
        for j in range(len(stack)):
            if stack[j][-1] == 'q':
                stack[j].append(duck[i])
                break
        else:
            print(-1)
            exit()
    elif duck[i] == 'a':
        for j in range(len(stack)):
            if stack[j][-1] == 'u':
                stack[j].append(duck[i])
                break
        else:
            print(-1)
            exit()
    elif duck[i] == 'c':
        for j in range(len(stack)):
            if stack[j][-1] == 'a':
                stack[j].append(duck[i])
                break
        else:
            print(-1)
            exit()
    elif duck[i] == 'k':
        for j in range(len(stack)):
            if stack[j][-1] == 'c':
                stack[j].append(duck[i])
                break
        else:
            print(-1)
            exit()
cnt = 0
for j in range(len(stack)):
    if len(stack[j]) % 5 == 0:
        cnt += 1
    else:
        print(-1)
        exit()
print(cnt)
# cnt = 0
# for k in range(len(stack)):
#     if not len(stack[k]) % 5:
#         cnt += 1
# if not cnt:
#     print(-1)
# else:
#     print(cnt)