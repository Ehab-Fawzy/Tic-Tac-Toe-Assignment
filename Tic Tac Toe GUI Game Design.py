import time
from tkinter import*

while ( True ):

    Quit_Array = [0]
    
    game = Tk()
    game.title('Tic Tac Toe')
    
    # >> Layout
    topFrame = Frame(game)
    topFrame.pack()

    # >> Layout Desing
    background = PhotoImage( file = "Layout-4.png" )
    lab        = Label( game , image = background )
    lab.pack()

    # >> DataBase Area

    GameData = [ -101 , -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 ]
    GamePlay = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]

    even_val = "02468"
    odd_val  = "13579"

    # >> function Area
    
    def Quit():
        Quit_Array[0] = 1
        game.destroy()

    def restart():
        game.destroy()

    def player_one():
        odd_button.config( state = "disable" )
        even_button.config( state = "normal" )
    def player_two():
        odd_button.config( state = "normal" )
        even_button.config( state = "disable" )
    
    def box1_even():
        check = False
        box1 = input_box1.get()
        if box1 in even_val:
            box1 = int( box1 )
            if box1 not in GameData:
                GameData[1] = int( box1 )
                input_box1.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box1_odd():
        check = False
        box1 = input_box1.get()
        if box1 in odd_val:
            box1 = int( box1 )
            if box1 not in GameData:
                GameData[1] = int( box1 )
                input_box1.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check

    def box2_even():
        check = False
        box2 = input_box2.get()
        if box2 in even_val:
            box2 = int( box2 )
            if box2 not in GameData:
                GameData[2] = int( box2 )
                input_box2.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box2_odd():
        check = False
        box2 = input_box2.get()
        if box2 in odd_val:
            box2 = int( box2 )
            if box2 not in GameData:
                GameData[2] = int( box2 )
                input_box2.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check
        
    def box3_even():
        check = False
        box3 = input_box3.get()
        if box3 in even_val:
            box3 = int( box3 )
            if box3 not in GameData:
                GameData[3] = int( box3 )
                input_box3.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box3_odd():
        check = False
        box3 = input_box3.get()
        if box3 in odd_val:
            box3 = int( box3 )
            if box3 not in GameData:
                GameData[3] = int( box3 )
                input_box3.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check
        
    def box4_even():
        check = False
        box4 = input_box4.get()
        if box4 in even_val:
            box4 = int( box4 )
            if box4 not in GameData:
                GameData[4] = int( box4 )
                input_box4.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box4_odd():
        check = False
        box4 = input_box4.get()
        if box4 in odd_val:
            box4 = int( box4 )
            if box4 not in GameData:
                GameData[4] = int( box4 )
                input_box4.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check

    def box5_even():
        check = False
        box5 = input_box5.get()
        if box5 in even_val:
            box5 = int( box5 )
            if box5 not in GameData:
                GameData[5] = int( box5 )
                input_box5.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box5_odd():
        check = False
        box5 = input_box5.get()
        if box5 in odd_val:
            box5 = int( box5 )
            if box5 not in GameData:
                GameData[5] = int( box5 )
                input_box5.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check

    def box6_even():
        check = False
        box6 = input_box6.get()
        if box6 in even_val:
            box6 = int( box6 )
            if box6 not in GameData:
                GameData[6] = int( box6 )
                input_box6.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box6_odd():
        check = False
        box6 = input_box6.get()
        if box6 in odd_val:
            box6 = int( box6 )
            if box6 not in GameData:
                GameData[6] = int( box6 )
                input_box6.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check

    def box7_even():
        check = False
        box7 = input_box7.get()
        if box7 in even_val:
            box7 = int( box7 )
            if box7 not in GameData:
                GameData[7] = int( box7 )
                input_box7.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box7_odd():
        check = False
        box7 = input_box7.get()
        if box7 in odd_val:
            box7 = int( box7 )
            if box7 not in GameData:
                GameData[7] = int( box7 )
                input_box7.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check

    def box8_even():
        check = False
        box8 = input_box8.get()
        if box8 in even_val:
            box8 = int( box8 )
            if box8 not in GameData:
                GameData[8] = int( box8 )
                input_box8.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box8_odd():
        check = False
        box8 = input_box8.get()
        if box8 in odd_val:
            box8 = int( box8 )
            if box8 not in GameData:
                GameData[8] = int( box8 )
                input_box8.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check

    def box9_even():
        check = False
        box9 = input_box9.get()
        if box9 in even_val:
            box9 = int( box9 )
            if box9 not in GameData:
                GameData[9] = int( box9 )
                input_box9.config( state = 'disable' )
                note.config( text = "Note : Player One Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Even" )

        return check
        
    def box9_odd():
        check = False
        box9 = input_box9.get()
        if box9 in odd_val:
            box9 = int( box9 )
            if box9 not in GameData:
                GameData[9] = int( box9 )
                input_box9.config( state = 'disable' )
                note.config( text = "Note : Player Two Turn" )
                check = True
            else:
                note.config( text = "Note : This Value Is Already Taken" )
        else:
            note.config( text = "Note : This Number Is Not Odd" )

        return check

    def even_check( x ):
        even_val = "02468"
        check = False
        for i in range ( len( even_val ) ):
            if ( x == even_val[i] ):
                check = True
        if ( check == False ):
            note.config( text = "Note : This Number Is Not Even" )
        return check

    def odd_check( x ):
        odd_val  = "13579"
        check = False
        for i in range ( len( odd_val ) ):
            if ( x == odd_val[i] ):
                check = True
        if ( check == False ):
            note.config( text = "Note : This Number Is Not Odd" )
        return check 

    def even_action():

        if   ( even_check( input_box1.get() ) == True and GamePlay[1] == 0 ):

            even_value_check = int ( input_box1.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box1_even()
                GamePlay[1] = 1
                player_two()
                
        elif ( even_check( input_box2.get() ) == True and GamePlay[2] == 0 ):

            even_value_check = int ( input_box2.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box2_even()
                GamePlay[2] = 1
                player_two()
                
        elif ( even_check( input_box3.get() ) == True and GamePlay[3] == 0 ):
            
            even_value_check = int ( input_box3.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box3_even()
                GamePlay[3] = 1
                player_two()
                
        elif ( even_check( input_box4.get() ) == True and GamePlay[4] == 0 ):
            
            even_value_check = int ( input_box4.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box4_even()
                GamePlay[4] = 1
                player_two()
                
        elif ( even_check( input_box5.get() ) == True and GamePlay[5] == 0 ):

            even_value_check = int ( input_box5.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1
                
            if ( counter == 0 ):
                box5_even()
                GamePlay[5] = 1
                player_two()
            
        elif ( even_check( input_box6.get() ) == True and GamePlay[6] == 0 ):

            even_value_check = int ( input_box6.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box6_even()
                GamePlay[6] = 1
                player_two()
                
        elif ( even_check( input_box7.get() ) == True and GamePlay[7] == 0 ):

            even_value_check = int ( input_box7.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box7_even()
                GamePlay[7] = 1
                player_two()
                
        elif ( even_check( input_box8.get() ) == True and GamePlay[8] == 0 ):

            even_value_check = int ( input_box8.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box8_even()
                GamePlay[8] = 1
                player_two()
                
        elif ( even_check( input_box9.get() ) == True and GamePlay[9] == 0 ):

            even_value_check = int ( input_box9.get() )
            counter = 0
            
            if even_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box9_even()
                GamePlay[9] = 1
                player_two()

        winner = 0
        if   ( GameData[1] + GameData[4] + GameData[7] == 15 ):
            winner = 1
        elif ( GameData[2] + GameData[5] + GameData[8] == 15 ):
            winner = 1
        elif ( GameData[3] + GameData[6] + GameData[9] == 15 ):
            winner = 1
        elif ( GameData[1] + GameData[2] + GameData[3] == 15 ):
            winner = 1
        elif ( GameData[4] + GameData[5] + GameData[6] == 15 ):
            winner = 1
        elif ( GameData[7] + GameData[8] + GameData[9] == 15 ):
            winner = 1
        elif ( GameData[1] + GameData[5] + GameData[9] == 15 ):
            winner = 1
        elif ( GameData[3] + GameData[5] + GameData[7] == 15 ):
            winner = 1

        if ( winner == 1 ):
            note.config( text = ">>>>    Player Two Won   <<<<" , font=('Agency FB',35) , fg = "white")
            input_box1.config(state='disable')
            input_box2.config(state='disable')
            input_box3.config(state='disable')
            input_box4.config(state='disable')
            input_box5.config(state='disable')
            input_box6.config(state='disable')
            input_box7.config(state='disable')
            input_box8.config(state='disable')
            input_box9.config(state='disable')
            even_button.config( state = "disable" )
            odd_button.config( state = "disable" )

        if -100 not in GameData:
            note.config( text = ">>>>    NO WINNER   <<<<" , font=('Agency FB',35) , fg = "white")
            even_button.config( state = "disable" )
            odd_button.config( state = "disable" )

    def odd_action():

        if   ( odd_check( input_box1.get() ) == True and GamePlay[1] == 0 ):
            
            odd_value_check = int ( input_box1.get() )
            counter = 0
            
            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1
                
            if ( counter == 0 ):
                box1_odd()
                GamePlay[1] = 1
                player_one()
                
        elif ( odd_check( input_box2.get() ) == True and GamePlay[2] == 0 ):
            
            odd_value_check = int ( input_box2.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1
                
            if ( counter == 0 ):
                box2_odd()
                GamePlay[2] = 1
                player_one()
                
        elif ( odd_check( input_box3.get() ) == True and GamePlay[3] == 0 ):

            odd_value_check = int ( input_box3.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1
                
            if ( counter == 0 ):
                box3_odd()
                GamePlay[3] = 1
                player_one()
                
        elif ( odd_check( input_box4.get() ) == True and GamePlay[4] == 0 ):

            odd_value_check = int ( input_box4.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box4_odd()
                GamePlay[4] = 1
                player_one()
                
        elif ( odd_check( input_box5.get() ) == True and GamePlay[5] == 0 ):

            odd_value_check = int ( input_box5.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box5_odd()
                GamePlay[5] = 1
                player_one()
                
        elif ( odd_check( input_box6.get() ) == True and GamePlay[6] == 0 ):

            odd_value_check = int ( input_box6.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box6_odd()
                GamePlay[6] = 1
                player_one()
                
        elif ( odd_check( input_box7.get() ) == True and GamePlay[7] == 0 ):

            odd_value_check = int ( input_box7.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box7_odd()
                GamePlay[7] = 1
                player_one()
                
        elif ( odd_check( input_box8.get() ) == True and GamePlay[8] == 0 ):

            odd_value_check = int ( input_box8.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box8_odd()
                GamePlay[8] = 1
                player_one()
                
        elif ( odd_check( input_box9.get() ) == True and GamePlay[9] == 0 ):

            odd_value_check = int ( input_box9.get() )
            counter = 0

            if odd_value_check in GameData:
                note.config( text = "Note : This Value Is Already Taken" )
                counter += 1

            if ( counter == 0 ):
                box9_odd()
                GamePlay[9] = 1
                player_one()

        winner = 0
        if   ( GameData[1] + GameData[4] + GameData[7] == 15 ):
            winner = 1
        elif ( GameData[2] + GameData[5] + GameData[8] == 15 ):
            winner = 1
        elif ( GameData[3] + GameData[6] + GameData[9] == 15 ):
            winner = 1
        elif ( GameData[1] + GameData[2] + GameData[3] == 15 ):
            winner = 1
        elif ( GameData[4] + GameData[5] + GameData[6] == 15 ):
            winner = 1
        elif ( GameData[7] + GameData[8] + GameData[9] == 15 ):
            winner = 1
        elif ( GameData[1] + GameData[5] + GameData[9] == 15 ):
            winner = 1
        elif ( GameData[3] + GameData[5] + GameData[7] == 15 ):
            winner = 1

        if ( winner == 1 ):
            note.config( text = ">>>>    Player One Won   <<<<" , font=('Agency FB',35) , fg = "white")
            input_box1.config(state='disable')
            input_box2.config(state='disable')
            input_box3.config(state='disable')
            input_box4.config(state='disable')
            input_box5.config(state='disable')
            input_box6.config(state='disable')
            input_box7.config(state='disable')
            input_box8.config(state='disable')
            input_box9.config(state='disable')
            even_button.config( state = "disable" )
            odd_button.config( state = "disable" )

        if -100 not in GameData:
            note.config( text = ">>>>    NO WINNER   <<<<" , font=('Agency FB',35) , fg = "white")
            even_button.config( state = "disable" )
            odd_button.config( state = "disable" )

    # >> Game Design

    input_box1 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box1.pack()
    input_box1.place( x = 115 , y = 274 , width = 80 , height = 80 )

    input_box2 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box2.pack()
    input_box2.place( x = 228 , y = 274 , width = 80 , height = 80 )

    input_box3 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box3.pack()
    input_box3.place( x = 341 , y = 274 , width = 80 , height = 80 )

    input_box4 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box4.pack()
    input_box4.place( x = 115 , y = 387 , width = 80 , height = 80 )

    input_box5 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box5.pack()
    input_box5.place( x = 228 , y = 387 , width = 80 , height = 80 )

    input_box6 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box6.pack()
    input_box6.place( x = 341 , y = 387 , width = 80 , height = 80 )

    input_box7 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box7.pack()
    input_box7.place( x = 115 , y = 500 , width = 80 , height = 80 )

    input_box8 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box8.pack()
    input_box8.place( x = 228 , y = 500 , width = 80 , height = 80 )

    input_box9 = Entry( game , font=('Arial Rounded MT Bold',30), justify = CENTER , fg = "Blue" )
    input_box9.pack()
    input_box9.place( x = 341 , y = 500 , width = 80 , height = 80 )

    note = Message( game , text = "Note : Player One Turn" , font=('Agency FB',25) , bg="#7DDBD3" , fg = "#1B1464", padx = 0 , pady = 80 )
    note.pack()
    note.place( x = 470 , y = 325 )

    odd_button = Button( game , justify = CENTER , bd = 0 , bg="#7DDBD3" , activebackground = "#7DDBD3" , command = odd_action )
    odd_button.pack()
    odd_button.place( x = 478 , y = 273 , width = 433 , height = 64 )

    odd_button_style = PhotoImage(file="oddbutton.png")
    odd_button.config( image = odd_button_style , width = 433 , height = 64 )

    even_button = Button( game , justify = CENTER , bd = 0 , bg="#7DDBD3" , activebackground = "#7DDBD3" , command = even_action )
    even_button.pack()
    even_button.place( x = 478 , y = 502 , width = 433 , height = 64 )

    even_button_style = PhotoImage(file="evedbutton1.png")
    even_button.config( image = even_button_style , width = 433 , height = 64 , state = "disable")

    Quit_button = Button( game , justify = CENTER , bd = 0 , bg="#7DDBD3" , activebackground = "#7DDBD3" , command = Quit )
    Quit_button.pack()
    Quit_button.place( x = 907 , y = 26 , width = 60 , height = 60 )

    Quit_button_style = PhotoImage( file="quit-button.png")
    Quit_button.config( image = Quit_button_style , width = 433 , height = 64 )

    ReStart_button = Button( game , justify = CENTER , bd = 0 , bg="#7DDBD3" , activebackground = "#7DDBD3" , command = restart )
    ReStart_button.pack()
    ReStart_button.place( x = 907 , y = 115 , width = 60 , height = 60 )

    ReStart_button_style = PhotoImage( file="restart-button.png")
    ReStart_button.config( image = ReStart_button_style , width = 433 , height = 64 )

    game.mainloop()

    
    if ( Quit_Array[0] == 1 ):
        break
