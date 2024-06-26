def solution(people, limit):
    answer = len(people)
    p = sorted(people, reverse = True)
    s,e = 0, len(p)-1

    while s < e :
        if p[s]+p[e] <= limit :
            e-=1
            answer-=1
        s+=1
    return answer


def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1

    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer