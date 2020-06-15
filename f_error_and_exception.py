# 错误和异常
print('-------------------- 错误和异常 --------------------')
print('-------------------- 错误不等于异常 --------------------')
print('--> 异常是在出现错误时采取正常控制流意外的动作')
print('--> 异常一般处理流程是: 检测到错误, 引发异常; 对异常进行捕获的操作')
print('--> try:')
print('--> \t<监控异常>')
print('--> except Exception[,reason]:')
print('--> \t<异常处理代码>')
print('--> finally:')
print('--> \t<无论异常是否发生都执行>')
# i = j
# print())
# a = '1ba'
# print(a[4])
# d = {'a': 1, 'b': 2}
# print(d['c'])


# try:
#     year = int(input('输入年份: '))
# except ValueError:
#     print('请输入数字')
# a = 123
# a.append()

# except (ValueError, AttributeError, KeyError):
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('0不能作为除数%s' % e)

try:
    print(1 / 'a')
except Exception as e:
    print('exception: %s' % e)

try:
    raise NameError('这是自己定义的一个error')
except NameError as e:
    print('错误信息%s' % e)

try:
    a = open('error.txt')
except Exception as e:
    print('error message: %s' % e)
finally:
    a.close()
