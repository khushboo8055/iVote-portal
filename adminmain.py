import tkinter as tk
import mysql.connector as ms

class adminmain:
    def __init__(self):
        self.__w = tk.Tk()
        self.__w.title("Voting Results")
        
        w = 400
        h = 400
        x = self.__w.winfo_screenwidth() // 2 - w // 2
        y = self.__w.winfo_screenheight() // 2 - h // 2
        self.__w.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        
        # Establish database connection
        connectiondb = ms.connect(user='root', password='Khushboo@123', host='localhost', database='votingdb')
        cur = connectiondb.cursor()
        cur.execute('SELECT party, COUNT(*) AS total_voter FROM voter WHERE party IS NOT NULL GROUP BY party ORDER BY total_voter DESC')
        res = cur.fetchall()
        party=tk.Label(text='Party')
        Total_voter=tk.Label(text='Totalvoter')
        party.grid(row=0,column=0)
        Total_voter.grid(row=0,column=1)
        # Display results in labels
        for i, (party, total_voter) in enumerate(res):
            labelp = tk.Label( text=party)
            labelv = tk.Label(text=total_voter)
            labelp.grid(row=i+1, column=0)
            labelv.grid(row=i+1, column=1)
        connectiondb.close()  # Close database connection
        
        self.__w.mainloop()

# Create an instance of adminmain to run the application
#a1 = adminmain()
