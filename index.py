from tkinter import *
from tkinter import messagebox, StringVar
from tkinter import ttk
import glob
import os
import webbrowser
top = Tk()

search_result_list = Listbox(top,width=50)
search_result_list.grid(row=1, column=0, sticky = W, columnspan = 3, padx=10, pady=10)  

file_path = "C:/search/"
top.title("Search keywords in "+ file_path + " path")
searchValue = StringVar()   

def openFileInWindow(event):     
    cs = search_result_list.get(search_result_list.curselection())
    if "Not Found" not in cs:
        #os.system(cs)
        webbrowser.open(file_path + cs)
 

def search_recursive(words, content):
    if (len(words)) > 0:
        search_word = words.pop().strip().lower()
        if  len(search_word)> 0 and search_word in content.lower():
            if (len(words)) > 0:                
                return search_recursive(words, content)
            else:
                return True
        else:
            return False
    else:
        return False




def searchContentEvent(event):
    searchContent()


def searchContent(): 
    os.chdir( file_path )  
    search_result_list.delete(0, END)
    found = False
    i = 0
    for file in glob.glob('*.*'):
        with open(file) as f:
            contents = f.read()            
            if search_recursive(searchValue.get().split(), file.lower()) or search_recursive(searchValue.get().split(), contents.lower()):
                 search_result_list.insert(i+1, (file))
                 found = True
         
    search_result_list.bind('<Double-1>', openFileInWindow) 
    if found is False:
        search_result_list.insert(i+1, "Not Found")


def writeFile (win, file_name, content):
    file = open(file_path + file_name.get() + ".txt",'a+')
    file.write(content.get("1.0", "end"))    
    file.close() 
    win.destroy()  
    
 
def createNewEntry():    
    win = Toplevel()
    win.wm_title("New content in new file :")    
    Label(win, text="File Name:",  width=50).grid(row=1,column=0, padx=10, pady=10)
    file_name = Entry(win,  width=50)
    file_name.grid(row=1, column=1, padx=10, pady=10)
    content = Text(win,  width=100)
    content.grid(row=2, column=0, sticky = W, columnspan = 2, padx=20, pady=20)
    b = ttk.Button(win, text="Save", command=lambda: writeFile(win, file_name, content))
    b.grid(row=3, column=0, sticky = W, columnspan = 2, padx=10, pady=10)
   

top.bind('<Return>', searchContentEvent)

if __name__ == '__main__':  
    top.geometry('400x300+100+200')
    text_box = Entry(top, textvariable=searchValue,width=30)
    text_box.grid(row=0, column=0, padx=5, pady=5)
    #text_box.bind("<Key>", searchContentEvent) 
    search_button = Button(top, text ="Search",width=5, command = searchContent)
    
    new_button = Button(top, text ="New",width=5, command = createNewEntry)
    search_button.grid(row=0, column=1, padx=5, pady=5)     
    new_button.grid(row=0,column=2, padx=5, pady=5)     
    top.mainloop()
    
