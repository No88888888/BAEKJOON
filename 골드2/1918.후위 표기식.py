'''
����
������ �Ϲ������� 3���� ǥ������� ǥ���� �� �ִ�. �����ڰ� �ǿ����� ��� ��ġ�ϴ� ���� ǥ���(�Ϲ������� �츮�� ���� ����̴�), �����ڰ� �ǿ����� �տ� ��ġ�ϴ� ���� ǥ���(prefix notation), �����ڰ� �ǿ����� �ڿ� ��ġ�ϴ� ���� ǥ���(postfix notation)�� �װ��̴�. ���� ��� ���� ǥ������� ǥ���� a+b�� ���� ǥ������δ� +ab�̰�, ���� ǥ������δ� ab+�� �ȴ�.

�� �������� �츮�� �ٷ� ǥ����� ���� ǥ����̴�. ���� ǥ����� ������ ���� ���� ���� �����ڰ� �ǿ����� �ڿ� ��ġ�ϴ� ����̴�. �� ����� ������ ������ ����. �츮�� ���� ���� ���� ǥ��� ���� ��쿡�� ������ ������ �켱������ ���̰� �־� ���ʺ��� ���ʷ� ����� �� ������ ���� ǥ����� ����ϸ� ������ ������ �����Ͽ� ������ ������ �� �ִ�. ���� ���� ������� ��ȣ � �ʿ� ���� �ȴ�. ���� ��� a+b*c�� ���� ǥ������� �ٲٸ� abc*+�� �ȴ�.

���� ǥ����� ���� ǥ������� �ٲٴ� ����� ������ �����ϸ� �̷���. �켱 �־��� ���� ǥ����� �������� �켱������ ���� ��ȣ�� �����ش�. �׷� ������ ��ȣ ���� �����ڸ� ��ȣ�� ���������� �Ű��ָ� �ȴ�.

���� ��� a+b*c�� (a+(b*c))�� �İ� ���� �ȴ�. �� ������ �ȿ� �ִ� ��ȣ�� ������ *�� ��ȣ ������ ������ �Ǹ� (a+bc*)�� �ȴ�. ���������� �� +�� ��ȣ�� ���������� ��ġ�� abc*+�� �ǰ� �ȴ�.

�ٸ� ���� ��� �׸����� ǥ���ϸ� A+B*C-D/E�� �����ϰ� ��ȣ�� ���� �����ڸ� �̵���ų ��Ҹ� ǥ���ϸ� ������ ���� �ȴ�.



���: ABC*+DE/-

�̷��� ����� �˰� ���� ǥ����� �־����� �� ���� ǥ������� ��ġ�� ���α׷��� �ۼ��Ͻÿ�

�Է�
ù° �ٿ� ���� ǥ����� �־�����. �� �� ������ �ǿ����ڴ� ���ĺ� �빮�ڷ� �̷������ ���Ŀ��� �� ������ �����Ѵ�. �׸��� -A+B�� ���� -�� ���� �տ� ���ų� AB�� ���� *�� �����Ǵ� ���� ������ �־����� �ʴ´�. ǥ����� ���ĺ� �빮�ڿ� +, -, *, /, (, )�θ� �̷���� ������, ���̴� 100�� ���� �ʴ´�. 
'''
# ���� �Ⱥ��� ������
sik = list(input())
stack = []
result = []
for i in sik:
    if not i in '*/+-()':   # ���ڸ� result�� �ٷ� �߰�
        result.append(i)
    elif i == '(':          # (�� stack�� �׳� �߰�
        stack.append(i)
    elif i in '*/':         # */��
        if stack == []:     # stack ������� �׳� �߰�
            stack.append(i)
        else:               # �� ������� */���� ���� �����ڳ��ö����� pop
            while stack[-1] in '*/':
                result.append(stack.pop())
                if stack == []:
                    break
            stack.append(i) # �׸��� stack�� �߰�
    elif i in '+-':         # +-��
        if stack == []:     # stack ������� �׳� �߰�
            stack.append(i)
        else:               # �� ������� (������ Ȥ�� stack�������� pop
            while stack[-1] != '(':
                result.append(stack.pop())
                if stack == []:
                    break
            stack.append(i) #�׸��� stack�� �߰�
    elif i == ')':          # )��
        while stack[-1] != '(': # (���Ë����� pop
            result.append(stack.pop())
        stack.pop()         #(�� pop
while stack !=[]:           # stack�� ���� ������ result�� �߰�
    result.append(stack.pop())
print(''.join(result))      # ���

# �������� ������ �� �ڵ�
sik = list(input())
stack = []
result = []
for i in sik:
    if i in '+-*/()':
        if not stack:
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i in '*/':
            while stack and stack[-1] in '*/':
                result.append(stack.pop())
            stack.append(i)
        elif i in '+-':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
    else:
        result.append(i)
while stack != []:
    result.append(stack.pop())
print(''.join(result))
        
