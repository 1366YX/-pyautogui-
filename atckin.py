import pyautogui
import time
import random
from apscheduler.schedulers.blocking import BlockingScheduler

#time.sleep(2*60)
def program_a():
 pyautogui.click(1527,66)
 time.sleep(5)
 pyautogui.click(1494,624)
 time.sleep(15)
 pyautogui.doubleClick(1365,383)
 time.sleep(15)
 x=random.randint(966-5,966+5)
 y=random.randint(559-5,559+5)
 pyautogui.click(x,y)
 time.sleep(15) #选取符合规定的随机位置
 pyautogui.click(1331,793)#设定完成虚拟定位
 time.sleep(15)
 pyautogui.click(1508,542)
 time.sleep(20)#打开微信并等待
 pyautogui.click(1183,78)
 time.sleep(20)
 pyautogui.click(753,163)
 time.sleep(20)
 pyautogui.click(807,336)
 time.sleep(60)
 pyautogui.click(958,918)

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # 添加定时任务，每天早上6点10分执行
    scheduler.add_job(program_a, 'cron', hour=6, minute=10)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass










