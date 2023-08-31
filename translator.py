from tkinter import ttk
from tkinter import *
from googletrans import Translator, LANGUAGES

# * Creating the display window and environment.
root = Tk()
root.geometry(“1080×400”)
root.resizable(0,0)
root.config(bg = “ghost white”)
root.title(“Language Translator”)
Label(root, text = “Language Translator”, font = “Georgia 24 bold”, bg = “white smoke”).pack()
Label(root,text =”Made By – (Enter your name”), font = ‘Georgia 15 bold’, bg =’white smoke’ , width = ’20’).pack(side = ‘bottom’)

# – Creating the input/output text.
Label(root, text = “Input”, font = ‘Georgia 15 bold’, bg = ‘white smoke’).place(x = 20, y = 60)
input = Text(root, font = ‘Georgia 12’, height = 11, wrap = WORD, padx = 5, pady = 5, width = 60)
input.place(x = 30, y = 100)
Label(root, text = “Output”, font = ‘Georgia 15 bold’, bg = ‘white smoke’).place(x = 795, y = 60)
output = Text(root, font = ‘Georgia 12’, height = 11, wrap = WORD, padx = 5, pady = 5, width = 60)
output.place(x = 540, y = 100)

# ! Defining the language selection.
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values = language, width = 22)
src_lang.place(x = 100, y = 65)
src_lang.set(‘Choose input language’)
dest_lang = ttk.Combobox(root, values = language, width = 22)
dest_lang.place(x = 890, y = 65)
dest_lang.set(‘Choose output language’)

# / Define function.
def Translate():
translator = Translator()
translated=translator.translate(text= input.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
output.delete(1.0, END)
output.insert(END, translated.text)

# . Create the translate button.
translate_btn = Button(root, text = ‘Translate’, font = ‘Georgia 12 bold’, pady = 5, command = Translate, bg = ‘white smoke’, activebackground = ‘white smoke’)
translate_btn.place(x = 490, y = 300)

# : Run main loop.
root.mainloop()















root.configure(bg="white")
root.mainloop()


