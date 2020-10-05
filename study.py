
# coding: utf-8

# In[1]:


from uiautomator import device as driver
import numpy as np
import time
import os
import sys
import random


#######用户编辑区############
isPhone=0#0为模拟器用户，1为手机用户
Height=1280#分辨率的高
Width=720#分辨率的宽
path='/Volumes/Macintosh HD - 数据/python work/'#替换为缓存文件的目录
word=["中国加油！未来在我们手中","希望世界和平，人人幸福安康"]#评论池
############################


savefile=path+'db.npy'
os.system("adb kill-server")
set_send="adb shell am broadcast -a ADB_INPUT_TEXT --es msg '"+word[random.randint(0,len(word)-1)]+"'"#随机选择语句
# In[2]:

all_of_list=[]
subscribe_count=0
drag_str='adb shell input swipe '+str(Width*0.5)+' '+str(Height*0.88)+' '+str(Width*0.5)+' '+str(Height*0.3)#模拟滑动
if isPhone==0:
    os.system("adb connect 127.0.0.1:62001")#连接夜神模拟器
else:
    os.system("adb start-server")
if os.path.isfile(savefile):
    all_of_list = np.load (savefile).tolist()

# In[3]:


def autoJob(tv,sleep_time,sum=6,click=True):
    count_click=0
    count=0
    for _ in range(100):
        text_lists=driver(className='android.widget.TextView')
        try:
            for i in range(len(text_lists)):
                txt=text_lists[i].text
                if len(txt)>11 and txt not in all_of_list and count<sum:
                    driver(text=txt,className='android.widget.TextView').click()
                    time.sleep(5)
                    all_of_list.append(txt)
                    print("正在"+tv+"...",txt)
                    #分享，收藏，评论
                    if click and count_click<2:
                        time.sleep(sleep_time-5) 
                        #分享
                        time.sleep(4)
                        driver.click(0.94*Width, 0.975*Height)
                        time.sleep(2)
                        driver(text="分享到学习强国").click()
                        time.sleep(2)
                        driver.press.back()
                        #收藏
                        driver.click(0.84*Width, 0.975*Height)
                        #评论
                        time.sleep(1)
                        driver(text="欢迎发表你的观点").click()
                        time.sleep(2)
                        os.system(set_send)#评论池随机发送一个评论
                        # os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '中国加油'")
                        #os.system("adb shell input keyevent 66")#不知道为什么输入一个回车，点击发布才有反应
                        time.sleep(2)
                        driver(text="发布").click()
                        count_click=count_click+1
                        driver.press.back()
                    else:
                        time.sleep(sleep_time-5)
                    count=count+1
                    driver.press.back()
                
        except BaseException:
            print("抛出异常，程序继续执行...")
        if count >=sum:
            break
        os.system(drag_str)


def watch_local():
    driver(text='北京').click()
    time.sleep(2)
    driver(text='北京卫视').click()
    print("观看本地频道...")
    time.sleep(20)
    print("本地频道结束")
    driver.press.back()
# In[4]:


#阅读文章,阅读6个文章，每个文章停留130秒
def read_articles():
    time.sleep(2)
    #切换到要闻界面
    driver(text='推荐').click()
    autoJob(tv="阅读文章",sleep_time=120)
    print("阅读文章结束")


# In[5]:


#观看视频,每个视频观看35秒，以及3分钟新闻联播
def watch_video():
    time.sleep(2)
    #切换到电视台页面
    driver(resourceId="cn.xuexi.android:id/home_bottom_tab_button_contact").click()
    driver(text="联播频道").click()
    autoJob(tv="观看视频",sleep_time=20,click=False)
    driver(text="联播频道").click()
    
    news=None
    for v in driver(className='android.widget.TextView'):
        if "《新闻联播》" in v.text:
            news=v.text
            break
    driver(text=news).click()

    #100天后删除最早一天的记录
    text_list=np.array (all_of_list)
    
    if len(text_list)>2500:
        text_list = text_list[25:]
    #存储已看视频和文章
    np.save (savefile,text_list)
    
    print("正在观看新闻联播...")
    time.sleep(300)
    driver.press('back')
    print("观看视频结束.")

def check_subscribe():
    global subscribe_count
    for a in driver(className="android.widget.ImageView"): 
        if "订阅" in a.description and "已订阅" not in a.description:
            if subscribe_count<2:
                a.click()
                subscribe_count+=1
            else:
                return    
    else:
        os.system(drag_str)
        time.sleep(1)
        check_subscribe()

def subscribe():
    
    driver(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
    time.sleep(8)
    os.system(drag_str)
    time.sleep(2)
    os.system(drag_str)
    time.sleep(2)
    os.system(drag_str)
    time.sleep(3)
    driver.click(0.883*Width, 0.459*Height)
    time.sleep(3)   
    check_subscribe()


# In[6]:

if __name__ == '__main__':
    #自动打开学习强国
    #os.system('adb shell am start cn.xuexi.android/com.alibaba.android.rimet.biz.SplashActivity')
    #屏幕高度
    Height=driver.info['displayHeight']
    Width=driver.info['displayWidth']
    #切换adb输入法
    os.system('adb shell ime set com.android.adbkeyboard/.AdbIME')
    watch_local()
    read_articles()
    watch_video()
    # subscribe()
    print("任务完成")
    os.system("adb kill-server")
    print("adb连接断开")
    #熄灭屏幕
    # os.system('adb shell input keyevent 26')
   