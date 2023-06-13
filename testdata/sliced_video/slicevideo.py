import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

vfilepath='' #이미지로 자를 영상 경로
videofile=cv2.VideoCapture(vfilepath)

length=int(videofile.get(cv2.CAP_PROP_FRAME_COUNT))
width=int(videofile.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(videofile.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=videofile.get(cv2.CAP_PROP_FPS)
print("length:",length) # 동영상 길이, 크기, fps 확인
print("width:",width)
print("height:",height)
print("fps:",fps)

count=1
while(True):
    ret, image=videofile.read()
    if not ret: break
    if(int(videofile.get(1)) % 4 == 0): # 몇 프레임 당 1장씩 자를지 
        cv2.imwrite('저장경로'+'/%d.jpg'%count,image) # 동영상 저장경로
        print('saved frame number:',str(int(videofile.get(1))))
        count+=1
    
videofile.release()