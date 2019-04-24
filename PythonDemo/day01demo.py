'''
使用变量保存数据并进行算术运算
'''
print('demo01')
a = 321
b = 123
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

'''
使用input函数输入
使用int*()进行类型转换
用占位符格式化输出字符串
'''
print('demo02')
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a,b,a+b))
print('%d - %d = %d' % (a,b,a-b))
print('%d * %d = %d' % (a,b,a*b))
print('%d / %d = %d' % (a,b,a/b))

'''
使用Type()检查变量的类型
'''
print('demo03')
a = 100
b = 12.34
c = 1 + 5j
d = 'Hello World!'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


