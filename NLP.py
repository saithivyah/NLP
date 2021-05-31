
s=[0,0,0]
c=[0,0,0]
r=[0,0,0]
f=open('weather.txt','r')
line = f.readline()
while line:
    line=line.rstrip().split(',')
    
    if line[0] == 'sunny' and line[1] == 'sunny':
        s[0]=s[0]+1
    elif line[0] == 'sunny' and line[1] == 'cloudy':
        s[1]=s[1]+1
    elif line[0] == 'sunny' and line[1] == 'rainy':
        s[2]=s[2]+1  
    elif line[0] == 'cloudy' and line[1] == 'sunny':
        c[0]=c[0]+1
    elif line[0] == 'cloudy' and line[1] == 'cloudy':
        c[1]=c[1]+1
    elif line[0] == 'cloudy' and line[1] == 'rainy':
        c[2]=c[2]+1
    elif line[0] == 'rainy' and line[1] == 'sunny':
        r[0]=r[0]+1
    elif line[0] == 'rainy' and line[1] == 'cloudy':
        r[1]=r[1]+1
    elif line[0] == 'rainy' and line[1] == 'rainy':
        r[2]=r[2]+1
    line = f.readline()
prob_mat=list()
temp=[]
for i in s:
    temp.append(i/sum(s))
prob_mat.append(temp)
temp=[]
for i in c:
    temp.append(i/sum(c))
prob_mat.append(temp)
temp=[]
for i in r:
    temp.append(i/sum(r))
prob_mat.append(temp)
print("Probability Matrix")
print(prob_mat)
prob_mat2=list()
prob_mat4=list()

def mat_mul(X):
    result = [[0,0,0],
         [0,0,0],[0,0,0]]
    r = [[0,0,0],
         [0,0,0],[0,0,0]]
    for i in range(len(X)):
        for j in range(len(X[0])):
            r[j][i] = X[i][j]
         
       
    for i in range(len(X)):
        for j in range(len(r[0])):
            for k in range(len(r)):
                result[i][j] += X[i][k] * r[k][j]
    return result

prob_mat2=mat_mul(prob_mat)
prob_mat4=mat_mul(prob_mat2)
print("Probability Matrix 2")
print(prob_mat2)
print("Probability Matrix 4")
print(prob_mat4)

from tkinter import *
import tkinter as tk
from datetime import datetime
from PIL import ImageTk , Image
import requests
from tkinter import messagebox
import gtts
from playsound import playsound

def weather():      

    master = Tk()

    # Create this method before you create the entry
    def return_entry(en):
        d={0:'sunny',1:'cloudy',2:'rainy'}
        content = entry.get()
        if content == 'sunny':
            m=max(prob_mat[0])
            i=prob_mat[0].index(m)
            m1=max(prob_mat2[0])
            i1=prob_mat2[0].index(m1)
            m2=max(prob_mat4[0])
            i2=prob_mat4[0].index(m2)
            w="Tomorrow's weather will be "+d[i]+",  Day after tomorrow's the weather will be  "+d[i1]+" and the weather will be "+d[i2]+"for the forthcoming day " +"\n Have a good day and be prepared"
            Label(master, text=w).grid(row=3,column=1)
            tts = gtts.gTTS(w)
            tts.save("hello.mp3")
            playsound("hello.mp3")
        elif content == 'cloudy':
            m=max(prob_mat[1])
            i=prob_mat[1].index(m)
            m1=max(prob_mat2[1])
            i1=prob_mat2[1].index(m1)
            m2=max(prob_mat4[1])
            i2=prob_mat4[1].index(m2)
            w="Tomorrow's weather will be "+d[i]+",  Day after today's the weather will be  "+d[i1]+" and the weather will be "+d[i2]+" for the forthcoming day " +"\n Have a good day and be prepared"
            Label(master, text=w).grid(row=3,column=1)
            tts = gtts.gTTS(w)
            tts.save("hello.mp3")
            playsound("hello.mp3")
        elif content == 'rainy':
            m=max(prob_mat[2])
            i=prob_mat[2].index(m)
            m1=max(prob_mat2[2])
            i1=prob_mat2[2].index(m1)
            m2=max(prob_mat4[2])
            i2=prob_mat4[2].index(m2)
            w="Tomorrow's weather will be "+d[i]+",  Day after today's the weather will be  "+d[i1]+" and the weather will be "+d[i2]+" for the forthcoming day " +"\n Have a good day and be prepared"
            Label(master, text=w).grid(row=3,column=1)
            tts = gtts.gTTS(w)
            tts.save("hello.mp3")
            playsound("hello.mp3")
        
            
            
            
          

    Label(master, text="TODAY'S WEATHER").grid(row=0, sticky=W)

    entry = Entry(master)
    entry.grid(row=0, column=1)

    entry.bind('<Return>', return_entry) 

    mainloop()

def about():
    root = Tk()
    root.geometry("700x300")
    s="Weather forecast through Markov chains and Python"
    labelframe = LabelFrame(root, text=s)
    labelframe.pack(fill="both", expand="yes")
    t="A Markov chain is a mathematical system that undergoes transitions from one state to another on a state space.\n It is essentially a kind of random process without any memory.\n This last statement, emphasizes the idea behind this process: “The future is independent from the past given the present”.\n In short, we could say that, the next step of our random process depends only on the very last step occurred. \n(Note that we are operating in discrete time in this case).Let’s say that we would like to build a statistical model to forecast the weather. \nIn this case, our state space, for the sake of simplicity, will contain only 2 states: bad weather (cloudy) and good weather (sunny). \n\nLet’s suppose that we have made some calculations and found out that tomorrow’s weather somehow relies on today’s weather, according  to the matrix below.\n Note that P(A|B) is the probability of A given B."


     
    left = Label(labelframe, text=t)
    left.pack()
    btn=Button(root, text="Back", fg="blue",command=root.destroy)
    btn.pack()


    tts = gtts.gTTS(t)
    tts.save("hello1.mp3")
    playsound("hello1.mp3")
    
    root.mainloop()

                


import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

 
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(side = BOTTOM)
root.geometry("500x300")

lb=Label(root,text="Weather prediction using Markov Chain Model",font=('Helvetica', 12, 'bold'))
lb.pack(side=TOP)
lbl = ImageLabel(root, height =200 ,width=300)
lbl.pack()
lbl.load('giphy.gif')

btn2 = tk.Button(frame,text="ABOUT",command=about)
btn2.pack(side=LEFT)

btn1 = tk.Button(frame,text ="PREDICT",fg="green",command=weather)
btn1.pack( side= LEFT)

btn2 = tk.Button(frame,text="QUIT",fg="red",command=quit)
btn2.pack(side = LEFT)



root.mainloop()
    
      
       
       
           
