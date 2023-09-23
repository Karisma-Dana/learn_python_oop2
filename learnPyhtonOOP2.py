# aplikasi undian no absen 
import tkinter as tk 
import random
import numpy as np
from tkinter import messagebox



def show_first(): 
    user_input1 = user1.get()
    user_input2 = user2.get()
    try :
        global n_list
        global n_first 
        global n_second
        
        n_first = int(user_input1) 
        n_second = int(user_input2) + 1
        if n_first or n_second >= 1 : 
            n_list = list(np.arange(n_first,n_second))
        else : 
            n_list = list(np.arange(n_first,n_second,-1))
        show_second()

    except ValueError : 
       messagebox.showerror("Error", "Input harus berupa angka integer.")



def show_second(): 
    second_root = tk.Toplevel(root)
    second_root.geometry("150x100")
    second_root.resizable(False,False)

    label_second = tk.Label(second_root,text="random execution")
    label_second.pack()
    button_execution = tk.Button(second_root,text="random click",command=final_execution)
    button_execution.pack()

    global label_final
    label_final = tk.Label(second_root,text="")
    label_final.pack()


def final_execution(): 
    if len(n_list) == 0 : 
        label_final.config(text="your number are up")

    else : 
        random_number = random.choice(n_list)
        n_list.remove(random_number)
        label_final.config(text=f"{random_number}")


"""""tampilan tkinter"""
root = tk.Tk()
root.title("Undian nomber acak")
root.geometry("200x150")
root.resizable(False,False)


"""""input user show"""
labe1 = tk.Label(root,text="masukan angka awal")
labe1.pack()
user1 = tk.Entry(root)
user1.pack()
labe2 = tk.Label(root,text="sampai rentang angka ke")
labe2.pack()
user2 = tk.Entry(root)
user2.pack()


"""""tombol peralihan"""
button1 = tk.Button(root,text="eksekusi",command=show_first)
button1.pack()


    
root.mainloop()



