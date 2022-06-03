## problem site : http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=297&sca=99

def listtoInteger(inboard):
    num = 0
    for i in range(4):
        num = num + inboard[i]*(10**(3-i))
    return num


def clockwiseboard(inboard):
    result = 10000
    for i in range(4):
        current_int = listtoInteger(inboard)
        if current_int < result:
            result = current_int
        inboard.append(inboard.pop(0))
    return result

input_board = []
for i in range(4):
    a = int(input("please enter the {0}th number : ".format(i+1)))
    input_board.append(a)
our_clockwiseNum = clockwiseboard(input_board)
count = 0
existing_list = []
for i1 in range(1,10):
    for i2 in range(1,10):
        for i3 in range(1,10):
            for i4 in range(1,10):
                current_list = [i1, i2, i3, i4]
                current_clockwiseNum = clockwiseboard(current_list)
                if current_clockwiseNum < our_clockwiseNum and (current_clockwiseNum not in existing_list):
                    existing_list.append(current_clockwiseNum)
                    count+=1

print("{0}th 시계수입니다.".format(count+1))
                




