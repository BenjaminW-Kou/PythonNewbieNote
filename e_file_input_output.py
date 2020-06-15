# 文件和输入输出
# 文件的内建函数
# 内建函数 open - 打开文件; read - 输入; readline - 输入一行; seek - 文件内移动; write - 输出; close - 关闭文件
# 将小说的主要人物记录在文件中
# 新建
# file_s = open('三国演义.txt', 'w')
# file_s.write('诸葛亮')
# file_s.close()

print('-------------------- 读取 --------------------')
# 读取
file_r = open('三国演义.txt')
print(file_r.read())
file_r.close()

print('-------------------- 增加 --------------------')
# 增加
# file_s2 = open('三国演义.txt', 'a')
# file_s2.write('刘备')
# file_s2.close()

print('-------------------- 读取2 --------------------')
# 读取
file_r2 = open('三国演义.txt')
print(file_r2.readline())
file_r2.close()

print('-------------------- 读取3 --------------------')
# 读取
file_r3 = open('三国演义.txt')
print(file_r3.readline())
file_r3.close()

print('-------------------- 读取4 --------------------')
# 读取
file_r4 = open('三国演义.txt')
for line in file_r4.readlines():
    print(line)
file_r4.close()

print('-------------------- 读取5 --------------------')
# 读取
file_r5 = open('三国演义.txt')
print(file_r5.tell())
print(file_r5.read(1))
file_r5.seek(0)
print(file_r5.tell())
print(file_r5.read(1))
print(file_r5.read(1))
# 第一个参数代表偏移的位置, 第二个参数 0表示从文件开头偏移, 1表示从当前位置开始偏移, 2表示从文件结尾偏移
file_r5.seek(1, 0)
print(file_r5.tell())
file_r5.close()
