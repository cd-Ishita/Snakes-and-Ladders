from tkinter import *

window=Tk()

list1 = []
border1 = []

list1.append(Label(window, text = "1",padx = 25, pady = 22, borderwidth = 2, relief="groove"))
list1[0].grid(row=0, column=0)
for i in range(1,100):
    border1.append(LabelFrame(window))
    if i//10 == 0:
        list1.append(Label(window, text = i+1, padx = 25, pady=22, borderwidth=2, relief="groove"))
        list1[i].grid(row=i//10, column=(i%10))
    else:
        list1.append(Label(window, text = i+1, borderwidth=2, padx = 22, pady = 22, relief="groove"))
        list1[i].grid(row=i//10, column=(i%10))
    #border1[i-1].pack(padx = 10, pady = 10)
    #list1[i-1].pack()


window.mainloop()