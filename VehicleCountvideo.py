f = open('/home/vislab/UAV/dataconversion/bumtracking/resultvid3/Tracking_coordinate.txt', 'r')
x1, y1, x2, y2 = 1000, 490, 1280, 720
trackinginfo = []


import cv2
import natsort
import os
vid = cv2.VideoCapture('/home/vislab/UAV/dataconversion/bumtracking/resultvid3/resultvid3.avi')
width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
length=int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
fps=vid.get(cv2.CAP_PROP_FPS)
out=codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/vislab/UAV/dataconversion/bumtracking/resultvid3/traffic3.avi', codec, fps, (width, height))
imagepath='/home/vislab/UAV/dataconversion/bumtracking/trackingv3'
imagelist=natsort.natsorted(os.listdir(imagepath))

dict={}
lines = f.readlines()
for line in lines:
  line = line.rstrip().split(' ')
  trackinginfo.append(line)

column_values = [int(idcolumn[1])for idcolumn in trackinginfo]
max_id = max(column_values)

checked = [0]*max_id
count_vehicle, count_car, count_truck, count_motorcycle = 0, 0, 0, 0
for i in trackinginfo:
  id = int(i[1])-1
  fr=int(i[0])
  center_x = ( int(i[2]) + int(i[4]) ) / 2.0
  bottom_y = int(i[5])
  if x1<=center_x<=x2 and y1<=bottom_y<=y2 :
    if checked[id] == 0:
      #print(i)
      class_car = int(i[6])
      if class_car == 3:
        count_car += 1
      elif class_car == 4:
        count_motorcycle += 1

      elif class_car == 8:
        count_truck += 1
      checked[id] = 1
  dict[fr]=(count_car,count_truck,count_motorcycle)

count_vehicle = count_car+count_motorcycle+count_truck
print("총 차량수 : {}, 승용차 : {}, 이륜차 : {}, 화물차 : {}".format(count_vehicle, count_car, count_motorcycle, count_truck))

x3,y3,x4,y4=900,10,1280,200
for i in range(length):
  img=cv2.imread("/home/vislab/UAV/dataconversion/bumtracking/trackingv3/%d.jpg"%(i+1))
  cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 2)
  cv2.rectangle(img,(x3,y3),(x4,y4),(255,255,255),-1)
  cv2.putText(img,'Car',(x3+10,y3+20),0,1,(0,0,0),thickness=1)
  cv2.putText(img, str(dict[i+1][0]), (x3+200, y3+20), 0,1,(0,0,0), thickness=1)
  cv2.putText(img,'Trcuk',(x3+10,y3+70),0,1,(0,0,0),thickness=1)
  cv2.putText(img, str(dict[i+1][1]), (x3+200, y3+70), 0,1,(0,0,0), thickness=1)
  cv2.putText(img,'Motorcycle',(x3+10,y3+120),0,1,(0,0,0),thickness=1)
  cv2.putText(img, str(dict[i+1][2]), (x3+200, y3+120), 0,1,(0,0,0), thickness=1)
  out.write(img)
  
out.release()
f.close()
vid.release()


