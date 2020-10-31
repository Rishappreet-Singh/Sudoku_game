from tkinter import *
import random
from tkinter import messagebox as msg

class game:
    def __init__(self,root):
        #getting random values at random places
        list1 = [[0,0,0,0,0,0,0,0,0] for j in range(9)]
        for i in range (9):
            j=random.randint(2,4)
            temp = []
            coloumn = []
            while True :
                l = random.randint(1,9)
                if l not in temp:
                    temp.append(l)
                if len(temp) == j:
                    break
            
            while True:
                l = random.randint(0,8)
                if l not in coloumn:
                    coloumn.append(l)
                if len(coloumn) == j:
                    break
            index=0
            for kl in temp:
                vr = coloumn[index]
                list1[i][vr] = kl
                index+=1
        
        temp = 0
        for i in range(9):
            for j in range(9):
                if(list1[i][j]!=0):
                    temp = list1[i][j]
                    for m in range(9):
                        if (temp == list1[m][j] and i!=m):
                            list1[m][j]=0
                            break 
                        else :    
                            if(i<3 and j<3):
                                for k in range(3):
                                    for l in range(3):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 
                                                
                            elif(i<3 and j<6):
                                for k in range(3):
                                    for l in range(3,6):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 
                            
                            elif (i<3 and j<9):
                                for k in range(3):
                                    for l in range(6,9):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 
                                
                            elif (i<6 and j<3):
                                for k in range(3,6):
                                    for l in range(3):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 
                            
                            elif (i<6 and j<6):                   
                                for k in range(3,6):
                                    for l in range(3,6):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 

                            elif (i<6 and j<9):
                                for k in range(3,6):
                                    for l in range(6,9):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 
                            
                            elif (i<9 and j<3):
                                for k in range(6,9):
                                    for l in range(3):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 
                            
                            elif (i<9 and j<6):
                                for k in range(6,9):
                                    for l in range(3,6):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break 
                            
                            elif (i<9 and j<9):
                                for k in range(6,9):
                                    for l in range(6,9):                            
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            list1[i][j]=0
                                            break             
        
        #initializing the values 
        self.sudoku_values = [[0,0,0,0,0,0,0,0,0,0] for i in range(9)]
        self.entry_in_index01 = IntVar()
        self.entry_in_index02 = IntVar()
        self.entry_in_index03 = IntVar()
        self.entry_in_index04 = IntVar()
        self.entry_in_index05 = IntVar()
        self.entry_in_index06 = IntVar()
        self.entry_in_index07 = IntVar()
        self.entry_in_index08 = IntVar()
        self.entry_in_index09 = IntVar()
                
        self.entry_in_index11 = IntVar()
        self.entry_in_index12 = IntVar()
        self.entry_in_index13 = IntVar()
        self.entry_in_index14 = IntVar()
        self.entry_in_index15 = IntVar()
        self.entry_in_index16 = IntVar()
        self.entry_in_index17 = IntVar()
        self.entry_in_index18 = IntVar()
        self.entry_in_index19 = IntVar()
                
        self.entry_in_index21 = IntVar()
        self.entry_in_index22 = IntVar()
        self.entry_in_index23 = IntVar()
        self.entry_in_index24 = IntVar()
        self.entry_in_index25 = IntVar()
        self.entry_in_index26 = IntVar()
        self.entry_in_index27 = IntVar()
        self.entry_in_index28 = IntVar()
        self.entry_in_index29 = IntVar()
                
        self.entry_in_index31 = IntVar()
        self.entry_in_index32 = IntVar()
        self.entry_in_index33 = IntVar()
        self.entry_in_index34 = IntVar()
        self.entry_in_index35 = IntVar()
        self.entry_in_index36 = IntVar()
        self.entry_in_index37 = IntVar()
        self.entry_in_index38 = IntVar()
        self.entry_in_index39 = IntVar()
                
        self.entry_in_index41 = IntVar()
        self.entry_in_index42 = IntVar()
        self.entry_in_index43 = IntVar()
        self.entry_in_index44 = IntVar()
        self.entry_in_index45 = IntVar()
        self.entry_in_index46 = IntVar()
        self.entry_in_index47 = IntVar()
        self.entry_in_index48 = IntVar()
        self.entry_in_index49 = IntVar()
                
        self.entry_in_index51 = IntVar()
        self.entry_in_index52 = IntVar()
        self.entry_in_index53 = IntVar()
        self.entry_in_index54 = IntVar()
        self.entry_in_index55 = IntVar()
        self.entry_in_index56 = IntVar()
        self.entry_in_index57 = IntVar()
        self.entry_in_index58 = IntVar()
        self.entry_in_index59 = IntVar()
                
        self.entry_in_index61 = IntVar()
        self.entry_in_index62 = IntVar()
        self.entry_in_index63 = IntVar()
        self.entry_in_index64 = IntVar()
        self.entry_in_index65 = IntVar()
        self.entry_in_index66 = IntVar()
        self.entry_in_index67 = IntVar()
        self.entry_in_index68 = IntVar()
        self.entry_in_index69 = IntVar()
                
        self.entry_in_index71 = IntVar()
        self.entry_in_index72 = IntVar()
        self.entry_in_index73 = IntVar()
        self.entry_in_index74 = IntVar()
        self.entry_in_index75 = IntVar()
        self.entry_in_index76 = IntVar()
        self.entry_in_index77 = IntVar()
        self.entry_in_index78 = IntVar()
        self.entry_in_index79 = IntVar()
                
        self.entry_in_index81 = IntVar()
        self.entry_in_index82 = IntVar()
        self.entry_in_index83 = IntVar()
        self.entry_in_index84 = IntVar()
        self.entry_in_index85 = IntVar()
        self.entry_in_index86 = IntVar()
        self.entry_in_index87 = IntVar()
        self.entry_in_index88 = IntVar()
        self.entry_in_index89 = IntVar()

        #Making Main Frame
        self.base=Frame(root,width =1400, height = 50, bg = '#90A4AE',padx=10,pady=10)
        self.base.propagate(0)

        #the guide module for beginners
        def help():
            top = Tk()
            top.resizable(width=False, height=False)
            top.title("Help Section")
            top.rowconfigure(0, minsize=430, weight=1)
            top.columnconfigure(1, minsize=850, weight=1)

            txt_edit = Text(top)
            min_frame = Frame(top, relief=RAISED, bd=2)
            head1 = Label(min_frame, text="The Rules of  \nSudoku :",font=("Verdana", 10,'bold'))
            head2 = Label(min_frame, text="\n\n\n\n\n\n\n\n\n\n\n\nHow to play \nSudoku :",font=("Verdana", 10,'bold'))

            head1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
            head2.grid(row=1, column=0, sticky="ew", padx=5)

            min_frame.grid(row=0, column=0, sticky="ns")
            txt_edit.grid(row=0, column=1, sticky="nsew")
            txt_edit.insert(1.0,'''The classic Sudoku game involves a grid of 81 squares.,
The grid is divided into nine blocks, each containing nine squares.\n
The rules of the game are simple: each of the nine blocks has to
contain all the numbers 1-9 within its squares.
Each number can only appear once in a row, column or box.\n
The difficulty lies in that each vertical nine-square column, or 
horizontal nine-square line across, within the larger square, 
must also contain the numbers 1-9, without repetition or omission.\n
Every puzzle has just one correct solution.\n
---------------------------------------------------------------------------------------------------------\n
The goal of Sudoku is to fill in a 9×9 grid with digits so that each column, row, and 3×3 section 
contain the numbers between 1 to 9. At the beginning of the game, the 9×9 grid will have some of 
the squares filled in.Your job is to use logic to fill in the missing digits and complete the grid.
Don’t forget, a move is incorrect if:\n
      •Any row contains more than one of the same number from 1 to 9
      •Any column contains more than one of the same number from 1 to 9
      •Any 3×3 grid contains more than one of the same number from 1 to 9\n
Sudoku is a fun puzzle game once you get the hang of it 😍❤!
            ''')
            top.mainloop()
        button = Button(self.base, text="HELP", command=help,bg='#90A4AE',padx=275 ,font=("Verdana", 20,"underline"), fg='#FFCA28',relief = 'flat',cursor = 'hand2')
        button.pack(side= 'left')

        check = Button(self.base, text = "Check" , fg='#FFCA28',bg='#90A4AE', relief = 'flat' , font=("Verdana",20,"underline"),width = 10,cursor = 'hand2',command = self.checker)
        check.pack()
        self.base.pack(fill=X)

        #Make gap between top label and sudoku grid 
        self.gap = Frame(root,height=100)
        self.gap.pack()

        title0 =Label(master= root,text ='S', font=("French Script MT", 50), fg= 'green')
        title0.place(x=1050,y=125)
        title1 =Label(master= root,text ='U', font=("French Script MT", 50), fg= 'green')
        title1.place(x=1050,y=200)
        title2 =Label(master= root,text ='D', font=("French Script MT", 50), fg= 'green')
        title2.place(x=1050,y=275)
        title3 =Label(master= root,text ='O', font=("French Script MT", 50), fg= 'green')
        title3.place(x=1050,y=350)
        title4 =Label(master= root,text ='K', font=("French Script MT", 50), fg= 'green')
        title4.place(x=1050,y=425)
        title5 =Label(master= root,text ='U', font=("French Script MT", 50), fg= 'green')
        title5.place(x=1050,y=500)
        title6 =Label(master= root,text ="Let's", font=("French Script MT", 70), fg= 'green')
        title6.place(x=55,y=200)
        title7 =Label(master= root,text ='Play', font=("French Script MT", 70), fg= 'green')
        title7.place(x=135,y=325)
        
        #this is for pattern of sudoku
        self.for_grid_frame = Frame(root,width = 50, height = 800 )
        
        def checkered(canvas, line_distance):
            # vertical lines at an interval of "line_distance" pixel
            for x in range(line_distance,440,line_distance):
                canvas.create_line(x+40, 80, x+40, 440, fill="#476042")
            # horizontal lines at an interval of "line_distance" pixel
            for y in range(line_distance,440,line_distance):
                canvas.create_line(80, y+40, 440, y+40, fill="#476042")
            #rectangle
            canvas.create_rectangle(80,80,440,440)
            canvas.create_rectangle(79,79,441,441)
            canvas.create_rectangle(78,78,442,442)
            #1st line
            canvas.create_line(199,80,199,440)
            canvas.create_line(200,80,200,440)
            canvas.create_line(201,80,201,440)
            #2nd line
            canvas.create_line(319,80,319,440)
            canvas.create_line(320,80,320,440)
            canvas.create_line(321,80,321,440)
            #3rd line
            canvas.create_line(80,199,440,199)
            canvas.create_line(80,200,440,200)
            canvas.create_line(80,201,440,201)
            #4th line
            canvas.create_line(80,319,440,319)
            canvas.create_line(80,320,440,320)
            canvas.create_line(80,321,440,321)
            
            # this is the row no 0
            self.entry_in_index01 = Text(master = canvas , width = 2 , font=("Verdana", 20), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index02 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index03 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index04 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index05 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index06 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index07 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index08 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index09 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index01.insert(1.0, ' ')
            self.entry_in_index02.insert(1.0, ' ')
            self.entry_in_index03.insert(1.0, ' ')
            self.entry_in_index04.insert(1.0, ' ')
            self.entry_in_index05.insert(1.0, ' ')
            self.entry_in_index06.insert(1.0, ' ')
            self.entry_in_index07.insert(1.0, ' ')
            self.entry_in_index08.insert(1.0, ' ')
            self.entry_in_index09.insert(1.0, ' ')

            # this is the row no 1
            self.entry_in_index11 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index12 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index13 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index14 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index15 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index16 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index17 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index18 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index19 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index11.insert(1.0, ' ')
            self.entry_in_index12.insert(1.0, ' ')
            self.entry_in_index13.insert(1.0, ' ')
            self.entry_in_index14.insert(1.0, ' ')
            self.entry_in_index15.insert(1.0, ' ')
            self.entry_in_index16.insert(1.0, ' ')
            self.entry_in_index17.insert(1.0, ' ')
            self.entry_in_index18.insert(1.0, ' ')
            self.entry_in_index19.insert(1.0, ' ')

            # this is the row no 2
            self.entry_in_index21 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index22 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index23 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index24 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index25 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index26 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index27 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index28 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index29 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index21.insert(1.0, ' ')
            self.entry_in_index22.insert(1.0, ' ')
            self.entry_in_index23.insert(1.0, ' ')
            self.entry_in_index24.insert(1.0, ' ')
            self.entry_in_index25.insert(1.0, ' ')
            self.entry_in_index26.insert(1.0, ' ')
            self.entry_in_index27.insert(1.0, ' ')
            self.entry_in_index28.insert(1.0, ' ')
            self.entry_in_index29.insert(1.0, ' ')
            
            # this is the row no 3
            self.entry_in_index31 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index32 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index33 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index34 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index35 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index36 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index37 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index38 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index39 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index31.insert(1.0, ' ')
            self.entry_in_index32.insert(1.0, ' ')
            self.entry_in_index33.insert(1.0, ' ')
            self.entry_in_index34.insert(1.0, ' ')
            self.entry_in_index35.insert(1.0, ' ')
            self.entry_in_index36.insert(1.0, ' ')
            self.entry_in_index37.insert(1.0, ' ')
            self.entry_in_index38.insert(1.0, ' ')
            self.entry_in_index39.insert(1.0, ' ')

            # this is the row no 4
            self.entry_in_index41 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index42 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index43 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index44 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index45 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index46 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index47 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index48 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index49 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')

            self.entry_in_index41.insert(1.0, ' ')
            self.entry_in_index42.insert(1.0, ' ')
            self.entry_in_index43.insert(1.0, ' ')
            self.entry_in_index44.insert(1.0, ' ')
            self.entry_in_index45.insert(1.0, ' ')
            self.entry_in_index46.insert(1.0, ' ')
            self.entry_in_index47.insert(1.0, ' ')
            self.entry_in_index48.insert(1.0, ' ')
            self.entry_in_index49.insert(1.0, ' ')

            # this is the row no 5
            self.entry_in_index51 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index52 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index53 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index54 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index55 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index56 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index57 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index58 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index59 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index51.insert(1.0, ' ')
            self.entry_in_index52.insert(1.0, ' ')
            self.entry_in_index53.insert(1.0, ' ')
            self.entry_in_index54.insert(1.0, ' ')
            self.entry_in_index55.insert(1.0, ' ')
            self.entry_in_index56.insert(1.0, ' ')
            self.entry_in_index57.insert(1.0, ' ')
            self.entry_in_index58.insert(1.0, ' ')
            self.entry_in_index59.insert(1.0, ' ')

            # this is the row no 6
            self.entry_in_index61 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index62 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index63 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index64 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index65 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index66 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index67 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index68 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index69 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index61.insert(1.0, ' ')
            self.entry_in_index62.insert(1.0, ' ')
            self.entry_in_index63.insert(1.0, ' ')
            self.entry_in_index64.insert(1.0, ' ')
            self.entry_in_index65.insert(1.0, ' ')
            self.entry_in_index66.insert(1.0, ' ')
            self.entry_in_index67.insert(1.0, ' ')
            self.entry_in_index68.insert(1.0, ' ')
            self.entry_in_index69.insert(1.0, ' ')

            # this is the row no 7
            self.entry_in_index71 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index72 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index73 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index74 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index75 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index76 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index77 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index78 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index79 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index71.insert(1.0, ' ')
            self.entry_in_index72.insert(1.0, ' ')
            self.entry_in_index73.insert(1.0, ' ')
            self.entry_in_index74.insert(1.0, ' ')
            self.entry_in_index75.insert(1.0, ' ')
            self.entry_in_index76.insert(1.0, ' ')
            self.entry_in_index77.insert(1.0, ' ')
            self.entry_in_index78.insert(1.0, ' ')
            self.entry_in_index79.insert(1.0, ' ')

            # this is the row no 8
            self.entry_in_index81 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index82 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index83 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index84 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index85 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index86 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index87 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index88 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            self.entry_in_index89 = Text(master = canvas , width = 2 , font=("Verdana", 19), fg= '#1D6AE5',height = 1,cursor= 'arrow')
            
            self.entry_in_index81.insert(1.0, ' ')
            self.entry_in_index82.insert(1.0, ' ')
            self.entry_in_index83.insert(1.0, ' ')
            self.entry_in_index84.insert(1.0, ' ')
            self.entry_in_index85.insert(1.0, ' ')
            self.entry_in_index86.insert(1.0, ' ')
            self.entry_in_index87.insert(1.0, ' ')
            self.entry_in_index88.insert(1.0, ' ')
            self.entry_in_index89.insert(1.0, ' ')
            
            #placing the entring boxex
            self.entry_in_index01.place(x=82,y=82)
            self.entry_in_index02.place(x=122,y=82)
            self.entry_in_index03.place(x=162,y=82)
            self.entry_in_index04.place(x=203,y=82)
            self.entry_in_index05.place(x=242,y=82)
            self.entry_in_index06.place(x=282,y=82)
            self.entry_in_index07.place(x=323,y=82)
            self.entry_in_index08.place(x=362,y=82)
            self.entry_in_index09.place(x=402,y=82)

            self.entry_in_index11.place(x=82,y=122)
            self.entry_in_index12.place(x=122,y=122)
            self.entry_in_index13.place(x=162,y=122)
            self.entry_in_index14.place(x=203,y=122)
            self.entry_in_index15.place(x=242,y=122)
            self.entry_in_index16.place(x=282,y=122)
            self.entry_in_index17.place(x=323,y=122)
            self.entry_in_index18.place(x=362,y=122)
            self.entry_in_index19.place(x=402,y=122)

            self.entry_in_index21.place(x=82,y=162)
            self.entry_in_index22.place(x=122,y=162)
            self.entry_in_index23.place(x=162,y=162)
            self.entry_in_index24.place(x=203,y=162)
            self.entry_in_index25.place(x=242,y=162)
            self.entry_in_index26.place(x=282,y=162)
            self.entry_in_index27.place(x=323,y=162)
            self.entry_in_index28.place(x=362,y=162)
            self.entry_in_index29.place(x=402,y=162)

            self.entry_in_index31.place(x=82,y=203)
            self.entry_in_index32.place(x=122,y=203)
            self.entry_in_index33.place(x=162,y=203)
            self.entry_in_index34.place(x=203,y=203)
            self.entry_in_index35.place(x=242,y=203)
            self.entry_in_index36.place(x=282,y=203)
            self.entry_in_index37.place(x=323,y=203)
            self.entry_in_index38.place(x=362,y=203)
            self.entry_in_index39.place(x=402,y=203)

            self.entry_in_index41.place(x=82,y=242)
            self.entry_in_index42.place(x=122,y=242)
            self.entry_in_index43.place(x=162,y=242)
            self.entry_in_index44.place(x=203,y=242)
            self.entry_in_index45.place(x=242,y=242)
            self.entry_in_index46.place(x=282,y=242)
            self.entry_in_index47.place(x=323,y=242)
            self.entry_in_index48.place(x=362,y=242)
            self.entry_in_index49.place(x=402,y=242)
            
            self.entry_in_index51.place(x=82,y=282)
            self.entry_in_index52.place(x=122,y=282)
            self.entry_in_index53.place(x=162,y=282)
            self.entry_in_index54.place(x=203,y=282)
            self.entry_in_index55.place(x=242,y=282)
            self.entry_in_index56.place(x=282,y=282)
            self.entry_in_index57.place(x=323,y=282)
            self.entry_in_index58.place(x=362,y=282)
            self.entry_in_index59.place(x=402,y=282)

            self.entry_in_index61.place(x=82,y=323)
            self.entry_in_index62.place(x=122,y=322)
            self.entry_in_index63.place(x=162,y=323)
            self.entry_in_index64.place(x=203,y=323)
            self.entry_in_index65.place(x=242,y=323)
            self.entry_in_index66.place(x=282,y=323)
            self.entry_in_index67.place(x=323,y=323)
            self.entry_in_index68.place(x=362,y=323)
            self.entry_in_index69.place(x=402,y=323)

            self.entry_in_index71.place(x=82,y=362)
            self.entry_in_index72.place(x=122,y=362)
            self.entry_in_index73.place(x=162,y=362)
            self.entry_in_index74.place(x=203,y=362)
            self.entry_in_index75.place(x=242,y=362)
            self.entry_in_index76.place(x=282,y=362)
            self.entry_in_index77.place(x=323,y=362)
            self.entry_in_index78.place(x=362,y=362)
            self.entry_in_index79.place(x=402,y=362)

            self.entry_in_index81.place(x=82,y=402)
            self.entry_in_index82.place(x=122,y=402)
            self.entry_in_index83.place(x=162,y=402)
            self.entry_in_index84.place(x=203,y=402)
            self.entry_in_index85.place(x=242,y=402)
            self.entry_in_index86.place(x=282,y=402)
            self.entry_in_index87.place(x=323,y=402)
            self.entry_in_index88.place(x=362,y=402)
            self.entry_in_index89.place(x=402,y=402)

            #Putting that Random values on interface
            def com_random_values(wl,vol):
                canvas=wl
                list1 = vol
                for i in range(9):
                    for j in range(9):
                        if(list1[i][j]!=0):
                            if(i==0):
                                if(j==0):
                                    self.entry_in_index01.insert(1.1, list1[i][j])
                                    self.entry_in_index01.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index01.place(x=82,y=82)

                                if(j==1):
                                    self.entry_in_index02.insert(1.1, list1[i][j])
                                    self.entry_in_index02.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index02.place(x=122,y=82)

                                if(j==2):
                                    self.entry_in_index03.insert(1.1, list1[i][j])
                                    self.entry_in_index03.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index03.place(x=162,y=82)

                                if(j==3):
                                    self.entry_in_index04.insert(1.1, list1[i][j])
                                    self.entry_in_index04.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index04.place(x=203,y=82)

                                if(j==4):
                                    self.entry_in_index05.insert(1.1, list1[i][j])
                                    self.entry_in_index05.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index05.place(x=242,y=82)

                                if(j==5):
                                    self.entry_in_index06.insert(1.1, list1[i][j])
                                    self.entry_in_index06.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index06.place(x=282,y=82)
                                
                                if(j==6):
                                    self.entry_in_index07.insert(1.1, list1[i][j])
                                    self.entry_in_index07.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index07.place(x=323,y=82)

                                if(j==7):
                                    self.entry_in_index08.insert(1.1, list1[i][j])
                                    self.entry_in_index08.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index08.place(x=362,y=82)

                                if(j==8):
                                    self.entry_in_index09.insert(1.1, list1[i][j])
                                    self.entry_in_index09.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index09.place(x=402,y=82)

                            if(i==1):

                                if(j==0):
                                    self.entry_in_index11.insert(1.1, list1[i][j])
                                    self.entry_in_index11.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index11.place(x=82,y=122)

                                if(j==1):
                                    self.entry_in_index12.insert(1.1, list1[i][j])
                                    self.entry_in_index12.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index12.place(x=122,y=122)

                                if(j==2):
                                    self.entry_in_index13.insert(1.1, list1[i][j])
                                    self.entry_in_index13.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index13.place(x=162,y=122)

                                if(j==3):
                                    self.entry_in_index14.insert(1.1, list1[i][j])
                                    self.entry_in_index14.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index14.place(x=203,y=122)

                                if(j==4):
                                    self.entry_in_index15.insert(1.1, list1[i][j])
                                    self.entry_in_index15.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index15.place(x=242,y=122)

                                if(j==5):
                                    self.entry_in_index16.insert(1.1, list1[i][j])
                                    self.entry_in_index16.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index16.place(x=282,y=122)
                                
                                if(j==6):
                                    self.entry_in_index17.insert(1.1, list1[i][j])
                                    self.entry_in_index17.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index17.place(x=323,y=122)

                                if(j==7):
                                    self.entry_in_index18.insert(1.1, list1[i][j])
                                    self.entry_in_index18.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index18.place(x=362,y=122)

                                if(j==8):
                                    self.entry_in_index19.insert(1.1, list1[i][j])
                                    self.entry_in_index19.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index19.place(x=402,y=122)

                            if(i==2):

                                if(j==0):
                                    self.entry_in_index21.insert(1.1, list1[i][j])
                                    self.entry_in_index21.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index21.place(x=82,y=162)

                                if(j==1):
                                    self.entry_in_index22.insert(1.1, list1[i][j])
                                    self.entry_in_index22.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index22.place(x=122,y=162)

                                if(j==2):
                                    self.entry_in_index23.insert(1.1, list1[i][j])
                                    self.entry_in_index23.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index23.place(x=162,y=162)

                                if(j==3):
                                    self.entry_in_index24.insert(1.1, list1[i][j])
                                    self.entry_in_index24.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index24.place(x=203,y=162)

                                if(j==4):
                                    self.entry_in_index25.insert(1.1, list1[i][j])
                                    self.entry_in_index25.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index25.place(x=242,y=162)

                                if(j==5):
                                    self.entry_in_index26.insert(1.1, list1[i][j])
                                    self.entry_in_index26.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index26.place(x=282,y=162)
            
                                if(j==6):
                                    self.entry_in_index27.insert(1.1, list1[i][j])
                                    self.entry_in_index27.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index27.place(x=323,y=162)

                                if(j==7):
                                    self.entry_in_index28.insert(1.1, list1[i][j])
                                    self.entry_in_index28.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index28.place(x=362,y=162)

                                if(j==8):
                                    self.entry_in_index29.insert(1.1, list1[i][j])
                                    self.entry_in_index29.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index29.place(x=402,y=162)


                            if(i==3):

                                if(j==0):
                                    self.entry_in_index31.insert(1.1, list1[i][j])
                                    self.entry_in_index31.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index31.place(x=82,y=203)

                                if(j==1):
                                    self.entry_in_index32.insert(1.1, list1[i][j])
                                    self.entry_in_index32.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index32.place(x=122,y=203)

                                if(j==2):
                                    self.entry_in_index33.insert(1.1, list1[i][j])
                                    self.entry_in_index33.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index33.place(x=162,y=203)

                                if(j==3):
                                    self.entry_in_index34.insert(1.1, list1[i][j])
                                    self.entry_in_index34.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index34.place(x=203,y=203)

                                if(j==4):
                                    self.entry_in_index35.insert(1.1, list1[i][j])
                                    self.entry_in_index35.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index35.place(x=242,y=203)

                                if(j==5):
                                    self.entry_in_index36.insert(1.1, list1[i][j])
                                    self.entry_in_index36.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index36.place(x=282,y=203)
            
                                if(j==6):
                                    self.entry_in_index37.insert(1.1, list1[i][j])
                                    self.entry_in_index37.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index37.place(x=323,y=203)

                                if(j==7):
                                    self.entry_in_index38.insert(1.1, list1[i][j])
                                    self.entry_in_index38.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index38.place(x=362,y=203)

                                if(j==8):
                                    self.entry_in_index39.insert(1.1, list1[i][j])
                                    self.entry_in_index39.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index39.place(x=402,y=203)

                            if(i==4):

                                if(j==0):
                                    self.entry_in_index41.insert(1.1, list1[i][j])
                                    self.entry_in_index41.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index41.place(x=82,y=242)

                                if(j==1):
                                    self.entry_in_index42.insert(1.1, list1[i][j])
                                    self.entry_in_index42.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index42.place(x=122,y=242)

                                if(j==2):
                                    self.entry_in_index43.insert(1.1, list1[i][j])
                                    self.entry_in_index43.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index43.place(x=162,y=242)

                                if(j==3):
                                    self.entry_in_index44.insert(1.1, list1[i][j])
                                    self.entry_in_index44.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index44.place(x=203,y=242)

                                if(j==4):
                                    self.entry_in_index45.insert(1.1, list1[i][j])
                                    self.entry_in_index45.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index45.place(x=242,y=242)

                                if(j==5):
                                    self.entry_in_index46.insert(1.1, list1[i][j])
                                    self.entry_in_index46.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index46.place(x=282,y=242)
                                
                                if(j==6):
                                    self.entry_in_index47.insert(1.1, list1[i][j])
                                    self.entry_in_index47.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index47.place(x=323,y=242)

                                if(j==7):
                                    self.entry_in_index48.insert(1.1, list1[i][j])
                                    self.entry_in_index48.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index48.place(x=362,y=242)

                                if(j==8):
                                    self.entry_in_index49.insert(1.1, list1[i][j])
                                    self.entry_in_index49.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index49.place(x=402,y=242)

                            if(i==5):

                                if(j==0):
                                    self.entry_in_index51.insert(1.1, list1[i][j])
                                    self.entry_in_index51.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index51.place(x=82,y=282)

                                if(j==1):
                                    self.entry_in_index52.insert(1.1, list1[i][j])
                                    self.entry_in_index52.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index52.place(x=122,y=282)

                                if(j==2):
                                    self.entry_in_index53.insert(1.1, list1[i][j])
                                    self.entry_in_index53.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index53.place(x=162,y=282)

                                if(j==3):
                                    self.entry_in_index54.insert(1.1, list1[i][j])
                                    self.entry_in_index54.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index54.place(x=203,y=282)

                                if(j==4):
                                    self.entry_in_index55.insert(1.1, list1[i][j])
                                    self.entry_in_index55.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index55.place(x=242,y=282)

                                if(j==5):
                                    self.entry_in_index56.insert(1.1, list1[i][j])
                                    self.entry_in_index56.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index56.place(x=282,y=282)
                                
                                if(j==6):
                                    self.entry_in_index57.insert(1.1, list1[i][j])
                                    self.entry_in_index57.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index57.place(x=323,y=282)

                                if(j==7):
                                    self.entry_in_index58.insert(1.1, list1[i][j])
                                    self.entry_in_index58.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index58.place(x=362,y=282)

                                if(j==8):
                                    self.entry_in_index59.insert(1.1, list1[i][j])
                                    self.entry_in_index59.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index59.place(x=402,y=282)

                            if(i==6):

                                if(j==0):
                                    self.entry_in_index61.insert(1.1, list1[i][j])
                                    self.entry_in_index61.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index61.place(x=82,y=323)

                                if(j==1):
                                    self.entry_in_index62.insert(1.1, list1[i][j])
                                    self.entry_in_index62.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index62.place(x=122,y=322)

                                if(j==2):
                                    self.entry_in_index63.insert(1.1, list1[i][j])
                                    self.entry_in_index63.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index63.place(x=162,y=323)

                                if(j==3):
                                    self.entry_in_index64.insert(1.1, list1[i][j])
                                    self.entry_in_index64.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index64.place(x=203,y=323)

                                if(j==4):
                                    self.entry_in_index65.insert(1.1, list1[i][j])
                                    self.entry_in_index65.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index65.place(x=242,y=323)

                                if(j==5):
                                    self.entry_in_index66.insert(1.1, list1[i][j])
                                    self.entry_in_index66.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index66.place(x=282,y=323)
                                
                                if(j==6):
                                    self.entry_in_index67.insert(1.1, list1[i][j])
                                    self.entry_in_index67.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index67.place(x=323,y=323)

                                if(j==7):
                                    self.entry_in_index68.insert(1.1, list1[i][j])
                                    self.entry_in_index68.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index68.place(x=362,y=323)

                                if(j==8):
                                    self.entry_in_index69.insert(1.1, list1[i][j])
                                    self.entry_in_index69.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index69.place(x=402,y=323)

                            if(i==7):

                                if(j==0):
                                    self.entry_in_index71.insert(1.1, list1[i][j])
                                    self.entry_in_index71.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index71.place(x=82,y=362)

                                if(j==1):
                                    self.entry_in_index72.insert(1.1, list1[i][j])
                                    self.entry_in_index72.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index72.place(x=122,y=362)

                                if(j==2):
                                    self.entry_in_index73.insert(1.1, list1[i][j])
                                    self.entry_in_index73.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index73.place(x=162,y=362)

                                if(j==3):
                                    self.entry_in_index74.insert(1.1, list1[i][j])
                                    self.entry_in_index74.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index74.place(x=203,y=362)

                                if(j==4):
                                    self.entry_in_index75.insert(1.1, list1[i][j])
                                    self.entry_in_index75.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index75.place(x=242,y=362)

                                if(j==5):
                                    self.entry_in_index76.insert(1.1, list1[i][j])
                                    self.entry_in_index76.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index76.place(x=282,y=362)
                            
                                if(j==6):
                                    self.entry_in_index77.insert(1.1, list1[i][j])
                                    self.entry_in_index77.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index77.place(x=323,y=362)

                                if(j==7):
                                    self.entry_in_index78.insert(1.1, list1[i][j])
                                    self.entry_in_index78.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index78.place(x=362,y=362)

                                if(j==8):
                                    self.entry_in_index79.insert(1.1, list1[i][j])
                                    self.entry_in_index79.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index79.place(x=402,y=362)

                            if(i==8):

                                if(j==0):
                                    self.entry_in_index81.insert(1.1, list1[i][j])
                                    self.entry_in_index81.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index81.place(x=82,y=402)

                                if(j==1):
                                    self.entry_in_index82.insert(1.1, list1[i][j])
                                    self.entry_in_index82.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index82.place(x=122,y=402)

                                if(j==2):
                                    self.entry_in_index83.insert(1.1, list1[i][j])
                                    self.entry_in_index83.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index83.place(x=162,y=402)

                                if(j==3):
                                    self.entry_in_index84.insert(1.1, list1[i][j])
                                    self.entry_in_index84.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index84.place(x=203,y=402)

                                if(j==4):
                                    self.entry_in_index85.insert(1.1, list1[i][j])
                                    self.entry_in_index85.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index85.place(x=242,y=402)

                                if(j==5):
                                    self.entry_in_index86.insert(1.1, list1[i][j])
                                    self.entry_in_index86.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index86.place(x=282,y=402)
                                
                                if(j==6):
                                    self.entry_in_index87.insert(1.1, list1[i][j])
                                    self.entry_in_index87.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index87.place(x=323,y=402)

                                if(j==7):
                                    self.entry_in_index88.insert(1.1, list1[i][j])
                                    self.entry_in_index88.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index88.place(x=362,y=402)

                                if(j==8):
                                    self.entry_in_index89.insert(1.1, list1[i][j])
                                    self.entry_in_index89.configure(state = 'disabled' , fg = 'black')
                                    self.entry_in_index89.place(x=402,y=402)
            com_random_values(canvas,list1)
                     
        canvas_width = 500
        canvas_height =500

        #Making Canvas for the pattern
        w = Canvas(root,width=canvas_width,height=canvas_height,highlightthickness=0)
        w.place(x=400,y=100)
        checkered(w,40)
 
        self.for_grid_frame.pack(after = self.gap,anchor = 'w',padx='300')
        
        self.gap = Frame(root,height=200)
        self.gap.pack()
    
    # string values in computer memory to calculate end result
    def checker (self):
        
        self.sudoku_values[0][0]= self.entry_in_index01.get("1.1",'end-1c')
        self.sudoku_values[0][1]= self.entry_in_index02.get("1.1",'end-1c')
        self.sudoku_values[0][2]= self.entry_in_index03.get("1.1",'end-1c')
        self.sudoku_values[0][3]= self.entry_in_index04.get("1.1",'end-1c')
        self.sudoku_values[0][4]= self.entry_in_index05.get("1.1",'end-1c')
        self.sudoku_values[0][5]= self.entry_in_index06.get("1.1",'end-1c')
        self.sudoku_values[0][6]= self.entry_in_index07.get("1.1",'end-1c')
        self.sudoku_values[0][7]= self.entry_in_index08.get("1.1",'end-1c')
        self.sudoku_values[0][8]= self.entry_in_index09.get("1.1",'end-1c')
        
        self.sudoku_values[1][0]= self.entry_in_index11.get("1.1",'end-1c')
        self.sudoku_values[1][1]= self.entry_in_index12.get("1.1",'end-1c')
        self.sudoku_values[1][2]= self.entry_in_index13.get("1.1",'end-1c')
        self.sudoku_values[1][3]= self.entry_in_index14.get("1.1",'end-1c')
        self.sudoku_values[1][4]= self.entry_in_index15.get("1.1",'end-1c')
        self.sudoku_values[1][5]= self.entry_in_index16.get("1.1",'end-1c')
        self.sudoku_values[1][6]= self.entry_in_index17.get("1.1",'end-1c')
        self.sudoku_values[1][7]= self.entry_in_index18.get("1.1",'end-1c')
        self.sudoku_values[1][8]= self.entry_in_index19.get("1.1",'end-1c')
        
        self.sudoku_values[2][0]= self.entry_in_index21.get("1.1",'end-1c')
        self.sudoku_values[2][1]= self.entry_in_index22.get("1.1",'end-1c')
        self.sudoku_values[2][2]= self.entry_in_index23.get("1.1",'end-1c')
        self.sudoku_values[2][3]= self.entry_in_index24.get("1.1",'end-1c')
        self.sudoku_values[2][4]= self.entry_in_index25.get("1.1",'end-1c')
        self.sudoku_values[2][5]= self.entry_in_index26.get("1.1",'end-1c')
        self.sudoku_values[2][6]= self.entry_in_index27.get("1.1",'end-1c')
        self.sudoku_values[2][7]= self.entry_in_index28.get("1.1",'end-1c')
        self.sudoku_values[2][8]= self.entry_in_index29.get("1.1",'end-1c')
        
        self.sudoku_values[3][0]= self.entry_in_index31.get("1.1",'end-1c')
        self.sudoku_values[3][1]= self.entry_in_index32.get("1.1",'end-1c')
        self.sudoku_values[3][2]= self.entry_in_index33.get("1.1",'end-1c')
        self.sudoku_values[3][3]= self.entry_in_index34.get("1.1",'end-1c')
        self.sudoku_values[3][4]= self.entry_in_index35.get("1.1",'end-1c')
        self.sudoku_values[3][5]= self.entry_in_index36.get("1.1",'end-1c')
        self.sudoku_values[3][6]= self.entry_in_index37.get("1.1",'end-1c')
        self.sudoku_values[3][7]= self.entry_in_index38.get("1.1",'end-1c')
        self.sudoku_values[3][8]= self.entry_in_index39.get("1.1",'end-1c')
        
        self.sudoku_values[4][0]= self.entry_in_index41.get("1.1",'end-1c')
        self.sudoku_values[4][1]= self.entry_in_index42.get("1.1",'end-1c')
        self.sudoku_values[4][2]= self.entry_in_index43.get("1.1",'end-1c')
        self.sudoku_values[4][3]= self.entry_in_index44.get("1.1",'end-1c')
        self.sudoku_values[4][4]= self.entry_in_index45.get("1.1",'end-1c')
        self.sudoku_values[4][5]= self.entry_in_index46.get("1.1",'end-1c')
        self.sudoku_values[4][6]= self.entry_in_index47.get("1.1",'end-1c')
        self.sudoku_values[4][7]= self.entry_in_index48.get("1.1",'end-1c')
        self.sudoku_values[4][8]= self.entry_in_index49.get("1.1",'end-1c')
        
        self.sudoku_values[5][0]= self.entry_in_index51.get("1.1",'end-1c')
        self.sudoku_values[5][1]= self.entry_in_index52.get("1.1",'end-1c')
        self.sudoku_values[5][2]= self.entry_in_index53.get("1.1",'end-1c')
        self.sudoku_values[5][3]= self.entry_in_index54.get("1.1",'end-1c')
        self.sudoku_values[5][4]= self.entry_in_index55.get("1.1",'end-1c')
        self.sudoku_values[5][5]= self.entry_in_index56.get("1.1",'end-1c')
        self.sudoku_values[5][6]= self.entry_in_index57.get("1.1",'end-1c')
        self.sudoku_values[5][7]= self.entry_in_index58.get("1.1",'end-1c')
        self.sudoku_values[5][8]= self.entry_in_index59.get("1.1",'end-1c')
        
        self.sudoku_values[6][0]= self.entry_in_index61.get("1.1",'end-1c')
        self.sudoku_values[6][1]= self.entry_in_index62.get("1.1",'end-1c')
        self.sudoku_values[6][2]= self.entry_in_index63.get("1.1",'end-1c')
        self.sudoku_values[6][3]= self.entry_in_index64.get("1.1",'end-1c')
        self.sudoku_values[6][4]= self.entry_in_index65.get("1.1",'end-1c')
        self.sudoku_values[6][5]= self.entry_in_index66.get("1.1",'end-1c')
        self.sudoku_values[6][6]= self.entry_in_index67.get("1.1",'end-1c')
        self.sudoku_values[6][7]= self.entry_in_index68.get("1.1",'end-1c')
        self.sudoku_values[6][8]= self.entry_in_index69.get("1.1",'end-1c')
        
        self.sudoku_values[7][0]= self.entry_in_index71.get("1.1",'end-1c')
        self.sudoku_values[7][1]= self.entry_in_index72.get("1.1",'end-1c')
        self.sudoku_values[7][2]= self.entry_in_index73.get("1.1",'end-1c')
        self.sudoku_values[7][3]= self.entry_in_index74.get("1.1",'end-1c')
        self.sudoku_values[7][4]= self.entry_in_index75.get("1.1",'end-1c')
        self.sudoku_values[7][5]= self.entry_in_index76.get("1.1",'end-1c')
        self.sudoku_values[7][6]= self.entry_in_index77.get("1.1",'end-1c')
        self.sudoku_values[7][7]= self.entry_in_index78.get("1.1",'end-1c')
        self.sudoku_values[7][8]= self.entry_in_index79.get("1.1",'end-1c')
        
        self.sudoku_values[8][0]= self.entry_in_index81.get("1.1",'end-1c')
        self.sudoku_values[8][1]= self.entry_in_index82.get("1.1",'end-1c')
        self.sudoku_values[8][2]= self.entry_in_index83.get("1.1",'end-1c')
        self.sudoku_values[8][3]= self.entry_in_index84.get("1.1",'end-1c')
        self.sudoku_values[8][4]= self.entry_in_index85.get("1.1",'end-1c')
        self.sudoku_values[8][5]= self.entry_in_index86.get("1.1",'end-1c')
        self.sudoku_values[8][6]= self.entry_in_index87.get("1.1",'end-1c')
        self.sudoku_values[8][7]= self.entry_in_index88.get("1.1",'end-1c')
        self.sudoku_values[8][8]= self.entry_in_index89.get("1.1",'end-1c')
        
        # msg buttons
        def error():
            msg.showinfo("Result","That doesn't look right! 🤔")
        def right():
            msg.showinfo("Result","That's looking Good! 😀👍")    

        # check that all User input are correct 
        def last_answer(vol):
            key=0
            list1 = vol
            for i in range(9):
                for j in range(9):
                    if(list1[i][j]==0):
                        error()
                        return 1 
                    
                    else:
                        passer=0 
                        temp= list1[i][j] 
                        for k in range(9):
                        
                            if(temp==list1[i][k] and k!=j):
                                error()
                                passer=1 
                                return 1 
                            
                            if(temp == list1[k][j] and k!=i):
                                error()
                                passer=1 
                                return 1 
                        
                        if(passer==0):
                            if(i<3 and j<3):
                                for k in range(3):
                                    for l in range(3):
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                            
                            elif(i<3 and j<6):
                                for k in range(3):
                                    for l in range(3,6):
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                            
                            elif (i<3 and j<9):
                                for k in range(3):
                                    for l in range(6,9):
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 

                            elif (i<6 and j<3):
                                for k in range(3,6):
                                    for l in range(3):
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                            
                            elif (i<6 and j<6):
                                for k in range(3,6):
                                    for l in range(3,6):    
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                           
                            elif (i<6 and j<9):
                                for k in range(3,6):
                                    for l in range(6,9):
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                                                                       
                            elif (i<9 and j<3):
                                for k in range(6,9):
                                    for l in range(3):
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                            
                            elif (i<9 and j<6):
                                for k in range(6,9):
                                    for l in range(3,6):    
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                            
                            elif (i<9 and j<9):
                                for k in range(6,9):
                                    for l in range(6,9):        
                                        if(temp==list1[k][l] and k!=i and k!=j):
                                            error()
                                            return 1 
                            
                            if (i == 8 and j==8):
                                key =1 
                            
                        else:
                            error()
                            return 1 
                
            if(key==1):
                right()
            return 0 
        
        last_answer(self.sudoku_values)

#starting of tkinter
root = Tk()
obj = game(root)
root.title("Sudoku! Lets Play ")
root.mainloop()
