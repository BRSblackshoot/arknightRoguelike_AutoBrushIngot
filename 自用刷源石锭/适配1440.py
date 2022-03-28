# -*- encoding=utf8 -*-
#1440*810
import os,time
import cv2

def connect():
    try:
        os.system('adb connect 127.0.0.1:7555')
    except:
        print('连接失败')

def click(list):
    os.system('adb shell input tap %s %s' % (list[0], list[1]))

def exists(cunzai):
    if cunzai!=False:
        return True
    else:
        return False

def swipe(list1,list2,duration=500):
    os.system("adb shell input swipe %s %s %s %s %s"%(list1[0],list1[1],list2[0],list2[1],duration))

def screenshot():
    path = os.path.abspath('.') + '\images'
    os.system('adb shell screencap /data/screen.png')
    os.system('adb pull /data/screen.png %s' % path)

def Image_to_position(image, m = 0):
    screenshot()
    image_path = 'images/' + str(image)
    screen = cv2.imread('images/screen.png', 1)
    Image_to_position = cv2.imread(image_path, 1)
    methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED]
    image_x, image_y = Image_to_position.shape[:2]
    result = cv2.matchTemplate(screen, Image_to_position, methods[m])
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(max_val)
    if max_val > 0.9:
        global center
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        print(center)
        # return center
        return center[0], center[1]
    else:
        return False




a=0#运行步数
b=0#判断关卡搜索次数
c=0#投资次数计数
def panduanguoguan():
    while not exists(Image_to_position(r"tpl1641989217172.png")):#判断过关
        time.sleep(4.0)#没有成功通过就等4秒，然后继续循环找成功通过
    else:
        time.sleep(2.0)#找到了之后，为了防止在“成功通关”这四个字从画面左边飞到画面内的瞬间识别到并立刻进行点击而设置的一个等待时间。（因为计算机执行）
    click((1000,490))#识别到了点击一下
    time.sleep(1.0)
    while not exists(Image_to_position(r"tpl1641989331329.png")):#判断有没有这个图片
        swipe((670,500),(570,500))#判断没有，就自右往左滑动屏幕，移到右边，移完回去继续判断图片
    else:
        click(Image_to_position(r"tpl1641989331329.png"))#判断到了就点它
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641989346223.png"))
    time.sleep(1.0)
def likai():
    click((45,30))
    time.sleep(1.0)
#第二次探索如果卡主，可以适当将这里的time.sleep时间增加一点，比如time.sleep(3.0)，time.sleep可以理解为等待一段时间的意思
    click(Image_to_position(r"tpl1641990570636.png"))
    time.sleep(1.0)
#这个对象likai()里的这些time.sleep时间都可以适当改一下，改到适合自己模拟器运行加载速度的等待时间
    click(Image_to_position(r"tpl1641990587770.png"))
    time.sleep(3.0)
    click((700,730))#等一段时间点击画面进入下一个结算的界面
    time.sleep(3.0)
    click((700,730))#等一段时间点击画面进入下一个结算的界面，点完这次应该就会回到肉鸽主菜单
    time.sleep(3.0)#对，就是这个，靠在一起了应该可以看到吧
    click((785,725))#有时候会解锁一些藏品，导致卡住，所以就加一步
def kaishi():
    click((1300,650))
#可以回到肉鸽主界面但不会进行下一次探索的，请修改likai()对象里面最下面的那个time.sleep时间'''
    while not exists(Image_to_position(r"tpl1641990883595.png")):
#精二高级的山比较稳定过关，所以选了这个分队'''
        swipe((670,500),(470,500))
    else:
        click(Image_to_position(r"tpl1641990883595.png"))
#有需要的就把这两个突击战术分队的图片换成自己想要的分队吧，用左侧Airtest辅助窗里的功能就可以截图生成自己的代码了。'''
        click(Image_to_position(r"tpl1641991004571.png"))
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641991034647.png"))
    click(Image_to_position(r"tpl1641991004571.png"))
    time.sleep(2.0)
    click((390,600))#点击第一张招募券下面的招募按钮的坐标。
    time.sleep(1.0)
    if exists(Image_to_position(r"tpl1641991518242.png")):#判断画面内有没有山，有就选，没有就执行else:后面的内容
        click(Image_to_position(r"tpl1641991518242.png"))
        time.sleep(2.0)
        click((1250,750))
        time.sleep(3.0)
    else:#上面if是选择自己的山，else下面的部分是选择用助战
        click((1220,30))
        while not exists(Image_to_position(r"tpl1641991335442.png")):#因为有时候刷新到的山在第三列，招募按钮在右边画面外，所以设置的一个判断。
            click((1300,30))
            while not exists(Image_to_position(r"tpl1641991147628.png")):
                click((1300,30))
            else:
                pass
        else:
            click(Image_to_position(r"tpl1641991335442.png" ))
        time.sleep(1.0)
        click(Image_to_position(r"tpl1641991373517.png"))
        time.sleep(2.0)
    while exists(Image_to_position(r"tpl1641991518242.png")):#判断画面是否在那个招到了干员的画面。
        time.sleep(1.0)
    else:
        time.sleep(1.0)
    click((700,730))#上面判断到了在那个画面再点击一下屏幕进入下一步。
    time.sleep(1.0)
    click((700,600))#点击第二张招募券下面的招募按钮的坐标。
    click(Image_to_position(r"tpl1641991636323.png"))
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641991650485.png"))
    time.sleep(1.0)
    click((1000,600))#点击第三张招募券下面的招募按钮的坐标。
    click(Image_to_position(r"tpl1641991636323.png"))
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641991650485.png"))
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641991718574.png"))
    time.sleep(4.0)
    b=0
def xuanren():
    if exists(Image_to_position(r"tpl1641994682261.png")):#判断行动选干员界面有没有山
        pass#有就pass不管
    else:
        click((250,190))#没有就执行这段选山和选择技能。
        time.sleep(1.0)
        click((680,160))
        time.sleep(1.0)
        click((200,600))
        time.sleep(1.0)
        click((1270,760))
def shijian():
    click(Image_to_position(r"tpl1641987478502.png"))
    time.sleep(4.0)
    click((1190,460))#这个点击的坐标可以在只有一个或两个选项的时候点击到最下面选项的位置。
    time.sleep(3.0)
    if exists(Image_to_position(r"tpl1642038786944.png")):#这里是针对不期而遇里有三个选项的情况进行确认。
        click(Image_to_position(r"tpl1642038786944.png"))
    else:
        click((1190,460))
    time.sleep(2.0)
    click(Image_to_position(r"tpl1641987560872.png") )
    time.sleep(4.0)
    click(Image_to_position(r"tpl1641987578489.png"))
    time.sleep(3.0)
    b=0
def buqieryu():
    click(Image_to_position(r"tpl1642165550078.png"))
    shijian()
def mujianyuxing():
    click(Image_to_position(r"tpl1642172804442.png"))
    shijian()
def xunshouxiaowu():
    click(Image_to_position(r"tpl1641987600343.png"))
    time.sleep(1.0)
    click((1290,600))
    time.sleep(1.0)
    xuanren()
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641988492692.png"))
    time.sleep(8.0)
    click((1240,60))#点击加速
    time.sleep(3.0)
    swipe((1390,760),(1180,400))#拖干员到位置，duration是拖动过程的时间，可以自行设定适当的时间防止模拟器卡顿没下到干员，单位秒，默认是0.5秒的，有人反映下干员太快就加了这个。
    time.sleep(1.0)
    swipe((1180,400),(1380,400))#设置朝向，这里也可以加duration=来设定拖动时间，招着上面的样子写出来代码就好。
    time.sleep(5.0)
    click((1100,410))#点山
    time.sleep(2.0)#如果连点山和开技能之间都卡了，那这里的等待时间自行增加吧。
    click((1000,490))#开山技能
    panduanguoguan()
    b=0
def lipaoxiaodui():#注释参考xunshouxiaowu()里的注释
    click(Image_to_position(r"tpl1641991796991.png"))
    time.sleep(1.0)
    click((1290,600))
    time.sleep(1.0)
    xuanren()
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641988492692.png"))
    time.sleep(8.0)
    click((1240,60))#点击加速
    time.sleep(1.0)
    swipe((1390,760),(575,386))#拖干员到位置
    time.sleep(1.0)
    swipe((560,382),(1380,400))#设置朝向
    time.sleep(4.0)
    click((455,364))#点山
    time.sleep(2.0)
    click((1000,490))#开山技能
    panduanguoguan()
    b=0
def yiwai():#注释参考xunshouxiaowu()里的注释
    click(Image_to_position(r"tpl1641998962031.png"))
    time.sleep(1.0)
    click((1290,600))
    time.sleep(1.0)
    xuanren()
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641988492692.png"))
    time.sleep(8.0)
    click((1240,60))#点击加速
    time.sleep(3.0)
    swipe((1390,760),(806,370))#拖干员到位置
    time.sleep(1.0)
    swipe((806,370),(1380,400))#设置朝向
    time.sleep(1.0)
    time.sleep(4.0)
    click((715,363))#点山
    time.sleep(2.0)
    click((1000,490))#开山技能
    panduanguoguan()
    b=0
def yuchongweiban():#注释参考xunshouxiaowu()里的注释
    click(Image_to_position(r"tpl1641994030492.png"))
    time.sleep(1.0)
    click((1290,600))
    time.sleep(1.0)
    xuanren()
    time.sleep(1.0)
    click(Image_to_position(r"tpl1641988492692.png"))
    time.sleep(8.0)
    click((1240,60))#点击加速
    time.sleep(1.0)
    swipe((1390,760),(667,432))#拖干员到位置
    time.sleep(1.0)
    swipe((667,432),(1380,400))#设置朝向
    time.sleep(4.0)
    click((575,411))#点山
    time.sleep(1.0)
    click((930,450))#开山技能
    panduanguoguan()
    b=0
def shandian():
    time.sleep(1.0)
    click((1290,600))
    time.sleep(1.0)
    c=0
    if exists(Image_to_position(r"tpl1641989654147.png")):
        click(Image_to_position(r"tpl1641989721200.png"))
        time.sleep(1.0)
        click(Image_to_position(r"tpl1641989745261.png"))
        time.sleep(1.0)
        while c<15:#为解决投完了身上的源石锭还没到投资受限的情况而设置的判断（运气好试过几次17颗源石锭投完了还能继续投就卡住了的情况。）
            if not exists(Image_to_position(r"tpl1641989989616.png")):
                # 点一次判断一次太麻烦 我直接点10次再说
                for i in range(10):
                    click((1100,560))
                    c+=1
                    # for循环非常快 虽然有adb命令的延迟 还是给个手动延迟
                    time.sleep(0.2)
            else:
                c=15
                # time.sleep(1.0)
                # c=5
        else:
            c=0
            likai()
    else:
        time.sleep(2.0)
        likai()
    kaishi()
    b=0
def panduanguanqia():
    time.sleep(2.0)
    
    if exists(Image_to_position(r"tpl1642045891855.png")):
        click(Image_to_position(r"tpl1642045891855.png"))
        shandian()
    elif exists(Image_to_position(r"tpl1642165495398.png")):
        buqieryu()
    elif exists(Image_to_position(r"tpl1641987600343.png")):
        xunshouxiaowu()
    elif exists(Image_to_position(r"tpl1641991796991.png")):
        lipaoxiaodui()
    elif exists(Image_to_position(r"tpl1641998962031.png")):
        yiwai()
    elif exists(Image_to_position(r"tpl1641994030492.png")):
        yuchongweiban()
    elif exists(Image_to_position(r"tpl1642172804442.png")):
        mujianyuxing()
    elif b>1:#由于识别图片，经常搜索不到不期而遇，这里是判断关卡两次没搜索到后运行的代码。
        click((900,360))#点击固定的几个点
        time.sleep(1.0)
        click((900,120))
        time.sleep(1.0)
        click((900,440))
        time.sleep(1.0)
        click((900,200))
        time.sleep(1.0)
        click((900,280))
        if exists(Image_to_position(r"tpl1642143362809.png")):#判断最终选择了什么关卡，然后执行相应的对象。由于战斗分支通常不会因搜索不到而触发反复判断的BUG，所以这里不对战斗关卡分支的图片进行判断。
            shijian()
        elif exists(Image_to_position(r"tpl1642172966906.png")):
            shijian() 
        elif exists(Image_to_position(r"tpl1642255403039.png")):
            shandian()
        else:
            pass

if __name__ == '__main__':
    connect()
    kaishi()#脚本从这里开始运行
    while a<300:
        panduanguanqia()
        a+=1
        b+=1
        print("=============\n完成第%s次\n当前系统时间%s\n ==========="%(a,time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))

