# xuexiqiangguo
超级简单的解放双手的学习强国脚本，旨在提高学习效率，妈妈再也不用担心我的学习（每天30分）～
### 2020/02/29 修改说明
已加入自动修改为adb输入法，感谢[liuzhijie443](https://github.com/liuzhijie443)提供的代码。
由于切换回的输入法因人而异，所以已经注释，[修改输入法教程](https://blog.csdn.net/weijinqian0/article/details/80390958)。
另外顺便上传windows批处理文件，将其与study.py放在一个目录即可，使用时直接运行autoStudy.bat，linux同理。
### 2020/02/06新增功能
- 评论，收藏，分享，本地
- 由于未充分了解uiautomator，看文章或视频时经常出异常，增添捕获异常，减少程序异常终止。
### 2020/02/06新增环境
由于adb input只能输入英文评论，并不友好，用户请[参考博客](https://blog.csdn.net/slimboy123/article/details/54140029)准备好相应环境。
（模拟器不知道为什么每次重启都要重新设置输入法，完全违背我快乐学习的初衷，如果觉得麻烦请自行注释。）
### 1.准备
1.安装adb
- Windows用户下载[adb资源](https://pan.baidu.com/s/16EpQvsGX19L9b6vZwRx7Aw)，安装教程自行百度。
- deepin用户
```
sudo apt-get install adb
```
2. 安装Python3
- 安装中(^_^)...
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
```
adb kill-server
adb start-server
```
- 运行脚本
```
python study.py
```
#### Android模拟器用户
- 通过adb连接模拟器，其中7555为mumu模拟器默认端口号，可以参考这篇文章[各模拟器默认端口号](https://www.cnblogs.com/HakunaMatata-/p/10609307.html)。模拟器用户由于模拟器加载视频慢，所以time.sleep(times)时间要长一些，才能有效观看。
```
adb kill-server
adb connect 127.0.0.1:7555
```
- 运行脚本
```
python study.py
```
### 3.问题
如果抛出异常，试试kill掉adb，重启试试。
### 4.后续
~~目前是看文章和视频，有24分，后续可能加入收藏，分享，评论，关注等功能，敬请关注。~~
功能应该就这样了，bug应该也就这样了...
