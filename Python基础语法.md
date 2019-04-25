## Python基础语法
### 分支结构
- if语句
    `if`,`elif`,`else`关键字
    与C/C++，Java等语言不同的是，Python中没有用花括号来构造代码块而是使用缩进的方式来设置代码的结构层次。

### 循环结构
- **for-in循环**  
```python
        sum = 0
        for x in range(2, 101, 2):
	        sum += x
        print(sum)
```
- **while循环** 

```python
        import random
        
        answer = random.randint(1, 100)
        counter = 0
        while True:
	        counter += 1
	        number = int(input('请输入: '))
	        if number < answer:
		        print('大一点')
	        elif number > answer:
	        	print('小一点')
	        else:
	        	print('恭喜你猜对了!')
	    	    break
        print('你总共猜了%d次' % counter)
        if counter > 7:
	        print('你的智商余额明显不足')
```

## Python函数
- **定义函数**
        在Python中用`def`关键字来定义函数，函数执行完成之后用`return`关键字返回结果
- **函数的参数**
        在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
        Python并不需要像其他语言那样支持`函数的重载`  
        `定义默认参数必须指向不变对象`

```python
      from random import randint


        def roll_dice(n=2):
        """
        摇色子
        
        :param n: 色子的个数
        :return: n颗色子点数之和
        """
	total = 0
	for _ in range(n):
		total += randint(1, 6)
	return total


        def add(a=0, b=0, c=0):
	return a + b + c


        # 如果没有指定参数那么使用默认值摇两颗色子
        print(roll_dice())
        # 摇三颗色子
        print(roll_dice(3))
        print(add())
        print(add(1))
        print(add(1, 2))
        print(add(1, 2, 3))
        # 传递参数时可以不按照设定的顺序进行传递
        print(add(c=50, a=100, b=200))  
```
- **模块**
由于Python没有`函数重载`的概念，同名函数就会很尴尬，因为后面的会覆盖前面定义的。
Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过`import`关键字导入指定的模块就可以区分到底要使用的是哪个模块中的函数


