"""
下述代码从键盘读入了以逗号分隔的两个整数a,b：
a,b = eval(input())
print(a,b,type(a),type(b))
当操作者输入 4,5 时，程序的执行结果如下：
4,5
4 5 <class 'int'> <class 'int'>
注意：4,5中间的逗号必须是英文逗号。
请以上述代码为基础，完成下述填空，并在计算机上调试运行。
1、请输入 5,7 ，此时，a = ___________________ ，b = ___________________ ；
2、a是否大于b？ print(  ___________________  )，执行结果是： ___________________  ；
3、a是否不大于b？ print( ___________________ a>b )，执行结果是： ___________________  ；
4、a是否大于b或者等于b？ print(a>b  ___________________  a==b)，执行结果是： ___________________  ；
5、a是否大于或等于b？ print(a  ___________________  b)，执行结果是： ___________________  ；
6、b是否大于3且小于等于7？ print( 3  ___________________  b  ___________________  7),执行结果是： ___________________  ；
7、b是否大于3且小于等于7？ print(b>3 and 7  ___________________  b)，执行结果是： ___________________  ；
8、a是否是奇数？print(  ___________________  )，执行结果是： ___________________  ；
9、a是奇数且b是偶数？ print(a%2==1 and  ___________________  ) ，执行结果是： ___________________  ；
10、两数中的较小值是否能够整除较大值？print(  ___________________  % min(a,b)  ___________________  0) ，执行结果是： ___________________  ；
11、a是否不等于b？ print(a  ___________________  b)，执行结果是： ___________________  。

"""


"""
基于给定的信息，下面是填空题的答案：
1、请输入 5,7 ，此时，a = 5 ，b = 7；

2、a是否大于b？
print(a > b)
执行结果是： False；

3、a是否不大于b？
print(not a > b)
执行结果是： True；

4、a是否大于b或者等于b？
print(a > b or a == b)
执行结果是： False；

5、a是否大于或等于b？
print(a >= b)
执行结果是： False；

6、b是否大于3且小于等于7？
print(3 < b and b <= 7)
执行结果是： True；

7、b是否大于3且小于等于7？
print(b > 3 and 7 >= b)
执行结果是： True；

8、a是否是奇数？
print(a % 2 == 1)
执行结果是： True；

9、a是奇数且b是偶数？
print(a % 2 == 1 and b % 2 == 0)
执行结果是： False；

10、两数中的较小值是否能够整除较大值？
print(max(a, b) % min(a, b) == 0)
执行结果是： False；

11、a是否不等于b？
print(a != b)
执行结果是： True。
"""