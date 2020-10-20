from tkinter import *
class game:
    def __init__(self,root):
    	
    	#Making Main Frame in which whole page will ccome in existence
        self.base=Frame(root,width =1400, height = 50, bg = 'grey',padx=10,pady=10)
        self.base.propagate(0)
        time = Label(self.base,text="Time",bg='grey',font=("Verdana",15),fg='orange',padx = 300)
        control = Label(self.base,text="Controls",bg='grey',font=("Verdana",15),fg='orange',padx = 300)
        time.pack(side = 'left')
        control.pack(side = 'right')
        self.base.pack(fill=X)

        #Make gap between top label and sudoku grid or we can use place instead of this 
        self.gap = Frame(root,height=100)
        self.gap.pack()

        #this is frame for the grid so the grid can exit
        self.for_grid_frame = Frame(root,width = 50, height = 50 )
        for i in range(9):
            for j in range(9):
                frame = Frame(self.for_grid_frame, relief=RAISED, borderwidth=2)
                frame.grid(row=i, column=j, padx=0.5, pady=0.5)
        
                if(i==0 and j==0):
                    user_input=Entry(master=frame,width = 2,font=("Verdana",20),fg='blue',text=" ")
                    user_input.configure(bg="white", insertbackground='white')
                    user_input.pack()
                else:
                    fixed_input = Label(master=frame,height = 1,width = 2,text=f"8",font=("Verdana",16,'bold'), fg = "black",padx = 5 , pady =5) 
                    fixed_input.pack()
        
        self.for_grid_frame.pack(after = self.gap,anchor = 'w',padx='300')
        
        #here the big buttons came with their placement
        normal = Button(text = "Normal" , fg='purple' , font=("Verdana",14,'bold'),width = 7)
        corner = Button(text = "Corner" , fg='purple' , font=("Verdana",14,'bold'),width = 7) 
        center = Button(text = "Center" , fg='purple' , font=("Verdana",14,'bold'),width = 7)
        colour = Button(text = "Colour" , fg='purple' , font=("Verdana",14,'bold'),width = 7)
        delete = Button(text = "Delete" , fg='purple' , font=("Verdana",14,'bold'),width = 12)
        undo = Button(text = "Undo" , fg='purple' , font=("Verdana",14,'bold'),width = 10)
        redo = Button(text = "Redo" , fg='purple' , font=("Verdana",14,'bold'),width = 10)
        restart = Button(text = "Restart" , fg='purple' , font=("Verdana",14,'bold'),width = 10)
        check = Button(text = "Check" , fg='purple' , font=("Verdana",14,'bold'),width = 10)
        normal.place(x=875,y=200)
        corner.place(x=875,y=250)
        center.place(x=875,y=300)
        colour.place(x=875,y=350)
        delete.place(x=1002,y=350)
        undo.place(x=875,y=400)
        redo.place(x=1025,y=400)
        restart.place(x=875,y=450)
        check.place(x=1025,y=450)

        #here no and their placement are their.  
        no1 = Button(text = "1" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no2 = Button(text = "2" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no3 = Button(text = "3" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no4 = Button(text = "4" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no5 = Button(text = "5" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no6 = Button(text = "6" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no7 = Button(text = "7" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no8 = Button(text = "8" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no9 = Button(text = "9" , fg='white' , bg ='purple' , font=("Verdana",14,'bold'),height = 1,width = 3)
        no1.place(x=1000,y=200)
        no2.place(x=1060,y=200)
        no3.place(x=1120,y=200)
        no4.place(x=1000,y=250)
        no5.place(x=1060,y=250)
        no6.place(x=1120,y=250)
        no7.place(x=1000,y=300)
        no8.place(x=1060,y=300)
        no9.place(x=1120,y=300)
        
        # to give the frame some weight to look better
        self.gap = Frame(root,height=200)
        self.gap.pack()

        # other functions or topics to do
        def get_entries_from_user():
            pass
        def ans_valiadtor():
            pass
        def others():
            pass

# the starting of tkinter
root = Tk()
obj = game(root)
root.title("Sudoku! Lets Play ")
root.mainloop()
