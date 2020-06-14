# 映射与字典
# 映射的类型: 字典 字典包含哈希值和指向的对象
print('-------------------- 字典的定义 --------------------')
dict1 = {}
print(type(dict1))
dict2 = {'x': 1, 'y': 2}
dict2['z'] = 5
dict2['1'] = 's'
print(dict2)

# print('-------------------- 根据用户输入的月份和日期输出星座 --------------------')
# chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
# constellation = (u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座', u'摩羯座')
# month_days = (
#     (1, 21), (2, 20), (3, 21), (4, 21), (5, 22), (6, 22), (7, 23), (8, 24), (9, 24), (10, 24), (11, 23), (12, 22))
# cz_num = {}
# for i in chinese_zodiac:
#     cz_num[i] = 0
# constellation_num = {}
# for i in constellation:
#     constellation_num[i] = 0
# print(cz_num)
# print(constellation_num)
# while True:
#     input_year = int(input('请输入年份'))
#     input_month = int(input('请输入月份'))
#     input_day = int(input('请输入日期'))
#     num = 0
#     while month_days[num] < (input_month, input_day):
#         if input_month == 12 and input_day > 22:
#             break
#         num += 1
#     cz_num[chinese_zodiac[input_year % 12 - 4]] += 1
#     constellation_num[constellation[num]] += 1
#     # 输出生肖和星座的统计信息
#     for cz_key in cz_num.keys():
#         print('生肖%s有%d个' % (cz_key, cz_num[cz_key]))
#     for c_key in constellation_num.keys():
#         print('星座%s有%d个' % (c_key, constellation_num[c_key]))

# 列表推导式与字典推导式
print('-------------------- 1-10所有偶数的平方 --------------------')
a_list = []
for i in range(1, 11):
    if i % 2 == 0:
        a_list.append(i * i)
print(a_list)
b_list = [i * i for i in range(1, 11) if i % 2 == 0]
print(b_list)

print('-------------------- 字典推导式 --------------------')
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0
cz_num2 = {i: 0 for i in chinese_zodiac}
print(cz_num)
print(cz_num2)
