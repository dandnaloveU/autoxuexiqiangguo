# xuexiqiangguo
想法与整体架构来自[IKeepMoving/xuexiqiangguo](https://github.com/IKeepMoving/xuexiqiangguo),我只是在此基础上做了新版本的适配和功能更新。
每天30分，除了答题所有功能已完成。
2020年10月5日更新：
	增加订阅功能，评论池随机评论。
### 1.准备
1.安装adb
- Windows用户下载[adb资源](https://pan.baidu.com/s/16EpQvsGX19L9b6vZwRx7Aw)，安装教程自行百度。
- deepin用户
```
sudo apt-get install adb
```
-MACOS用户
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
```
brew cask install android-platform-tools
```

2.安装Python3
自行百度
3.安装依赖包
```
pip install uiautomator
```
```
pip install numpy
```
### 2.运行
切换至项目目录，手机或者模拟器需在运行python脚本前自己打开学习强国。
#### 手机用户
- 打开手机的开发者模式，开启手机调试功能并允许通过adb安装应用，通过数据线让手机与电脑连接。本程序基于uiautomator编写，所以第一次会在手机安装两个应用，需要用户手动点击同意安装。
- 将isPhone设为1
```
isPhone=1
```
#### Android模拟器用户
- 通过adb连接模拟器，其中62001为夜神模拟器默认端口号，可以参考这篇文章[各模拟器默认端口号](https://www.cnblogs.com/HakunaMatata-/p/10609307.html)。模拟器用户由于模拟器加载视频慢，所以time.sleep(times)时间要长一些，才能有效观看。
-将isPhone设为0
```
isPhone=0
adb connect 127.0.0.1:62001
```
- 运行脚本
```
python study.py
```
### 3.问题
如果抛出异常，试试kill掉adb，重启试试。
声明：
个人非常不建议过度依赖自动工具，学习强国内有许多有营养的资料，本程序只适合工作繁忙的上班族在没有时间的时候救急。