# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:38:46 2020

@author: 77433
"""
import re

#s = r'\d+.\d+'
#cpu = 'Intel 酷睿i7 10510U'
#pattern = re.compile(s)
#screen_size1 = "14.5英寸"
#a = re.search(pattern,screen_size1)
#print(a.group(0))

def cpu_rank(s):
    p = r'i+\d'
    pattern = re.compile(p)
    a = re.search(pattern,s)
    if a == None :
        return 0
    else:
        return a.group(0)

def screen_size(s):
    p = r'\d+\.\d'
    pattern = re.compile(p)
    a = re.search(pattern,s)
    if a == None :
        return 0
    else:
        return float(a.group(0))
    
def keyboardhaslight(s):
    if '背光' in s :
        return '1'
    else:
        return '0'
    
def gpu_memory(s):
    p = r'\d+'
    pattern = re.compile(p)
    a = re.search(pattern,s)
    if a == None:
        return 0 
    else:
        return int(a.group(0))
    
def ram(s):
    p = r'\d*'
    pattern = re.compile(p)
    a = re.search(pattern,s)
    if a == None:
        return 0 
    else:
        return int(a.group(0))
    
def is_rtx(s):
    p = r'RTX.*\d'
    pattern = re.compile(p)
    a = re.search(pattern,s)
    if a == None:
        return 0 
    else:
        return a.group(0).replace(" ","")
    
def weight(s):
    p = r'\d+.\d+'
    pattern = re.compile(p)
    a = re.search(pattern,s)
    if a == None :
        return 0
    else:
        weight = float(a.group(0))
    if weight > 10:
        weight =weight/1000
    if 0.1<weight < 1.2 :
        return "light"
    if weight <1.8 :
        return 'medium'
    else:
        return 'heavy'
    
def battery(s):
    p = r'\d+'
    pattern = re.compile(p)
    a = re.search(pattern,s)
    if a == None :
        return 0
    else:
        time = float(a.group(0))
    if time > 5:
        return "long"
    else:
        return "short"
    
def game_type(s):

    if '游戏' in str(s) :
        return '1'
    else :
        return '0'

def thin_type(s):

    if '轻' in str(s) :
        return '1'
    else :
        return '0'

def business_type(s):

    if '商务' in str(s):
        return '1'
    else :
        return '0'
    
def video_type(s):
    if '影音' in str(s) :
        return '1'
    else:
        return '0'

def is_apple(s):
    if'苹果' in s :
        return '1'
    else:
        return '0'
    
if __name__ == '__main__':
    cpu = 'Intel 酷睿i7 10510U'
    screen_size1 = "14.5英寸"
    gm = '4gb'
    GPU = 'NVIDIA GeForce RTX 2060'
    w = ' 775g'
    b = '10小时的无线网络浏览10小时的iTunes影片播放'
    d = '游戏本,影音娱乐本,'
    print(game_type(d),video_type(d))
    print (battery(b))
    print(weight(w))
    print(is_rtx(GPU))
    print (cpu_rank(cpu))
    print(screen_size(screen_size1))
    print(gpu_memory(gm))