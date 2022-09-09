l, c = map(int, input().split())
string = list(map(str, input().split()))

string.sort()

consonant = 'bcdfghjklmnpqrstvwxyz'
vowel = 'aeiou'


def comb(idx, cur=None):
    if cur is None:
        cur = ''

    if len(cur) > l:
        return
    if len(cur) == l:
        vowel_cnt = 0
        consonant_cnt = 0
        for i in cur:
            if i in vowel:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(cur)
        return
    if idx >= c:
        return

    comb(idx + 1, cur + string[idx])
    comb(idx + 1, cur)
comb(0)