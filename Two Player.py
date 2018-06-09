# include Information
print("="*80)
print("| My Name       : Ehab Fawzy Ibrahim ")
print("| My ID         : 20170072           ")
print("| Academic Year : Level 1            ")
print("| My Group      : G3                 ")
print("| My Faculty    : FCI                ")
print("="*80)


while ( True ):

    # Welcame Message

    print( " "*28 ,"Welcome To Tic Tac Toe Game" )
    print(" ")

    # Show Position With Start

    print("This Is Position Of Game Board")
    print(" ")

    print("|----|----|----|")
    print("|" , 1 , " |" , 2 , " |" , 3 , " |" )
    print("|----+----+----|")
    print("|" , 4 , " |" , 5 , " |" , 6 , " |" )
    print("|----+----+----|")
    print("|" , 7 , " |" , 8 , " |" , 9 , " |" )
    print("|----|----|----|")
    print(" ")

    while( True ):
        x = str( input('To Start Game Press (Y) Button : ') )
        if ( x == "y" or x == "Y" ):
            break

    # Algorithm

    GameData = [ -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 ]
    GamePosition = [ "X" , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]

    k = 1
    Player_Number = [0,1,2]
    while ( True ):
        print(" ")
        str_index = str( input('Who Will Start ?  Player 1 or player 2 (Enter Number of Player) : ') )
        if ( str_index == "1" or str_index == "2" ):
            index = int(str_index)
            if ( index == 1 or index == 2 ):
                break
        else:
            print( "Oops! You Should Choose 1 OR 2 Only" )
            print(" ")

    if ( index != Player_Number[1] ):
        k = 2


    # Design Board

    print(" ")
    print("|----|----|----|",                                  " "*40 ,                                               "|----|----|----|"                    )
    print("|" , " " , " |" , " " , " |" , " " , " |" ,         " "*40 ,                                               "|" , 1 , " |" , 2 , " |" , 3 , " |"  )
    print("|----+----+----|",                                  " "*2  ,  " >>>> " , " "*30                 ,          "|----+----+----|" )
    print("|" , " " , " |" , " " , " |" , " " , " |" ,         " "*2  , " > "  , "Postion Of Board available", " "*6 ,"|" , 4 , " |" , 5 , " |" , 6 , " |"  )
    print("|----+----+----|",                                  " "*2  , " >>>> " ,                            " "*30 ,"|----+----+----|" )
    print("|" , " " , " |" , " " , " |" , " " , " |" ,         " "*40 ,                                               "|" , 7 , " |" , 8 , " |" , 9 , " |"  )
    print("|----|----|----|",                                  " "*40 ,                                               "|----|----|----|" )
    print(" ")


    while(True):
        print(" ")
        print("Player", Player_Number[k] , "Turn..")

        #print(" ")
        pos = int( input('Choose Position : ') )

        while( True ):
            if ( pos > 9 or pos < 1 ):
                print( "Oops! - Sorry Poistion Should Be In Range 1 TO 9 " )
                print(" ")
                pos = int( input('Choose Position : ') )
            else:
                break

        while( True ):
            if ( GameData[pos] != -100 ):
                print("Sorry This Position Is Not Aavailable ")
                print(" ")
                pos = int( input('Choose Another Position : ') )
            else:
                break

        val = int( input('Choose Value    : ') )

        while( True ):
            if ( val > 9 or val < 0 ):
                print( "Oops! - Sorry Value Should Be In Range 1 TO 9 " )
                print(" ")
                val = int( input('Choose Value    : ') )
            elif ( k == 1 and val % 2 == 0 ):
                print( "Oops! - Sorry You Should Choose Odd Numbers " )
                print(" ")
                val = int( input('Choose Another Value    : ') )
            elif ( k == 2 and val % 2 != 0 ):
                print( "Oops! - Sorry You Should Choose Even Numbers " )
                print(" ")
                val = int( input('Choose Another Value    : ') )
            elif ( val in GameData ):
                print( "Oops! - Sorry You Are Use This Value Before " )
                print(" ")
                val = int( input('Choose Another Value    : ') )
            else:
                break
        
        
        GameData[pos]     = val
        GamePosition[pos] = "X"


        for i in range ( 1 , 10 , 1 ):
            if ( GameData[i] == -100 ):
                GameData[i] = " "

        print(" ")
        print("|----|----|----|"   ,     " "*40    , "|----|----|----|" )
        print("|" , GameData[1] , " |" , GameData[2] , " |" , GameData[3] , " |" , " "*40 , "|" , GamePosition[1] , " |" , GamePosition[2] , " |" , GamePosition[3] , " |")
        print("|----+----+----|"   , " "*2 , " >>>> " , " "*30 , "|----+----+----|" )
        print("|" , GameData[4] , " |" , GameData[5] , " |" , GameData[6] , " |" , " "*2  , " > "  , "Postion Of Board available", " "*6 ,"|" , GamePosition[4] , " |" , GamePosition[5] , " |" , GamePosition[6] , " |"  )
        print("|----+----+----|"   , " "*2 , " >>>> " , " "*30 , "|----+----+----|" )
        print("|" , GameData[7] , " |" , GameData[8] , " |" , GameData[9] , " |" ,   " "*40 , "|" , GamePosition[7] , " |" , GamePosition[8] , " |" , GamePosition[9] , " |" )
        print("|----|----|----|"   ,     " "*40    , "|----|----|----|" )
        print(" ")

        for i in range ( 1 , 10 , 1 ):
            if ( GameData[i] == " " ):
                GameData[i] = -100

        counter = 0
        if   ( GameData[1] + GameData[4] + GameData[7] == 15 ):
            counter = 1
        elif ( GameData[2] + GameData[5] + GameData[8] == 15 ):
            counter = 1
        elif ( GameData[3] + GameData[6] + GameData[9] == 15 ):
            counter = 1
        elif ( GameData[1] + GameData[2] + GameData[3] == 15 ):
            counter = 1
        elif ( GameData[4] + GameData[5] + GameData[6] == 15 ):
            counter = 1
        elif ( GameData[7] + GameData[8] + GameData[9] == 15 ):
            counter = 1
        elif ( GameData[1] + GameData[5] + GameData[9] == 15 ):
            counter = 1
        elif ( GameData[3] + GameData[5] + GameData[7] == 15 ):
            counter = 1

        if ( counter == 1 ):
            print(" "*16  ,"=========================================")
            print(" "*16 , "|   Player ",Player_Number[k], " Win"," - Congratulations   |")
            print(" "*16 , "=========================================")
            break
        counter = 0
        for i in range(10):
            if ( GamePosition[i] != "X" ):
                counter = 1
        if ( counter == 0 ):
            print(" "*16  ,"=========================================")
            print(" "*16 , "|               NO Winner               |")
            print(" "*16 , "=========================================")
            break

        if ( k == 1 ):
            k = 2
        else:
            k = 1
    
    print( "If You Want To Play Another Game Press (Y) key , If You Want To Exit Press Any Key" )
    ask = str( input( "Do You Want To Play Another Game ? : " ) )
    print(" ")
    if ( ask != "Y" and ask != "y" ):
        break
