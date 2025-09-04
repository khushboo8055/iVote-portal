
import tkinter as  t

class Voting:
    def nextwindow(self):
        import main as m 
        self.__w.destroy()
        v1=m.v_a()        
        
    def __init__(self):
        self.__w=t.Tk()
        self.__w.overrideredirect(True)
        w=750
        h=398
        x=self.__w.winfo_screenwidth()//2-w//2
        y=self.__w.winfo_screenheight()//2-h//2
        self.__w.geometry('{}x{}+{}+{}'.format(w,h,x,y))
        
        self.__ig=t.PhotoImage(file='vote12.png')
        self.__ig1=t.Label(image=self.__ig)
        self.__ig1.place(x=0,y=0,width=w,height=h)
        self.__w.after(3000,self.nextwindow)
        
        
        
        self.__w.mainloop()
i1=Voting()        
        
