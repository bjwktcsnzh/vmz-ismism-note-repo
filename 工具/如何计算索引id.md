# 如何计算索引id

## 通过计算b站页数

假如一个视频在第 x 页 **从后往前** 数第 $i_x$​​​ 个；总共有y页视频；每页有 t 个视频 *(b站网页端 t=30)* ；最后一页的视频数是 $i_y$​​​​​。

那么该视频是第 r 个视频。$ r = (y-x-1)\times t + i_x + i_y $​

```python
def r(x,ix,y,iy,t=30):
    return (y-x-1)*t+ix+iy
```

假如一个视频是第 r 个视频。总共有y页视频；每页有 t 个视频 *(b站网页端 t=30)* ；最后一页的视频数是 $i_y$​。

那么该视频在第 x 页的 **从后往前** 数第 $i_x$​个。

$x = y-((r-i_y)整除以t)-1$

$ i_x = (r-i_y)对t求余 $

计算id所在页数的python函数代码。

```python
""" First is x, last is ix . """
def locate(r,y,iy,t=30):
    result = divmod(r-iy,t)
    return y-result[0]-1, result[1] 
```

**想偷懒** 并且 **已经在本地装上python** 的小朋友，把这两个函数复制粘贴到终端中，就可以傻瓜式调用了。例如在以下的终端中的代码示例：

```python
tcsnzh@ubuntuzh:~$ python3
Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def r(x,ix,y,iy,t=30):
...     return (y-x-1)*t+ix+iy
... 
>>> def locate(r,y,iy,t=30):
...     result = divmod(r-iy,t)
...     return y-result[0]-1, result[1] 
... 
>>> r(3,23,16,26)
409
>>> locate(409,16,26)
(3, 23)
>>> quit()
```

聪明的小朋友发现了可以设置默认值来省力气。

```python
tcsnzh@ubuntuzh:~$ python3
Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def r(x,ix,y=16,iy=26,t=30):
...     return (y-x-1)*t+ix+iy
... 
>>> def locate(r,y=16,iy=26,t=30):
...     result = divmod(r-iy,t)
...     return y-result[0]-1, result[1] 
... 
>>> r(3,23)
409
>>> locate(409)
(3, 23)
>>> quit()
```

不过假若叔叔把视频夹掉了，可能导致前后序号不一致，这时候请自行灵活变通。

