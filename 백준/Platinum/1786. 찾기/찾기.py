t = input().rstrip()
p = input().rstrip()
len_p = len(p)
pi=[0] *len_p


def makeTable(P):  # P는 패턴
    lp = len(P)
    Table = [0] * lp  # 패턴의 길이와 같은크기의 테이블 생성
    i = 0  # i를 사용하여 테이블 값을 갱신한다
    for j in range(1, lp):
        while i > 0 and P[i] != P[j]:  # i와 j가 다르면 i는 i-1의 테이블값 인덱스로 돌아간다
            i = Table[i - 1]  # 왜?->현재의 i에서 j와 다르니 i가 +1되었던것을 되돌아가서
            # i-1에서의 테이블값 인덱스에서 다시 j와 비교해준다
            # 테이블에는 최대 공통 부분들이 있어서 돌아갈지점을 계속 갱신해주다가
            # 0까지 가면 0이 된다.0을 저장하고 다음 j로 넘어간다

        if P[i] == P[j]:  # 만약 같으면 i값을 1더해주고 table값에 넣는다.
            i += 1  # i,j둘다 1씩 증가한다
            Table[j] = i
    return Table
answer=  []
answer_count = 0

table = makeTable(p)

j= 0
for i in range(len(t)):

    while j > 0 and t[i] != p[j]:
        j = table[j-1]
    if t[i] == p[j] :

        if len_p- 1 == j:
            answer_count +=1
            answer.append(i-len_p + 2 )
            j= table[j]
        else:
            j+=1
print(answer_count)
print(*answer)
