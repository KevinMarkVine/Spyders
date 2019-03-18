import re
import requests

url = 'http://photopin.com/free-photos/%E7%8C%AB'

wb_data = requests.get(url).text
#print(wb_data)

res = re.compile(r'src="(.+?.jpg)"')  #r表示原字符，编译好正则表达式对象
reg = re.findall(res, wb_data)
#print(reg)

num = 0
for i in reg:
    a = requests.get(i)
    f = open('/Users/kevinmarkvine/Documents/PycharmProjects/Spyders-1/Photos/%s.jpg'%num,'wb')
    f.write(a.content)
    f.close()
    num += 1
    print("第%s张图片下载完毕"%num)