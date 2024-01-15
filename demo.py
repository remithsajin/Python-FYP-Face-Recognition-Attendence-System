# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import pandas as pd
class Face_Recognition:

    


    def __init__(self,root):
        self.var_sub=StringVar()
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\hp\Pictures\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.NEAREST)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.NEAREST)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # current_course_frame = LabelFrame(bg_img,relief=RIDGE,bd=2,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
        # current_course_frame.place(x=350,y=25,width=350,height=50)

        sub_label=Label(bg_img,font=("verdana",12,"bold"),bg="white",fg="navyblue")
        sub_label.grid(row=0,column=2,padx=5,pady=15)

        #combo box 
        sub_combo=ttk.Combobox(bg_img,textvariable=self.var_sub,width=15,font=("verdana",12,"bold"),state="readonly")
        sub_combo["values"]=("Select Subject","AIML","BDA","NM","UID","EPM","AIML LAB")
        sub_combo.current(0)
        sub_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)
        sub_combo.place(x=600,y=50,width=170,height=50)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.NEAREST)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_img_btn2=Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn2=std_img_btn2.resize((180,180),Image.NEAREST)
        self.std_img2=ImageTk.PhotoImage(std_img_btn2)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=500,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=500,y=350,width=180,height=45)


        std_b2 = Button(bg_img,command=self.save_attend,image=self.std_img2,cursor="hand2")
        std_b2.place(x=700,y=170,width=180,height=180)

        std_b1_2 = Button(bg_img,command=self.save_attend,text="Save Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_2.place(x=700,y=350,width=180,height=45)


    #=====================Attendance===================

    def mark_attendance(self,i,r,n):
        # with open("attendance.csv","r+",newline="\n") as f:
        #     myDatalist=f.readlines()
        #     name_list=[]
        #     for line in myDatalist:
        #         entry=line.split(",")
        #         name_list.append(entry[0])

        #     # if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
        #         now=datetime.now()
        #         d1=now.strftime("%d/%m/%Y")
        #         dtString=now.strftime("%H:%M:%S")
        #         f.write(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")
        attendance_data = f"{i}, {r}, {n}, {dtString}, {d1}, Present\n"

        with open("attendance.csv", "a", newline="\n") as f:
            f.write(attendance_data)


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            global coord
            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                # id,predict=clf.predict(y:y+h,x:x+w)
                

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()


                cursor.execute("select Name from students where Student_ID=%s",("Student_ID",))
                global n 
                n=cursor.fetchone()
                n=n
                n=str(n)
                # n=str(n)
                # n="".join(n)

                cursor.execute("select Roll_No from students where Student_ID=%s",("Student_ID",))
                global r
                r=cursor.fetchone()
                r=r
                r=str(r)
                # r="+".join(r)

                cursor.execute("select Student_ID from students where Student_ID=%s",("Student_ID",))
                i=cursor.fetchone()
                i=i
                i=str(i)
                # i=str(i)
                # i="+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll-No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    # self.mark_attendance(i,r,n)
                    # self.save_attend()
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        


        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        videoCap.release()
        cv2.destroyAllWindows()
    
    def save_attend(self):
            sub=self.var_sub.get()
            if sub!="Select Subject":
                try:
                    file_path=fr"C:\Users\hp\Pictures\Python-FYP-Face-Recognition-Attendence-System\Attendance\{sub}.csv"
                    df = pd.read_csv(file_path)
                    # print(df)
                    now=datetime.now()
                    column_name = now.strftime("%Y-%m-%d %H:%M")
                    # df['Name'] = n
                    # df['USN'] = r
                    print(n)
                    # if n:
                    #     df[column_name]="Present"
                    #     df.to_csv(file_path, index=False)
                    messagebox.showinfo("Success", "Attendance saved successfully.")
                    # else:
                    #     df[column_name]="Absent"

                except FileNotFoundError:
                    messagebox.showerror("Error", "CSV file not found.")
            else:
                messagebox.showerror("Error","Please select the subject")
        




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()