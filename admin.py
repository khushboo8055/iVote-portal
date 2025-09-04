import tkinter as t 
from tkinter import messagebox as m
import mysql.connector as ms
class admin:
    def toggle_password(self):
        if self.__showing:
           self.__p1.config(show="*")
           self.__eye_btn.config(text="👁")
           self.__showing = False
        else:
           self.__p1.config(show="")
           self.__eye_btn.config(text="🚫")
           self.__showing = True

    def validation(self,event):
        if self.__a1.get()=='' or  self.__p1.get()=='':
            m.showerror('Error','Please fill all entries')               
        else:
            connectiondb=ms.connect(user='root',password='Khushboo@123',host='localhost',database='votingdb')
            cur=connectiondb.cursor()
            cur.execute('select * from Admin where Admin=%s and Password=%s',(self.__a1.get(),self.__p1.get()))
            #print(cur.fetchone)
            if cur.fetchone():
                m.showinfo('success','Login Success')    
                import adminmain as am 
                self.__w.destroy()
                a1=am.adminmain()
                       
            else:
                m.showerror('Error','No details found')               
        
    def __init__(self):
        self.__w=t.Tk()
        w=370
        h=260
        x=self.__w.winfo_screenwidth()//2-w//2
        y=self.__w.winfo_screenheight()//2-h//2
        self.__w.geometry('{}x{}+{}+{}'.format(w,h,x,y))
        self.__w.title('Admin page')
        self.__a=t.Label(text='Admin',font=26)
        self.__p=t.Label(text='Password',font=26)
        
        
        self.__a1=t.Entry()
        self.__p1=t.Entry(show='*')
        self.__showing = False
        self.__eye_btn = t.Button(self.__w, text="👁", command=self.toggle_password)
        self.__eye_btn.place(x=315, y=90, width=30, height=30)

        
        self.__a.place(x=40,y=40)
        self.__a1.place(x=160,y=40,width=155,height=30)
        
        self.__p.place(x=40,y=90)
        self.__p1.place(x=160,y=90,width=155,height=30)
        
        
        
        self.__b=t.Button(text='Login',fg='white',bg='black')
        self.__b.place(x=170,y=160,width=100,height=35)
        self.__b.bind('<Button-1>',self.validation)
        
        self.__w.mainloop()
#s1=admin()        