from email import message
from tkinter import *
from tkinter import messagebox
import pyttsx3
import json
from difflib import get_close_matches
#from PyDictionary import PyDictionary
#dictionary=PyDictionary()


engine=pyttsx3.init()

# get_close_matches(word,possibilities,sequence,n,cutoff)

#get_close_matches('apple')


##functionality part

def search():
    data=json.load(open('data.json'))
    word=entryField.get()
    textarea.delete(0.0,END)


    if word in data:
        textarea.config(state=NORMAL)

        for meaning in data[word]:
            textarea.insert(END,U'\u2022'+meaning + '\n \n')  ##U'\u2022' use for buletin symbol
        textarea.config(state=DISABLED)

    elif len(get_close_matches(word,data.keys()))>0:
        best_match=get_close_matches(word,data.keys())[0]
        result=messagebox.askyesno('Conform',f'did you mean {best_match[0]} instead?')
        if result==True:   # true hoga to sahi kare ga meaning ko
            entryField.delete(0,END)  # worng meaning delete
            entryField.insert(0,best_match)  # sahi kare ga meaning
            textarea.config(state=NORMAL)

            for m in data[best_match]:
                textarea.insert(END,u'\u2022'+m+' \n\n')  # insert in meaning test filed
            textarea.config(state=DISABLED)


        else:
            closest_matches=get_close_matches(word,data.keys())
            #print(closest_matches)
            result = messagebox.askyesno('Conform', f'did you mean {best_match[0]} instead?')
            if result == True:  # true hoga to sahi kare ga meaning ko
                entryField.delete(0, END)  # worng meaning delete
                entryField.insert(0, closest_matches[1])  # sahi kare ga meaning

                for m in data[closest_matches[1]]:
                    textarea.insert(END, u'\u2022' + m + ' \n\n')  # insert in meaning test filed


            else:

                 messagebox.showerror('Error','please double checknthe word,it doesnt exist')


    else:
        print('word doesnot exist')





def meaningAudio():
    data_set=textarea.get(0.0,END)
    engine.say(data_set)
    engine.runAndWait()


def wordAudio():
    data=entryField.get()
    engine.say(data)
    engine.runAndWait()

def clear():  ## clear ka functinality
    textarea.config(state=NORMAL)
    textarea.delete(0.0,END)
    entryField.delete(0,END)
    textarea.config(state=DISABLED)

def exit_window():
    result =messagebox.askyesno('conform','Do you want to exit?')
    if result==True:
     root.destroy()



root = Tk()
root.title("Dictionary Create By Rohit") ##title use its line.
root.geometry("1000x626+10+30")
root.resizable(0,0)  ## minimize button hide.
bgimg=PhotoImage(file='background.png')
bglabel=Label(root,image=bgimg)
bglabel.pack()
wordlabel=Label(root,text=("ENTER WORD"),font=('castell',29,'bold'),fg='red3') ##text table create
wordlabel.place(x=530,y=20)
entryField=Entry(root,font=('arial',23,'bold'),bd=4,relief=RIDGE,justify='center')
#entryField.focus
entryField.place(x=510,y=80)
searchImage=PhotoImage(file='Search.png')
searchButton=Button(root,image=searchImage,bd=0,cursor='hand2',command=search)
searchButton.place(x=620,y=150)

micImage=PhotoImage(file='mic1.png')
micButton=Button(root,image=micImage,bd=0,cursor='hand2',command=wordAudio)
micButton.place(x=710,y=153)
meaningLabel=Label(root,text=('MEANING'),font=("castell",29,'bold'),fg='red3')
meaningLabel.place(x=580,y=240)
textarea=Text(root,font=('Arial',17,'bold'),width=34,height=8,bd=8,relief=GROOVE,wrap='word',state=DISABLED)
textarea.place(x=460,y=300)

microphoneImage=PhotoImage(file='microphone.png')
microphoneButton=Button(root,image=microphoneImage,bd=0,cursor='hand2',command=meaningAudio)
microphoneButton.place(x=530,y=555)

clearImage=PhotoImage(file='clear.png')
clearButton=Button(root,image=clearImage,bd=0,cursor='hand2',command=clear)
clearButton.place(x=660,y=555)


exitImage=PhotoImage(file='Exit.png')
exitButton=Button(root,image=exitImage,bd=0,cursor='hand2',command=exit_window)
exitButton.place(x=790,y=555)


root.mainloop()