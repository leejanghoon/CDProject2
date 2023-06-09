from PIL import Image
import json
import os
import re


path='/home/vislab/UAV/gdrive/datatestfolder/[원천]범계사거리/범계사거리/AY0001013/'
#filelist=os.listdir(path)

#sortfile=sorted(filelist, key=lambda x: int(re.split('[' + separators + ']',x)[3]))
#print(sortfile)
with open('/home/vislab/UAV/gdrive/datatestfolder/범계사거리_AY0001013.json', 'r') as f:
    data = json.load(f)


separators="/.jpg"
images=data['images']
annotations=data['annotations']
for i in images:
    #print(i['id'])
    id=i['id']
    for j in annotations:
        annoid=j['image_id']
        if id==annoid:
            name=i['file_name']
            new=re.split('['+separators+']',name)[1] # 숫자 파일 명만 남김 ex) AY0001013/20201222_153520_3_1710.jpg -> 20201222_153520_3_1710
            #print(new)
            f=open('/home/vislab/UAV/gdrive/datatestfolder/[원천]범계사거리/범계사거리/AY0001013/label/'+new+'.txt','w') #좌표 바꿀 파일 생성
            img = Image.open(path+new+'.jpg') # 이미지 파일 열기
            width, height = img.size # 이미지의 너비와 높이 가져오기
            print(annoid)
            for info in zip(j['bbox'],j['category_id']):
                #print(info)
                x_center=(info[0][0]+info[0][2])/(2*width) # 중심점
                y_center=(info[0][1]+info[0][3])/(2*height) # 중심점
                w=(info[0][2]-info[0][0])/width # 너비
                h=(info[0][3]-info[0][1])/height # 높이
                cls=info[1]
                if cls==1:
                    cls=0
                if cls==2 or cls==3 or cls==4 or cls==5: #화물차는 1번 클래스로 통합
                    cls=1
                if cls==6: #오토바이는 2번으로, 0번은 승용차임
                    cls=2
                if cls==7 or cls==8:continue #보행자나 분류없음은 다음으로 넘어가기
                writelist=[str(cls),str(x_center),str(y_center),str(w),str(h),'\n']
                result=" ".join(writelist)
                f.write(result)

f.close()        
                
    
