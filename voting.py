import tkinter as t 
import mysql.connector as ms
from tkinter import messagebox  as m
class choose:
    def nextPage(self,event,party):
          condb=ms.connect(user='root',password='Khushboo@123',host='localhost',database='votingdb')
          cur=condb.cursor()
          cur.execute('update voter set status=1 ,party=%s  where Aadhar_id=%s',(party,self.aid)) 
          condb.commit()   
          m.showinfo('Success','Vote success,Thanks')
          self.__w.destroy()
          
    def __init__(self,Aadhar_id):
        self.aid=Aadhar_id
        self.__w=t.Tk()
        w=400
        h=600
        x=self.__w.winfo_screenwidth()//2-w//2
        y=self.__w.winfo_screenheight()//2-h//2
        self.__w.geometry('{}x{}+{}+{}'.format(w,h,x,y))
        
        self.__img1=t.PhotoImage(file='Bjp 1.png')
        self.__img12=t.Button(image=self.__img1) 
        self.__img12.place(x=0,y=0,width=200,height=200)
        self.__img12.bind('<Button-1>',lambda event,p='bjp':self.nextPage(event,p))    
        
        self.__img2=t.PhotoImage(file='congress 1.png')
        self.__img21=t.Button(image=self.__img2) 
        self.__img21.place(x=200,y=0,width=200,height=200)
        self.__img21.bind('<Button-1>',lambda event,p='congress':self.nextPage(event,p))    
        
        
        self.__img3=t.PhotoImage(file='aap1.png')
        self.__img31=t.Button(image=self.__img3) 
        self.__img31.place(x=0,y=200,width=200,height=200)
        self.__img31.bind('<Button-1>',lambda event,p='aap':self.nextPage(event,p))    
        
            
        self.__img4=t.PhotoImage(file='jjp 1.png')
        self.__img41=t.Button(image=self.__img4) 
        self.__img41.place(x=200,y=200,width=200,height=200)
        self.__img41.bind('<Button-1>',lambda event,p='jjp':self.nextPage(event,p))    
        
               
        self.__img5=t.PhotoImage(file='tmc 1.png')
        self.__img51=t.Button(image=self.__img5) 
        self.__img51.place(x=0,y=400,width=200,height=200)
        self.__img51.bind('<Button-1>',lambda event,p='tmc':self.nextPage(event,p))    
        
            
        self.__img6=t.PhotoImage(file='nota 1.png')
        self.__img61=t.Button(image=self.__img6) 
        self.__img61.place(x=200,y=400,width=200,height=200)
        self.__img61.bind('<Button-1>',lambda event,p='nota':self.nextPage(event,p))    
        
        
        self.__w.mainloop()
#v1=choose()        
            
        
        
