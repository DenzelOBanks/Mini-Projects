import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Clock App")
root.geometry("400x100")

# The function for the clock
def clock():
   time = datetime.now().strftime('%H:%M:%S') 
   time_label.configure(text=time)

   root.after(1000,clock)


# Label widget to show the clock time
time_label = tk.Label(root, font="Helvetica, 25" )
time_label.pack(pady=20)

clock()
root.mainloop()