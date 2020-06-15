import time

# 条件与循环

# 条件语句
x = 'abc'
a = 'abc'
b = 'ab'
if x == a:
    print('x 等于 a')
elif x == b:
    print('x 等于 b')
else:
    print('x 不等于 a, 也不等于b')
print('--------------------')
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
year = int(input('请输入出生年份'))
chinese_zodiac_single = str(chinese_zodiac[year % 12 - 4])
print(str(year) + '年对应的生肖是: ' + chinese_zodiac_single)
if chinese_zodiac_single == '鼠':
    print('鼠年行大运!')
elif chinese_zodiac_single == '牛':
    print('牛年行大运!')
elif chinese_zodiac_single == '虎':
    print('虎年行大运!')
elif chinese_zodiac_single == '兔':
    print('兔年行大运!')
elif chinese_zodiac_single == '龙':
    print('龙年行大运!')
elif chinese_zodiac_single == '蛇':
    print('蛇年行大运!')
elif chinese_zodiac_single == '马':
    print('马年行大运!')
elif chinese_zodiac_single == '羊':
    print('羊年行大运!')
elif chinese_zodiac_single == '猴':
    print('猴年行大运!')
elif chinese_zodiac_single == '鸡':
    print('鸡年行大运!')
elif chinese_zodiac_single == '狗':
    print('狗年行大运!')
else:
    print('猪年行大运!')
print('--------------------')
# for循环
for a in chinese_zodiac:
    print(a)
print('--------------------')
for b in range(4):
    print(b)
print('--------------------')
for c in range(3, 4):
    print(c)
print('--------------------')
for year in range(2010, 2020):
    print('%d年的生肖是: %s' % (year, chinese_zodiac[year % 12 - 4]))

# while循环
# 死循环
print('-------------------- 死循环 --------------------')
while True:
    print('1')
    break  # 不使用break即为死循环
print('-------------------- 从1数到3 --------------------')
num = 1
while True:
    print(num)
    num = num + 1
    if num >= 4:
        break
print('-------------------- 使用continue打印10到20的奇数 --------------------')
num = 9
while True:
    num = num + 1
    if num >= 20:
        break
    else:
        if num % 2 == 0:
            continue
        else:
            print(num)
            time.sleep(1)
print('-------------------- 根据输入月份和日期判断星座(for中的嵌套if) --------------------')
constellation = (u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座', u'摩羯座')
month_days = (
    (1, 21), (2, 20), (3, 21), (4, 21), (5, 22), (6, 22), (7, 23), (8, 24), (9, 24), (10, 24), (11, 23), (12, 22))
input_month = int(input('请输入月份'))
input_day = int(input('请输入日期'))
for m_d in range(len(month_days)):
    if month_days[m_d] >= (input_month, input_day):
        print(constellation[m_d])
        break
    elif input_month == 12 and input_day > 22:
        print(constellation[0])
        break
print('-------------------- 根据输入月份和日期判断星座(while中的if嵌套) --------------------')
