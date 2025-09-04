import tkinter as t
from tkinter import messagebox as m,ttk
from tkcalendar import*
import mysql.connector as ms
import re
from datetime import date, datetime
import random

class Register:
    def valid_email(self, email):
        # Regex pattern for a basic email validation
        self.__pattern = r'^[\w\.]+@(gmail|yahoo|icloud|outlook)\.(com|in|org|net)$'
        if re.match(self.__pattern, email):
            return True
        else:
            return False
        
    def age(self,dob):
        self.__bd= datetime.strptime(dob, "%d-%m-%Y").date()
        self.__today = date.today()
        self.__age = self.__today.year - self.__bd.year - ((self.__today.month, self.__today.day) < (self.__bd.month,self.__bd.day))        
        if self.__age >= 18:
            return True
        else:
            return False
        
    def toggle_password(self):
        if self.__showing:
           self.__p1.config(show="*")
           self.__eye_btn.config(text="👁")
           self.__showing = False
        else:
           self.__p1.config(show="")
           self.__eye_btn.config(text="🚫")
           self.__showing = True
    def toggle_cpassword(self):
        if self.showing_cp:
            self.__cp1.config(show="*")
            self.eye_btn_cp.config(text="👁")
            self.showing_cp = False
        else:
            self.__cp1.config(show="")
            self.eye_btn_cp.config(text="🚫")
            self.showing_cp = True
    #API stands for Application Programming Interface.
    def check_otp(self,event=None):
        self.__otp_window = t.Toplevel(self.__w)
        w = 200
        h = 200
        x = self.__otp_window.winfo_screenwidth() // 2 - w // 2
        y = self.__otp_window.winfo_screenheight() // 2 - h // 2
        self.__otp_window.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        self.__otp_window.title('OTP')
        self.__otp = None  # Store generated OTP
        
        self.__otp_window.transient(self.__w)
        self.__otp_window.grab_set()
        self.__otp_window.focus_force()

        # Button to generate OTP
        self.__generate_btn = t.Button(self.__otp_window, text="Generate OTP", command=self.generate_otp)
        self.__generate_btn.place(x=30,y=30,width=140,height=30)

        # Entry for OTP
        self.__entry = t.Entry(self.__otp_window,text='Enter OTP', font=("Arial", 14))
        self.__entry.place(x=65,y=80,width=90,height=30)

        # Verify Button
        self.verify_btn = t.Button(self.__otp_window, text="Verify OTP", command=self.verify_otp)
        self.verify_btn.place(x=30,y=130,width=140,height=30)

    def generate_otp(self):
        self.__otp = str(random.randint(100000, 999999))  # 6 digit OTP
        print("Generated OTP (for testing):", self.__otp)
        m.showinfo("OTP Sent", "OTP has been generated. (Check Console)")

    def verify_otp(self):
        user_otp = self.__entry.get()
        if user_otp == self.__otp:
            m.showinfo("Success", "OTP Verified Successfully ✅")
            self.__otp_verified = True   # 🔹 Mark as verified
            self.__otp_window.destroy()
        else:
            m.showerror("Error", "Invalid OTP ❌")
            self.__otp_verified = False



    def valid(self,event):
        if self.__f1.get()=='' or self.__l1.get()=='' or self.__e1.get()=='' or  self.__m1.get()=='' or self.__g.get()=='' or self.__p1.get()=='' or self.__cp1.get()=='':
           m.showerror('Error','Please fill all entries')
        elif self.__p1.get()!=self.__cp1.get():
            m.showerror('Error','confirm password should be same as password ')
        elif not self.valid_email(self.__e1.get()):
            m.showerror('Error', 'Invalid email format')
        elif not self.age(self.__cal.get()):
            m.showwarning("Age Restriction","YOU MUST BE 18 OR ABOVE TO REGISTER")
        elif not self.__otp_verified:
            m.showerror("Error",'Please generate otp by clicking on verify option')                
        else:
            # Database connection and insertion logic (unchanged)
            connectiondb = ms.connect(user='root', password='Khushboo@123',
                                      host='localhost', database='votingdb')
            cur = connectiondb.cursor()
            cur.execute('insert into voter(First_name,Last_name,Email_ID,Mobile_num,Aadhar_id,Password,Gender)values(%s,%s,%s,%s,%s,%s,%s)',
                        (self.__f1.get(), self.__l1.get(), self.__e1.get(),
                         self.__m1.get(), self.__ad1.get(), self.__p1.get(),
                         self.__g.get()))
            connectiondb.commit()
            m.showinfo('Success', 'Registration Success')
            self.__w.destroy()
            import login as l
            s1 = l.login()   
    
    def pick_date(self,event):
        self.__cal=DateEntry(self.__w, selectmode='day',date_pattern='dd-mm-yyyy',year=2025)
        self.__cal.place(x=150, y=110, width=170, height=30)
        
    def __init__(self):
        self.__w = t.Tk()
        w = 400
        h = 575
        x = self.__w.winfo_screenwidth() // 2 - w // 2
        y = self.__w.winfo_screenheight() // 2 - h // 2
        self.__w.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        self.__w.title('Registration Form')
        self.__otp_verified = False
        self.__f = t.Label(text='First Name', fg='purple',font=('bold',12))
        self.__l = t.Label(text='Last Name', fg='purple',font=('bold',12))
        self.__dob = t.Label(text='DOB', fg='purple',font=('bold',12))
        self.__e = t.Label(text='Email id', fg='purple',font=('bold',12))
        self.__m = t.Label(text='Mobile No.', fg='purple',font=('bold',12))
        self.__state=t.Label(text='State',fg='purple',font=('bold',12))
        self.__c = t.Label(text='City', fg='purple',font=('bold',12))
        self.__ad = t.Label(text='Aadhar Id', fg='purple',font=('bold',12))
        self.__p = t.Label(text='Password', fg='purple',font=('bold',12))
        self.__cp = t.Label(text='Confirm Password', fg='purple',font=('bold',10))

        self.__f1 = t.Entry()
        self.__l1 = t.Entry()
        self.__dob1 = t.Entry()
        self.__e1 = t.Entry()
        self.__m1 = t.Entry()
        self.__ad1 = t.Entry()
        self.__p1 = t.Entry(show='*')
        self.__showing = False
        self.__eye_btn = t.Button(self.__w, text="👁", command=self.toggle_password)
        self.__eye_btn.place(x=320, y=420, width=30, height=30)

        self.__cp1 = t.Entry(show='*')
        self.showing_cp = False
        self.eye_btn_cp = t.Button(self.__w, text="👁", command=self.toggle_cpassword)
        self.eye_btn_cp.place(x=320, y=460, width=30, height=30)

        self.__f.place(x=30, y=30)
        self.__f1.place(x=150, y=30, width=170, height=30)

        self.__l.place(x=30, y=70)
        self.__l1.place(x=150, y=70, width=170, height=30)

        self.__dob.place(x=30, y=110)
        self.__dob1.place(x=150, y=110, width=170, height=30)
        self.__dob1.insert(0, "dd-mm-yyyy")
        self.__dob1.bind('<Button-1>', self.pick_date)

        self.__g = t.StringVar()
        self.__g.set('male')
        t.Label(self.__w, text='Gender', fg='purple', justify='right', padx=1,font=('bold',12)).place(x=30, y=140)
        self.__r = t.Radiobutton(self.__w, text='Male', padx=8, variable=self.__g, value='male').place(x=150, y=160)
        self.__r = t.Radiobutton(self.__w, text='Female', padx=8, variable=self.__g, value='female').place(x=150, y=180)

        self.__e.place(x=30, y=220)
        self.__e1.place(x=150, y=220, width=240, height=30)

        self.__m.place(x=30, y=260)
        self.__m1.place(x=150, y=260, width=170, height=30)
        self.__otp=t.Label(text='Verify',fg='darkgrey',font='bold')
        self.__otp.place(x=325,y=262)
        self.__otp.bind('<Button-1>',self.check_otp)

        self.__state.place(x=30,y=300)
        options = ['Haryana']
        self.__dropdown_menu = ttk.Combobox(self.__w, values=options)
        self.__dropdown_menu.place(x=150, y=300, width=170, height=30)

        self.__c.place(x=30, y=340)
        options = [ "Ambala", "Bhiwani", "Charkhi Dadri", "Faridabad", "Fatehabad", "Gurugram",
                  "Hisar", "Jhajjar", "Jind", "Kaithal", "Karnal", "Kurukshetra",
                   "Mahendragarh", "Nuh", "Palwal", "Panchkula", "Panipat",
                   "Rewari", "Rohtak", "Sirsa", "Sonipat", "Yamunanagar"]
        self.__dropdown_menu = ttk.Combobox(self.__w, values=options)
        self.__dropdown_menu.place(x=150, y=340, width=170, height=30)

        self.__ad.place(x=30, y=380)
        self.__ad1.place(x=150, y=380, width=170, height=30)

        self.__p.place(x=30, y=420)
        self.__p1.place(x=150, y=420, width=170, height=30)

        self.__cp.place(x=30, y=465)
        self.__cp1.place(x=150, y=460, width=170, height=30)

        self.__b1 = t.Button(text='Sign up', fg='yellow', bg='blue')
        self.__b1.place(x=150, y=510, width=120, height=40)
        self.__b1.bind('<Button-1>', self.valid)
        self.__w.mainloop()
#l1= Register()        