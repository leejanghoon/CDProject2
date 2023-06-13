
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
vfilepath='/home/vislab/UAV/dataconversion/bumtracking/video4.mp4'
videofile=cv2.VideoCapture(vfilepath)

length=int(videofile.get(cv2.CAP_PROP_FRAME_COUNT))
width=int(videofile.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(videofile.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=videofile.get(cv2.CAP_PROP_FPS)
print("length:",length)
print("width:",width)
print("height:",height)
print("fps:",fps)

f=open("/home/vislab/UAV/dataconversion/bumtracking/newlabel/vid4.txt","r")
f2=open("/home/vislab/UAV/dataconversion/bumtracking/vid4convertnew.txt","w")


while True:
    line=f.readline()
    if not line:break
    newline=line.split()
    x=float(newline[2])
    y=float(newline[3])
    w=float(newline[4])
    h=float(newline[5])
    # 이미지 세로
    dw = 1./width
    dh = 1./height
    x = x/dw
    y = y/dh
    w = round(w/dw)                 # Box 가로
    h = round(h/dh)                 # Box 세로

    x1 = round((2*x - w)/2)         # 좌측 최상단 x좌표
    y1 = round((2*y - h)/2)         # 좌측 최상단 y좌표
    out='{} {} {} {} {} {}\n'.format(newline[0],newline[1],x1,y1,x1+w,y1+h)
    f2.write(out)
f.close()
f2.close()
"""
import os
import natsort
path='/home/vislab/UAV/dataconversion/bumtracking/labels/vid4/'

file=natsort.natsorted(os.listdir(path))
f=open("/home/vislab/UAV/dataconversion/bumtracking/newlabel/vid4.txt","w")
count=1
for i in file:
    f2=open(path+i,"r")
    while True:
        line=f2.readline()
        if not line:break
        newline=str(count)+' '+line
        f.write(newline)
    count+=1
    
    
f.close()
f2.close()
"""