from tkinter import*
from PIL import Image,ImageTk
import webbrowser
import os


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        # img=Image.open(r"C:\Users\hp\Pictures\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\banner.jpg")
        # img=img.resize((1366,130),Image.NEAREST)
        # self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        # f_lb1 = Label(self.root,image=self.photoimg)
        # f_lb1.place(x=0,y=0,width=1366,height=130)
        title_lb1 = Label(self.root,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # backgorund image 
        bg1=Image.open(r"C:\Users\hp\Pictures\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\hlpdsk.jpg")
        bg1=bg1.resize((1366,720),Image.NEAREST)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=55,width=1366,height=768)


        #title section
     

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\hp\Pictures\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\web.png")
        std_img_btn=std_img_btn.resize((180,180),Image.NEAREST)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=270,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=450,width=180,height=45)

        # f_lbl=Label(self.root,image=self.photobg1)
        # f_lbl.place(x=0,y=55,width=1430,height=720)

        # lbl=Label( bg_img,text="reach out to us via email.\n By clicking below 👇 button",font=("verdana",30,"bold"),fg="blue",bg="white")
        # lbl.place(x=390,y=50)

        # lbl2=Label( bg_img,text="By clicking below 👇 button",font=("verdana",30,"bold"),fg="blue",bg="white")
        # lbl.place(x=390,y=170)
        # # create function for button 
    
    
    def website(self):
        # self.new = 1
        # recipients = ["saadzh7@gmail.com", "mani@gmail.com","remithsajin@gmail.com"]

        # # Subject and body of the email
        # subject = "Face Recognition Attendance System"
        # message = "Your Query Here"

        # # Create a comma-separated string of recipients
        # to_email = ",".join(recipients)

        # # Encode the subject and message for the URL
        # subject_encoded = subject.replace(" ", "%20")
        # message_encoded = message.replace(" ", "%20")

        # # Gmail compose link
        # compose_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={to_email}&su={subject_encoded}&body={message_encoded}"

        # Open the default web browser and navigate to the Gmail compose link
        webbrowser.open("https://facerecognition.my.canva.site/face-recognition-system/")
            


if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()