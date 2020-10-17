from tkinter import *
from tkinter import messagebox, StringVar
import glob
import os
top = Tk()

search_result_list = Listbox(top,width=50)
search_result_list.grid(row=2, column=0)  

file_path = "C:/search/"
top.title("Search keywords in "+ file_path + " path")
searchValue = StringVar()   

def openFileInWindow(event):     
    cs = search_result_list.get(search_result_list.curselection())
    if "Not Found" not in cs:
        os.system(cs)
 


def searchContent(): 
    os.chdir( file_path )  
    search_result_list.delete(0, END)
    found = False
    i = 0
    for file in glob.glob('*.*'):
        with open(file) as f:
            contents = f.read()
            if searchValue.get().lower() in file.lower() or searchValue.get().lower() in contents.lower():
                search_result_list.insert(i+1, (file_path + str(file)))
                found = True
    #messagebox.showinfo( "Hello Python", "Hello World")
    search_result_list.bind('<Double-1>', openFileInWindow) 
    if found is False:
        search_result_list.insert(i+1, "Not Found")
    
    


#top.bind('<Return>', searchContent)


if __name__ == '__main__':  
    top.geometry('400x200+100+200')
    text_box = Entry(top, textvariable=searchValue,width=25)
    text_box.grid(row=1, column=0) 
    search_button = Button(top, text ="Search",width=10, command = searchContent)
    search_button.grid(row=1, column=1)      
    top.mainloop()
    