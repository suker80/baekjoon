def main():
    flt, pw = input().split()
    pos = len(flt[flt.index('.') + 1:]) # 실수의 정수부


    flt = flt.replace('.', '')
    result = str(int(flt) ** int(pw))
    pos = str((10 ** pos) ** int(pw)) # 정부수끼리의 자릿수 계산


    # 정수 계산결과와 자릿수로 '.' 소숫점이 들어갈 부분을 체크한다.
    # 만약 입력숫자가 0.nn.. 정수부가 없다면 음수, 그렇지 않다면 양수이다.
    index = len(result) - len(pos) + 1

    if index >= 0:
        print(result[:index] + '.' + result[index:])
    else:
        print('0.' + '0' * (-index) + result)


if __name__ == '__main__':
    main()