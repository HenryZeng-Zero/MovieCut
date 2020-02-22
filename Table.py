Conduct = 0
Count = 0
Long = []
Info = []


def PrintTable():
    global Long, Info

    for Con in Info:
        # 打印表头分割线
        print('+', end='')
        for i in Long:
            for Tmp in range(i):
                print('-', end='')
            print('+', end='')
        print('\n', end='')
        # 打印表头分割线

        Index = 0
        for Now in range(len(Long)):
            try:
                String = Con[Now]
            except:
                String = ''

            print('| ' + String, end='')
            Empty_Length = LengthOfChinese(String)
            for Tmps in range(Long[Index] - Empty_Length - 1):
                print(' ', end='')
            Index += 1
        print('|')
    # 打印表尾分割线
    print('+', end='')
    for i in Long:
        for Tmp in range(i):
            print('-', end='')
        print('+', end='')
    print('\n', end='')
    # 打印表尾分割线


def AddInfo(*C):
    global Long, Conduct, Info, Count
    if len(C) > Count:
        for i in range(len(C) - Count):
            Count += 1
            Long.append(0)
        # 根据数据添加存储间隔数据的list项
    Index = 0

    Lib = []
    for tmp in range(len(C)):
        Lib.append('')
    Info.append(Lib)

    for i in C:
        Info[Conduct][Index] = i
        Length = LengthOfChinese(i)
        if Length > Long[Index]:
            Long[Index] = Length + 2
        Index += 1
    Conduct += 1


def LengthOfChinese(Sentence):
    Length = 0
    for ZhCN in Sentence:
        if '\u4e00' <= ZhCN <= '\u9fff':
            Length += 2
        else:
            Length += 1
    return Length
