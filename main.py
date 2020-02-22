from Table import *
from FileSearcher import *

output_path = None
CuttingStart = 18.3
CuttingToEnd = 7
CuttingEnd = None
if __name__ == '__main__':

    AddInfo('功能(序号)', '说明')
    AddInfo('1.转换单个文件', '拖放文件即可')
    AddInfo('2.转换文件夹下所有视频', '只支持mp4')
    AddInfo('3.设置开始时间', '默认从18.3s开始')
    AddInfo('4.设置距结尾的时间', '默认从尾7秒开始')
    AddInfo('5.设置结尾的时间', '默认设置无此项')
    AddInfo('6.设置输出目录', '默认与原文件同目录,若要恢复输入None')
    AddInfo('7.退出', 'None')

    while True:
        os.system("cls")
        PrintTable()
        IN = str(input('输入选项：'))
        if '1' == IN:
            file = str(input('把文件拖入窗口：'))
            FileInfo(False, file, output_path, CuttingStart, CuttingToEnd, CuttingEnd)

        elif '2' == IN:
            file = str(input('把文件夹拖入窗口：'))
            FileInfo(True, file, output_path, CuttingStart, CuttingToEnd, CuttingEnd)

        elif '3' == IN:
            CuttingStart = int(input('设置开始时间：'))

        elif '4' == IN:
            CuttingEnd = None
            CuttingToEnd = int(input('设置距结尾的时间：'))

        elif '5' == IN:
            CuttingEnd = int(input('设置距结尾的时间：'))

        elif '6' == IN:
            tmp = str(input('设置输出目录：'))
            if 'None' != tmp:
                output_path = tmp

            else:
                output_path = None

        elif '7' == IN:
            quit()
