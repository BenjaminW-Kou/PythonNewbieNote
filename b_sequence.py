# 序列 - 指它的成员都是有序排列, 并且可以通过下标偏移量访问到它的一个或几个成员
# 字符串("abcde")、列表[0,"abcde"]、元组("abcde","fghij")三种类型都属于序列
# 序列的基本操作: 成员操作符(in; not in), 连接操作符(+), 重复操作符(*), 切片操作符([:])

# 切片操作符([:])
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
print(chinese_zodiac[6:9])
print(chinese_zodiac[6:])
print(chinese_zodiac[6:-1])
print(chinese_zodiac[-1])

# 记录生肖, 根据年份来判断生肖
year = 2020
print(chinese_zodiac[year % 12 - 4])

# 成员操作符(in; not in)
dog = '狗'
print(dog in chinese_zodiac)
print(dog not in chinese_zodiac)

# 连接操作符(+)
print(chinese_zodiac + dog)
print(dog + '大象')

# 重复操作符
print(chinese_zodiac * 3)
print(dog * 4)

# 元组
# u表示Unicode
# 根据月份判断星座
constellation = (u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座', u'摩羯座')
month_days = (
    (1, 21), (2, 20), (3, 21), (4, 21), (5, 22), (6, 22), (7, 23), (8, 24), (9, 24), (10, 24), (11, 23), (12, 22))
(month, day) = (4, 18)
month_day = list(filter(lambda x: x <= (month, day), month_days))
month_day_len = len(month_day) % 12 - 1
print(constellation[month_day_len])

# 列表
a_list = [0, 'abc', 'def']
print(a_list)
a_list.append('g')
print(a_list)
a_list.remove(0)
print(a_list)
