import qrcode
from tkinter import filedialog
from tkinter import *

def make_qrcode():
    test = qrcode.make(url_ori.get(),)
    test.save(f'{save_dir}/{nome.get()}.png')

def folder_selected():
    loc = filedialog.askdirectory()
    return loc

window = Tk()
window.geometry('500x200')
window.title('QR CODE')
window.configure(background='#dde')

text = Label(window, text="Insert the URL and the file name: ", background='#dde')
text.place(x=166, y=10)

url_ori = Entry(window, width=60)
url_ori.place(x=80, y=50)

nome = Entry(window, width=60)
nome.place(x=80, y=80)
    
# save_dir = Button(window, text='Directory', command=folder_selected)
# save_dir.place(x = 227, y=100)
save_dir = folder_selected()

download = Button(window, text='Download', command=make_qrcode)
download.place(x=227,y=140)

window.mainloop()