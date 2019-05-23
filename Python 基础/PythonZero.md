# Python 零基础入门

![Python](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=chris-ried-512801-unsplash.jpg)

Photo by [Chris Ried](https://unsplash.com/photos/ieic5Tq8YMk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/python?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Python 是一种易于学习又功能强大的编程语言。它提供了高效的高级数据结构，还有简单有效的面向对象编程。Python 优雅的语法和动态类型，以及解释型语言的本质，使它成为多数平台上写脚本和快速开发应用的理想语言。

Python 解释器及丰富的标准库以源码或机器码的形式提供，可以到 Python 官网 [https://www.python.org/](https://www.python.org/) 免费获取适用于各个主要系统平台的版本，并可自由地分发。这个网站还包含许多免费第三方 Python 模块、程序和工具以及附加文档的发布页面或链接。

Python 解释器易于扩展，可以使用 C 或 C++（或者其他可以通过 C 调用的语言）扩展新的功能和数据类型。Python 也可用于可定制化软件中的扩展程序语言。

如果你经常在电脑上工作，总会有些任务会想让它自动化。比如，对一大堆文本文件进行查找替换，对很多照片文件按照比较复杂的规则重命名并放入不同的文件夹。也可能你想写一个小型的数据库应用，一个特定的界面应用，或者一个简单的游戏。

如果你是专业的软件开发人员，你可能需要编写一些 C/C++/Java 库，但总觉得通常的开发的流程（编写、编译、测试、再次编译等）太慢了。可能给这样的库写一组测试，就是很麻烦的工作了。或许你写了个软件，可以支持插件扩展语言，但你不想为了自己这一个应用，专门设计和实现一种新语言了。

那么，Python 正好能满足你的需要。

对于这些任务，你也可以写 Unix 脚本或者 Windows 批处理完成，但是 shell 脚本最擅长移动文件和替换文本，并不适合 GUI 界面或者游戏开发。你可以写一个 C/C++/Java 程序，但是可能第一版本的草稿都要很长的开发时间。Python 的使用则更加简单，可以在 Windows，Mac OS X，以及 Unix 操作系统上使用，而且可以帮你更快地完成工作。

Python 很容易使用，但它是一种真正的编程语言，提供了很多数据结构，也支持大型程序，远超 shell 脚本或批处理文件的功能。Python 还提供比 C 语言更多的错误检查，而且作为一种 “超高级语言”，它有高级的内置数据类型，比如灵活的数组和字典。正因为这些更加通用的数据类型，Python 能够应付更多的问题，超过 Awk 甚至 Perl，而且很多东西在 Python 中至少和那些语言同样简单。

Python 允许你划分程序模块，在其他的 Python 程序中重用。它内置了很多的标准模块，你可以在此基础上开发程序——也可以作为例子，开始学习 Python 编程。例如，文件输入输出，系统调用，套接字，甚至图形界面接口工作包比如 Tk 。

Python 是一种解释型语言，在程序开发阶段可以为你节省大量时间，因为不需要编译和链接。解释器可以交互式使用，这样就可以方便地尝试语言特性，写一些一次性的程序，或者在自底向上的程序开发中测试功能。它也是一个顺手的桌面计算器。

Python 程序的书写是紧凑而易读的。Python 代码通常比同样功能的 C，C++，Java 代码要短很多，原因列举如下：

1. 高级数据类型允许在一个表达式中表示复杂的操作；
1. 代码块的划分是按照缩进而不是成对的花括号；
1. 不需要预先定义变量或参数。

Python 是 “可扩展的”：如果你知道怎么写 C 语言程序，就能很容易地给解释器添加新的内置函数或模块，不论是让关键的程序以最高速度运行，还是把 Python 程序链接到只提供预编译程序的库（比如硬件相关的图形库）。一旦你真正链接上了，就能在 Python 解释器中扩展或者控制 C 语言编写的应用了。

顺便提一下，这种语言的名字（Python 意为 “蟒蛇”）来自于 BBC 节目 “Monty Python 的飞行马戏团”，而与爬行动物没有关系。在文档中用 Monty Python 来开玩笑不只是可以的，还是推荐的！

现在你已经对 Python 跃跃欲试了，想要深入了解一些细节了。因为学习语言的最佳方式是使用它，本教程邀请你一边阅读，一边在 Python 解释器中玩耍。

## 使用 Python 解释器

### 调用解释器

在 Python 可用的机器上，Python 解释器通常放在 `/usr/local/bin/python3.7` ; 把 `/usr/local/bin` 放到你 Unix shell 的搜索路径当中 , 这样就能键入命令:

```sh
python3.7
```

就能运行了。

安装时可以选择安装目录，所以解释器也可能在别的地方；可以问问你身边的 Python 大牛，或者你的系统管理员。（比如 `/usr/local/python` 也是比较常用的备选路径）

在 Windows 机器上， Python 安装通常放在 `C:\Python37` 中，尽管你可以在运行安装程序时更改此设置。要将此目录添加到路径中，可以将以下命令键入 [命令提示符窗口](https://docs.python.org/zh-cn/3/faq/windows.html#faq-run-program-under-windows):

```sh
set path=%path%;C:\python37
```

在主提示符中输入文件结束字符（在 Unix 系统中是 `Control-D`，Windows 系统中是 `Control-Z`）就退出解释器并返回退出状态为 0。如果这样不管用，你还可以写这个命令退出：`quit()`。

解释器的行编辑功能也包括交互式编辑，在支持 readline 的系统中，可以回看历史命令，也有 `Tab` 代码补全功能。要想快速检查是否支持行编辑，在出现提示符后，按键盘 `Control-P`。如果它 “哔” 了一声，它就是支持行编辑的；关于按键的详细介绍请看附录 [交互式编辑和编辑历史](https://docs.python.org/zh-cn/3/tutorial/interactive.html#tut-interacting)。如果什么都没发生，或者显示出 `^P`，那么就不支持行编辑功能；你只能用退格（`Backspace`）键从当前行中删除字符。

解释器运行的时候有点像 Unix 命令行：在一个标准输入 tty 设备上调用，它能交互式地读取和执行命令；调用时提供文件名参数，或者有个文件重定向到标准输入的话，它就会读取和执行文件中的 *脚本*。

另一种启动解释器的方式是 `python -c command [arg] ...`，其中 *command* 要换成想执行的指令，就像命令行的 [`-c`](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-c) 选项。由于 Python 代码中经常会包含对终端来说比较特殊的字符，通常情况下都建议用英文单引号把 *command* 括起来。

有些 Python 模块也可以作为脚本使用。可以这样输入：`python -m module [arg] ...`，这会执行 *module* 的源文件，就跟你在命令行把路径写全了一样。

在运行脚本的时候，有时可能也会需要在运行后进入交互模式。这种时候在文件参数前，加上选项 [`-i`](https://docs.python.org/zh-cn/3/using/cmdline.html#cmdoption-i) 就可以了。

关于所有的命令行选项，请参考 [命令行与环境](https://docs.python.org/zh-cn/3/using/cmdline.html#using-on-general)。

### 交互模式

在终端（tty）输入并执行指令时，我们说解释器是运行在 *交互模式（interactive mode）*。在这种模式中，它会显示 *主提示符（primary prompt）*，提示输入下一条指令，通常用三个大于号（`>>>`）表示；连续输入行的时候，它会显示 *次要提示符*，默认是三个点（`...`）。进入解释器时，它会先显示欢迎信息、版本信息、版权声明，然后就会出现提示符：

```sh
$ python3.7
Python 3.7 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

多行指令需要在连续的多行中输入。比如，以 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 为例：

```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

有关交互模式的更多内容，请参考 [交互模式](https://docs.python.org/zh-cn/3/tutorial/appendix.html#tut-interac)。

## 解释器的运行环境 [](https://docs.python.org/zh-cn/3/tutorial/interpreter.html#the-interpreter-and-its-environment "永久链接至标题")

### 源文件的字符编码

默认情况下，Python 源码文件以 UTF-8 编码方式处理。在这种编码方式中，世界上大多数语言的字符都可以同时用于字符串字面值、变量或函数名称以及注释中——尽管标准库中只用常规的 ASCII 字符作为变量或函数名，而且任何可移植的代码都应该遵守此约定。要正确显示这些字符，你的编辑器必须能识别 UTF-8 编码，而且必须使用能支持打开的文件中所有字符的字体。

如果不使用默认编码，要声明文件所使用的编码，文件的 *第一* 行要写成特殊的注释。语法如下所示：

```python
# -*- coding: encoding -*-
```

其中 *encoding* 可以是 Python 支持的任意一种 [`codecs`](https://docs.python.org/zh-cn/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")。

比如，要声明使用 utf-8 编码，你的源码文件要写成：

```python
# -*- coding: utf-8 -*-
```

关于 *第一行* 规则的一种例外情况是，源码以 [UNIX "shebang" 行](https://docs.python.org/zh-cn/3/tutorial/appendix.html#tut-scripts) 开头。这种情况下，编码声明就要写在文件的第二行。例如：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

## [内置类型](https://docs.python.org/zh-cn/3/library/stdtypes.html)

*   [逻辑值检测](https://docs.python.org/zh-cn/3/library/stdtypes.html#truth-value-testing)
*   [布尔运算 --- `and`, `or`, `not`](https://docs.python.org/zh-cn/3/library/stdtypes.html#boolean-operations-and-or-not)
*   [比较](https://docs.python.org/zh-cn/3/library/stdtypes.html#comparisons)
*   [数字类型 --- `int`, `float`, `complex`](https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex)
*   [迭代器类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator-types)
*   [序列类型 --- `list`, `tuple`, `range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#sequence-types-list-tuple-range)
*   [文本序列类型 --- `str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#text-sequence-type-str)
*   [二进制序列类型 --- `bytes`, `bytearray`, `memoryview`](https://docs.python.org/zh-cn/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
*   [集合类型 --- `set`, `frozenset`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set-types-set-frozenset)
*   [映射类型 --- `dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#mapping-types-dict)
*   [上下文管理器类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#context-manager-types)
*   [其他内置类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#other-built-in-types)
*   [特殊属性](https://docs.python.org/zh-cn/3/library/stdtypes.html#special-attributes)

## 基本数据类型

Python 中的变量不需要提前声明。
变量赋值后会自动创建。

* 不可变
  * 数字（Number）
  * 字符串（String）
  * 元组（Tuple）
* 可变
  * 列表（List）
  * 字典（Dictionary）
  * 列表（Set）

### 数字

* 整数（比如 `2`、`4`、`20` ） [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int") 类型
* 有小数部分的（比如 `5.0`、`1.6` ） [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float "float") 类型
* 等号 (`=`) 用于给一个变量赋值

```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

### 字符串

* 单引号（`'……'`）
* 双引号（`"……"`）
* 反斜杠 `\` 可以用来转义
* 字符串前面加 `r` 禁止反斜杠 `\` 转义
* 索引从 0 开始，-1 为结尾位置
* `+` 连接字符串

```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

除了索引，字符串还支持 切片。索引可以得到单个字符，而 切片 可以获取子字符串:

```python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

注意切片的开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s

### 列表

Python 中可以通过组合一些值得到多种 复合 数据类型，其中最常用的 列表。

* 通过方括号括起、逗号分隔的一组值
* 一个 列表 可以包含不同类型的元素，但通常使用时各个元素类型相同
* 和字符串一样，列表也支持索引和切片

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

### 元组

* 元组是不可变序列，通常用于储存异构数据的多项集（例如由 [`enumerate()`](https://docs.python.org/zh-cn/3/library/functions.html#enumerate "enumerate") 内置函数所产生的二元组）
* 元组也被用于需要同构数据的不可变序列的情况（例如允许存储到 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set "set") 或 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict "dict") 的实例）。
* Python的元组与列表类似，不同之处在于元组的元素不能修改。
* 元组使用小括号，列表使用方括号。
* 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

```python
>>> brother = ('小武', '小久', 2015, 2019)
>>> numbers = (1, 2, 3, 4, 5 )
>>> alpha = "a", "b", "c", "d"
>>> brother
('小武', '小久', 2015, 2019)
>>> numbers
(1, 2, 3, 4, 5)
>>> alpha
('a', 'b', 'c', 'd')
```

### 字典

[mapping](https://docs.python.org/zh-cn/3/glossary.html#term-mapping) 对象会将 [hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable) 值映射到任意对象。 映射属于可变对象。 目前仅有一种标准映射类型 *字典*。

* 字典的键 *几乎* 可以是任何值。
* 非 [hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable) 的值，即包含列表、字典或其他可变类型的值（此类对象基于值而非对象标识进行比较）不可用作键。
* 数字类型用作键时遵循数字比较的一般规则：如果两个数值相等 (例如 `1` 和 `1.0`) 则两者可以被用来索引同一字典条目。 （但是请注意，由于计算机对于浮点数存储的只是近似值，因此将其用作字典键是不明智的。）

```python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
```

### 集合

*set* 对象是由具有唯一性的 [hashable](https://docs.python.org/zh-cn/3/glossary.html#term-hashable) 对象所组成的无序多项集。 常见的用途包括成员检测、从序列中去除重复项以及数学中的集合类计算。

* 交集
* 并集
* 差集
* 对称差集

无序的多项集

* 支持 `x in set, len(set)` 和 `for x in set`
* 集合并不记录元素位置或插入顺序
* 不支持索引、切片或其他序列类的操作

```python
>>> basket = {'apple', 'orange', 'apple', 'grape', 'orange', 'banana'}
>>> print(basket)
{'orange', 'banana', 'grape', 'apple'}
>>> 'orange' in basket
True
>>> 'strawberry' in basket
False
```

## 流程控制

### `if` 语句

用于有条件的执行:

```python
>>> x = int(input("Please enter an integer:"))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```

可以有零个或多个 [`elif`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#elif) 部分，以及一个可选的 [`else`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#else) 部分。 关键字 '`elif`' 是'else if' 的缩写，适合用于避免过多的缩进。 一个 `if` ... `elif` ... `elif` ... 序列可以看作是其他语言中的 `switch` 或 `case` 语句的替代。

###  `for` 语句

用于对序列（例如字符串、元组或列表）或其他可迭代对象中的元素进行迭代:

```python
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

### `while` 语句

用于在表达式保持为真的情况下重复地执行:

```python
>>> monkeys = 5
>>> while monkeys > 0:
...     print("{} 只猴子当荡秋千，嘲笑鳄鱼被水淹。鳄鱼来了，鳄鱼来了，啊呜!".format(monkeys))
...     monkeys -= 1
...
5 只猴子当荡秋千，嘲笑鳄鱼被水淹。鳄鱼来了，鳄鱼来了，啊呜!
4 只猴子当荡秋千，嘲笑鳄鱼被水淹。鳄鱼来了，鳄鱼来了，啊呜!
3 只猴子当荡秋千，嘲笑鳄鱼被水淹。鳄鱼来了，鳄鱼来了，啊呜!
2 只猴子当荡秋千，嘲笑鳄鱼被水淹。鳄鱼来了，鳄鱼来了，啊呜!
1 只猴子当荡秋千，嘲笑鳄鱼被水淹。鳄鱼来了，鳄鱼来了，啊呜!
```

### `break` 和 `continue` 语句

 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break) 语句，和 C 中的类似，用于跳出最近的 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 或 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while) 循环.

循环语句可能带有一个 `else` 子句；它会在循环遍历完列表 (使用 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for)) 或是在条件变为假 (使用 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while)) 的时候被执行，但是不会在循环被 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break) 语句终止时被执行。

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

###  `pass` 语句

[`pass`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#pass) 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它。例如:

```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

这通常用于创建最小的类:

```python
>>> class MyEmptyClass:
...     pass
...
```

[`pass`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#pass) 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，允许你保持在更抽象的层次上进行思考。 `pass` 会被静默地忽略:

```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```


## 函数

我们可以创建一个输出任意范围内 Fibonacci 数列的函数:

```python
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

* 关键字 [`def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#def) 引入一个函数 *定义*
* 它必须后跟函数名称和带括号的形式参数列表
* 构成函数体的语句从下一行开始，并且必须缩进。

* 函数体的第一个语句可以（可选的）是字符串文字；这个字符串文字是函数的文档字符串或 *docstring*
* 有些工具使用文档字符串自动生成在线或印刷文档，或者让用户以交互式的形式浏览代码
* 在你编写的代码中包含文档字符串是一种很好的做法，所以要养成习惯。


## 编码风格

现在你将要写更长，更复杂的 Python 代码，是时候讨论一下 *代码风格*。大多数语言都能使用不同的风格编写（或更简洁，格式化的）；有些比其他的更具有可读性。能让其他人轻松阅读你的代码总是一个好主意，采用一种好的编码风格对此有很大帮助。

对于 Python，[**PEP 8**](https://www.python.org/dev/peps/pep-0008) 已经成为大多数项目所遵循的风格指南；它促进了一种非常易读且令人赏心悦目的编码风格。每个 Python 开发人员都应该在某个时候阅读它；以下是为你提取的最重要的几个要点：

*   使用 4 个空格缩进，不要使用制表符。

    4 个空格是一个在小缩进（允许更大的嵌套深度）和大缩进（更容易阅读）的一种很好的折中方案。制表符会引入混乱，最好不要使用它。

*   换行，使一行不超过 79 个字符。

    这有助于使用小型显示器的用户，并且可以在较大的显示器上并排放置多个代码文件。

*   使用空行分隔函数和类，以及函数内的较大的代码块。

*   如果可能，把注释放到单独的一行。

*   使用文档字符串。

*   在运算符前后和逗号后使用空格，但不能直接在括号内使用： `a = f(1, 2) + g(3, 4)`。

*   类和函数命名的一致性；规范是使用 `CamelCase` 命名类，`lower_case_with_underscores` 命名函数和方法。始终使用 `self` 作为第一个方法参数的名称（有关类和方法，请参阅 [初探类](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-firstclasses) ）。

*   如果你的代码旨在用于国际环境，请不要使用花哨的编码。Python 默认的 UTF-8 或者纯 ASCII 在任何情况下都能有最好的表现。

*   同样，哪怕只有很小的可能，遇到说不同语言的人阅读或维护代码，也不要在标识符中使用非 ASCII 字符。

## Python 之弹

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

* 优美优于丑陋，
* 明了优于隐晦；
* 简单优于复杂，
* 复杂优于凌乱，
* 扁平优于嵌套，
* 可读性很重要！
* 即使实用比纯粹更优，
* 特例亦不可违背原则。
* 错误绝不能悄悄忽略，
* 除非它明确需要如此。
* 面对不确定性，
* 拒绝妄加猜测。
* 任何问题应有一种，
* 且最好只有一种，
* 显而易见的解决方法。
* 尽管这方法一开始并非如此直观，
* 除非你是荷兰人。
* 做优于不做，
* 然而不假思索还不如不做。
* 很难解释的，必然是坏方法。
* 很好解释的，可能是好方法。
* 命名空间是个绝妙的主意，
* 我们应好好利用它。

参考：[https://docs.python.org/zh-cn/3/](https://docs.python.org/zh-cn/3/)
