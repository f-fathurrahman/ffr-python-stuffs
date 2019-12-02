# from https://stackoverflow.com/questions/37964605/arabic-text-in-tkinter
# not working

from tkinter import *

root = Tk()
root.title('Alram')
root.geometry("1500x600")

mytext= 'ذكرت تقارير' #Arabic text

msg = Message(root, bg="red", text= mytext, justify='right')

msg.config(font=('times', 72, 'bold'))

exit_button = Button(root, width=10, text='Exit', command=root.destroy)
exit_button.pack()

msg.pack(fill=X)

root.mainloop()