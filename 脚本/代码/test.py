#!/usr/bin/python3
#整体思路：
#初始化程序创建socket服务器端，创建两个子线程，一个负责图像传输，一个负责接收指令码
#主线程将接收到的指令码解析到不同的功能驱动函数


import socket 				#导入socket：指令码传输
import threading      		#导入threading：多线程
import os  					#导入os：调用系统命令
import time 				#导入time：睡眠定时
import RPi.GPIO as GPIO 	#树莓派GPIO导入：硬件控制


def main(): 				#定义主函数
    initall() 				#调用系统初始化函数
    xuanze() 				#调用指令码分配函数


def initall(): 				#定义初始化函数
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 			#创建tcp套接字
    s.bind((host,port))  										#绑定本地地址端口
    s.listen(1) 												#等待连接，最大连接数量限制为1
    c,addr=s.accept()
    t1 = threading.Thread(target=tuchuan,args=()) 				#创建子线程，子线程调用图传函数
    t2 = threading.Thread(target=datarecv,args=()) 				#创建子线程，子线程循环接收指令码
    t1.setDaemon(True)  										#子线程设置为守护线程
    t2.setDaemon(True)
    t1.start() 													#开启子线程
    t2.start()
    GPIO.setmode(GPIO.BCM) 										#设置树莓派GPIO口编码方式为BCM
    GPIO.setup(2,GPIO.OUT)										#分别设置GPIO：2、3、4、5、6、7、8、9、10、11、为输出模式
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(5,GPIO.OUT)
    GPIO.setup(6,GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(8,GPIO.OUT)
    GPIO.setup(9,GPIO.OUT)
    GPIO.setup(10,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)

def tuchuan():   				#定义图传函数
  #  print("start done")
    os.system('cd ./mjpg;./mjpg_streamer -i "./input_raspicam.so" -o "./output_http.so -w ./www"') 		#调用系统指令开启mjpg图传程序

def datarecv():  				#定义数据接收函数
#    c,addr=s.accept() 			#接受socket连接
  #  print(addr) 				#打印连接端ip地址
    while i:  					#进入接收循环，如果接收标志值为真，则始终循环接受，为假则结束接收
        data=c.recv(1024)  		#接收来自socket连接的数据，最大接收数据长度为1024
        num=int(data) 			#将接收到的字节数组转换为整型数据
  #      print(num)
        if num==100: 			#判断如果接收到的数据值为100则将接收标志值设置为假，“100为设置断开连接标志值”
            car_stop()
            i=0				

            
    s.close() 					#当接收停止时关闭连接


def xuanze():
    while i:
        gongneng(num)
        time.sleep(zq)
#	gongneng(num)
 #       time.sleep(zq) 			#延时一个舵机脉冲周期

#def gongneng(i): 				#定义功能选择函数，
"""
	不同的指令码对应不同的功能，详细对照为：
		21：小车向前进
		22：小车后退
		23：小车左转
		24：小车右转
		111：机械臂第一级舵机顺转
		112：机械臂第一级舵机逆转
		121：机械臂第二级舵机顺转
		······
		0：停止所有动作
"""
def gongneng(i):
    if i==21:
        car_qian()
    elif i==22:
        car_hou()
    elif i==23:
        car_zuo()
    elif i==24:
        car_you()
    elif i==111:
        dj1z()
    elif i==112:
        dj1y()
    elif i==121:
        dj2z()
    elif i==122:
        dj2y()
    elif i==131:
        dj3z()
    elif i==132:
        dj3y()
    elif i==141:
        dj4z()
    elif i==142:
        dj4y()
    elif i==151:
        dj5z()
    elif i==152:
        dj5y()
    elif i==161:
        dj6z()
    elif i==162:
        dj6y()
    elif i==0:
        car_stop()


"""
机械臂各级驱动，GPIO2~7分别对应机械臂六个舵机，
通过不同时常的脉冲，设置相对关节转向，具体脉冲市时长取决于舵机型号和目标角度
这里全部设置满舵旋转到预期位置认为停止工作
"""

def dj1z(): 					
    GPIO.output(2,GPIO.HIGH)
    time.sleep(zmd)
    GPIO.output(2,GPIO.LOW)

def dj2z():
    GPIO.output(3,GPIO.HIGH)
    time.sleep(zmd)
    GPIO.output(3,GPIO.LOW)

def dj3z():
    GPIO.output(4,GPIO.HIGH)
    time.sleep(zmd)
    GPIO.output(4,GPIO.LOW)

def dj4z():
    GPIO.output(5,GPIO.HIGH)
    time.sleep(zmd)
    GPIO.output(5,GPIO.LOW)

def dj5z():
    GPIO.output(6,GPIO.HIGH)
    time.sleep(zmd)
    GPIO.output(6,GPIO.LOW)

def dj6z():
    GPIO.output(7,GPIO.HIGH)
    time.sleep(zmd)
    GPIO.output(7,GPIO.LOW)

def dj1y():
    GPIO.output(2,GPIO.HIGH)
    time.sleep(ymd)
    GPIO.output(2,GPIO.LOW)

def dj2y():
    GPIO.output(3,GPIO.HIGH)
    time.sleep(ymd)
    GPIO.output(3,GPIO.LOW)

def dj3y():
    GPIO.output(4,GPIO.HIGH)
    time.sleep(ymd)
    GPIO.output(4,GPIO.LOW)

def dj4y():
    GPIO.output(5,GPIO.HIGH)
    time.sleep(ymd)
    GPIO.output(5,GPIO.LOW)

def dj5y():
    GPIO.output(6,GPIO.HIGH)
    time.sleep(ymd)
    GPIO.output(6,GPIO.LOW)

def dj6y():
    GPIO.output(7,GPIO.HIGH)
    time.sleep(ymd)
    GPIO.output(7,GPIO.LOW)

"""
小车前后左右行动驱动，通过GPIO8~11控制两个电机的旋转及方向，
8，9控制一个电机，10，11控制一个电机
通过两个电机的正反转控制小车的前后左右的运动
"""

def car_qian():
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(10,GPIO.HIGH)
    GPIO.output(9,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)

def car_hou():
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)

def car_zuo():
    GPIO.output(8,GPIO.HIGH)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(9,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)

def car_you():
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(10,GPIO.HIGH)
    GPIO.output(8,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)

def car_stop(): 					#停止函数，将所有用到的GPIO口全部拉低，终止所有运动
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)
    GPIO.output(4,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(8,GPIO.LOW)	
    GPIO.output(9,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)


zmd=0.0005 						#定义舵机左满舵脉冲时长
ymd=0.0025						#定义舵机右满舵脉冲时长
zq=0.015						#定义舵机脉冲长度
host = '192.168.100.8' 		#本地ip地址
port = 60000 					#本地接收端口
i=1 							#设置接收标志值，初始值为真
num=0 							#初始指令码
main()   						#调用主函数

