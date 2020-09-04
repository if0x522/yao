#!/usr/bin/python3

import requests
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendemail(ho,mi,te1,te2,j):
	from_addr = '3232584646@qq.com'
	passwd = 'tvxvtmepkwkrdade'
	to_addr = '3064782929@qq.com'
	smtp_server = 'smtp.qq.com'
	if(j == -1):
		str = '填报失败。时间：' + ho + ':' + mi + '温度:' + te1 + '.' + te2
	else:
		str = '填报成功。时间：' + ho + ':' + mi + '温度:' + te1 + '.' + te2
	msg = MIMEText(str,'plain','utf-8')
	msg['from'] = Header(from_addr)
	msg['To'] = Header(to_addr)
	msg['Subject'] = Header('填报完成')
	server = smtplib.SMTP_SSL(smtp_server)
	server.connect(smtp_server,465)
	server.login(from_addr,passwd)
	server.sendmail(from_addr,to_addr,msg.as_string())
	server.quit()

def loadup():
	Time = time.localtime(time.time())
	ho = Time[3]
	mi = Time[4]
	te1 = 36
	te2 = random.randint(2,8)
	
	#打包数据包，数据均来自抓包
	header = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.4.8','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Referer':'http://219.246.21.225/LzcuXG/SPCP/Web/Temperature/StuTemperatureInfo','Accept-Encoding':'gzip,deflate','Accept-Language':'zh-CN,en-US;q=0.8'}
	cookie = {'ASP.NET_SessionId':'ixwwtqnul5bnlgi40yz3vnsv','CenterSoftWeb':'14B64F89DC93D38AD0A5108DF5B75EA0BB8950AC5C3C5CA5F557C461DEF97E1A58B2D45D1696FCFF63E5188F58F3022ECD46B5DF44F3656A56405394D3D01FDF1A94666D73ECE170AC3A88D3A33E490F36442A7902B4D38DC6AB5AC8C3F0E01FA8651EF02C1E0E2649B61540C5129A2D39C248857337483E85FA13213721ED4B6DE9FA132F94EAE647629F5DE4329DEC9C334CBA6C9C8A4E181594124CB08678FD0FD2B2867C6A9EA7886102AB84500E4C6C310E2DDB5BD8981034E6AFA43C4C'}
	Data = {'TimeNowHour':ho,'TimeNowMinute':mi,'Temper1':te1,'Temper2':te2,'ReSubmiteFlag':'05e9e185-8172-4876-a267-ad626658b76c'}
	URL = 'http://219.246.21.225/LzcuXG/SPCP/Web/Temperature/StuTemperatureInfo'
	R = requests.post(URL,data=Data,headers=header,cookies=cookie)
	htm = R.text
	j = htm.find('填报成功')
	if j == -1:
		print('填报失败')
		sendemail(ho,mi,te1,te2,j)
	else:
		print('填报成功')
		sendemail(ho,mi,te1,te2,j)


#tvxvtmepkwkrdade



while(1):
	Time = time.localtime(time.time())
	ho = Time[3]
	mi = Time[4]
	if ho == 5:
		i = 3
		while(i):
			sl = random.randint(5,20)
			sle = sl * 60
			time.sleep(sle)
			loadup()
			time.sleep(4*60*60)
			i = i-1
	time.sleep(60*60)



