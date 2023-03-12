import sys
sys.stdin = open('0_BOJ_비슷한단어.txt', 'r')

num = int(input())

word = input()

#첫 번째 단어가 어떤 단어로 어떤 개수로 구성되어있는지 파악
components = {}
for _ in word:
    if _ in components:
        components[_] += 1
    else:
        components[_] = 1

count = 0
for i in range(num-1):
    #다른 단어들의 구성을 돌아가면서 파악한다.
    temp = input()
    components_temp = {}

    for _ in temp:
        if _ in components_temp:
            components_temp[_] += 1
        else:
            components_temp[_] = 1

    #첫번째 단어와 구성을 비교한다.
    remains = 0
    now = 0

    for component in components:
        if component in components_temp:
            remains += abs(components[component] - components_temp[component])
            if abs(components[component] - components_temp[component]) == 1:
                now = 1
        else:
            remains += components[component]
            if components[component] == 1 and now == 1:
                now = 1
        if now == 1:
            remains = 1
    
    #첫번째 단어의 길이보다 비교하는 단어의 길이가 더 길다면,
    #비교하는 단어의 구성요소 중에 첫번째 단어가 가지지 못한 요소의 수도 고려해준다.
    if len(temp) > len(word):
        for temp_component in components_temp:
            if temp_component not in components:
                remains += components_temp[temp_component]

    #구성요소의 차이값이 0이거나 1이면 비슷한 단어로 취급한다.
    if remains == 0 or remains == 1:
        count += 1

print(count)