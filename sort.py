from manimlib import *
import random

# FRAME_WIDTH = 20
# FRAME_HEIGHT = 20

def creatRect(h,w):
    rect = Rectangle(height=h,width=w)
    rect.set_fill(BLUE_B,1)
    rect.set_stroke(opacity=0)
    return rect

def cgroup(arr):
    res = VGroup()
    res.add(*[creatRect(h,FRAME_WIDTH/ len(arr)) for h in arr])
    res.arrange(RIGHT,aligned_edge=DOWN,buff=0)
    return res
def exchange(sc:Scene,group:VGroup,x,y):
    sc.play(group[x].animate.shift((group[y].get_x()-group[x].get_x())*RIGHT),
            group[y].animate.shift((group[x].get_x()-group[y].get_x())*RIGHT),run_time=0.3)


def getRandomArr(n):
    """创建一个长度为n的乱序数组"""
    l = [i*float(FRAME_HEIGHT)/n for i in range(1,n+1)] 
    random.shuffle(l) # 这个函数没有返回值，而是直接打乱原列表
    return l

def buble_sort(sc:Scene,group:VGroup,arr:list):
    """冒泡法排序
    
    :param sc    : current Scene
    :param group : the array need to be sorted  
    :param arr   : number list
    :return: None
    """
    for _ in range(len(arr)):
        for i in range(len(arr)-1):
            group[i].set_color(RED)
            group[i+1].set_color(RED)
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1],arr[i]
                exchange(sc,group,i,i+1)
                sc.remove(group)
                group = cgroup(arr)
                sc.add(group)               

            # sc.wait(0.1)
            group[i].set_color(BLUE_B)
            group[i+1].set_color(BLUE_B)


class SortScene(Scene):
    def construct(self):
    # 创建矩形c
        arr = getRandomArr(10)
        rectGroup = cgroup(arr=arr)
        self.add(rectGroup)
        tittle1 = Tex("bublesort",font='Source Han Sans').to_corner(LEFT+UP)
        self.add(tittle1)
        buble_sort(self,rectGroup,arr)               
        
       