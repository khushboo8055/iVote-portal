import tkinter as t
class v_a:
    
    def nextpage(self,event):
        import admin as a 
        self.__w.destroy()
        a.admin()
    def nextwindow(self,event):
        import login as l 
        self.__w.destroy()
        l.login()
        
    def __init__(self):
        self.__w=t.Tk()
        w=300
        h=230
        x=self.__w.winfo_screenwidth()//2-w//2
        y=self.__w.winfo_screenheight()//2-h//2
        self.__w.geometry('{}x{}+{}+{}'.format(w,h,x,y))
        
        self.__b1=t.Button(text='Voter',fg='purple')
        self.__b1.place(x=100,y=50,width=100,height=50)
        self.__b1.bind('<Button-1>',self.nextwindow)
        
        self.__b2=t.Button(text='Admin',fg='purple')
        self.__b2.place(x=100,y=130,width=100,height=50)
        self.__b2.bind('<Button-1>',self.nextpage)
        
        
        
        self.__w.mainloop()
#v1=v_a()        