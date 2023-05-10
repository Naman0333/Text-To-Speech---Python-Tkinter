import tkinter as tk
import os
from gtts import gTTS
window = tk.Tk()

window.wm_iconbitmap('icon.ico')
window.title('Text to Speech')
window.geometry('400x250')
window.resizable(False,False)

def play():
    language = 'en'
    myobj = gTTS(
        text = text_input.get(),
        lang = language,
        slow = False
    )
    myobj.save('convert.wav')
    os.system('convert.wav')

headline = tk.Label(window, text='Text to Speech',font=("Arial",30,'bold'),bg='#78838f',fg='#ffffb3')
headline.pack(fill='x')

text_label = tk.Label(window,text='Enter the Text',font=('Arial',16,'bold'))
text_label.pack(pady=5)

text_input = tk.Entry(window,width=50)
text_input.pack(pady=5)

convert_button = tk.Button(window,width=20,text='Convert',font=('Arial',8,'bold'),bg='black',fg='white',command=play)
convert_button.pack(pady=5)



window.mainloop()
