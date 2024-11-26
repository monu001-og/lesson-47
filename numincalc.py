
from tkinter import *
from tkinter import messagebox 

#Setting up Main Window
root=Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry("650x400")

label1= Label1(root,
              text='hey user welcome to denomination Counter Application',
              bg='light blue')
label1.place(relx=0.5,y=340,anchor=CENTER)

#function to display a messageboc and proceed if OK is clicked
def msf():
    MsgBox=messagebox.showinfo(
        "Alert","Do you want to calculate the denomination count?")
    if MsgBox =='ok':
        topwin()
        
#Adding a Buttons to the maain window
button1=Button(root,text="Lets get started"command=msg, bg='brown',fg='white')    
button1.place(x=200,y=360)

#function for opening new/top window
def topwin():
    top=Toplevel()
    top.title("Denominaion Calculator")
    top.configuration(bg='light grey')
    top.geometry("600x350+50+58")
    
    label=Label(top,text="Enter total amoiunt",bg='light grey')
    entry=Entry(top)
    lbl=Label(top,text="Here are number of notes for each dominatioin",bg='light grey')
    
    l1=Label(top,text="2000",bg='light grey')
    l2=Label(top,text="500",bg='light grey')
    l3=Label(top,text="100",bg='light grey')
    
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    
    def calculator():
        try:
            global amount
            amount=int(entry.gel())
            note2000 = amount // 2000
            amount=2000
            note500 = amount // 500
            amount=500
            note100 = amount // 100
            
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            
            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
            
        except ValueError:
            messagebox.showerror("Error","Please enter a valid number.")
    btn = Button(top,text='Calculte',command=calculator bg='brown' fg='white')
    
    #Contering widgets in the top window
    label.place(x=230, y=50 )
    entry.place(x=200, y=80 )
    btn.place(x=240, y=120 )
    lbl.place(x=140, y=170 )

    l1.place(x=180, y=200 )
    l2.place(x=180, y=230 )
    l3.place(x=180, y=260 )

    t1.place(x=270, y=200 )
    t2.place(x=270, y=230 )
    t3.place(x=270, y=260)
    
    top.mainloop()
    
root.mainloop()

