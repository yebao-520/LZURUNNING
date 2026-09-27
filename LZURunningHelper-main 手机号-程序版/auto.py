import datetime
import time
import os

now = datetime.datetime.now().strftime("%Y-%m-%d %H").split()


def timeCompare():
    TIME_TXT_PATH = "C:/Users/von/Desktop/Projects/joyrun/time.txt"
    with open("C:Users\zzh\Downloads\LZURunningHelper-main\time.txt", "r") as t:
        before = t.read()

    # 下面逻辑保持不变
    if before != now[0] and int(now[1]) >= 12:
        while True:
            if netCheck():
                with open(TIME_TXT_PATH, "w", encoding="utf-8") as t:
                    t.write(now[0])
                return True
            else:
                print("网络连接失败，重试中...")
                time.sleep(10)
    return False


def netCheck():
    cmd = "ping www.baidu.com -n 2 >nul"
    exit_code = os.system(cmd)
    if exit_code:
        print("网络连接失败，重试中...")
        return False
    return True


if timeCompare():
    os.system("C:/Users/von/Desktop/Projects/joyrun/start.bat")
