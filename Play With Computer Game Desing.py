import random
import time

while ( True ):

    # include Information
    print("="*80)
    print("| My Name       : Ehab Fawzy Ibrahim ")
    print("| My ID         : 20170072           ")
    print("| Academic Year : Level 1            ")
    print("| My Group      : G3                 ")
    print("| My Faculty    : FCI                ")
    print("="*80)

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

    GameData      = [ -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 , -100 ]
    GamePosition  = [ "X" , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
    playerArray   = []
    computerArray = []

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
            print( "Oops! Tou Should Choose 1 OR 2 Only" )
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

    # Main Loop

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
        playerArray.append(val)          


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
            print(" "*16  ,"=========================================")
            print(" "*16 , "|           YOU ARE THE WINNER          |")
            print(" "*16 , "=========================================")
            break

        counter = 0
        for i in range ( 1 , 10 ):
            if ( GamePosition[i] != "X" ):
                counter += 1
        if ( counter == 0 ):
            print(" "*16  ,"=========================================")
            print(" "*16 , "|               NO WINNER               |")
            print(" "*16 , "=========================================")
            break

        

        # Computer Turn
        
        if ( k == 1 ):

            # Even Section
            print(" ")
            print("Computer Turn..")

            Play_Number = 0        
            # Check For Computer Winner
            # 1-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 1 , 4 , 1 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[1] + GameData[2] + GameData[3] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 1 , 4 , 1 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1
            # 2-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 4 , 7 , 1 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[4] + GameData[5] + GameData[6] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 4 , 7 , 1 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1


            # 3-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 7 , 10 , 1 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[7] + GameData[8] + GameData[9] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 7 , 10 , 1 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 4-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 1 , 8 , 3 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[1] + GameData[4] + GameData[7] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 1 , 8 , 3 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 5-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 2 , 9 , 3 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[2] + GameData[5] + GameData[8] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 2 , 9 , 3 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1



            # 6-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 3 , 10 , 3 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[3] + GameData[6] + GameData[9] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 3 , 10 , 3 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 7-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 1 , 10 , 4 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[1] + GameData[5] + GameData[9] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 1 , 10 , 4 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 8-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 3 , 10 , 2 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[3] + GameData[5] + GameData[7] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 == 0 ):
                            if sumation not in computerArray:
                                for i in range ( 3 , 10 , 2 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1


            # Computer Turn
            if ( Play_Number == 0 ):
                # Check For Player Win
                defence  = 0
                start    = 1
                end      = 4
                loop_end = 0
                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( start , end , 1 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( start , end , 1 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        start += 3
                        end   += 3
                        if ( end > 10 ):
                            break

                start    = 1
                end      = 8
                
                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( start , end , 3 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( start , end , 3 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        start += 1
                        end   += 1
                        if ( end > 10 ):
                            break
                
                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( 1 , 10 , 4 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( 1 , 10 , 4 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        else:
                            break

                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( 3 , 10 , 2 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( 3 , 10 , 2 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        else:
                            break
                        
                if ( defence == 0 ):
                    while ( True ):
                        Random_Pos = random.randint(1,9)
                        if ( GameData[ Random_Pos ] == -100 ):
                            break
                    
                while ( True ):
                    Random_Val = random.randint(0,9)
                    if ( Random_Val % 2 == 0 ):
                        if Random_Val not in computerArray:
                            break
                GameData[ Random_Pos ] = Random_Val
                GamePosition[ Random_Pos ] = "X"
                computerArray.append( Random_Val )
            

        else:
            # Odd Section
            print(" ")
            print("Computer Turn..")

            Play_Number = 0        
            # Check For Computer Winner
            # 1-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 1 , 4 , 1 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[1] + GameData[2] + GameData[3] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 1 , 4 , 1 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1
            # 2-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 4 , 7 , 1 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[4] + GameData[5] + GameData[6] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 4 , 7 , 1 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1


            # 3-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 7 , 10 , 1 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[7] + GameData[8] + GameData[9] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 7 , 10 , 1 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 4-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 1 , 8 , 3 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[1] + GameData[4] + GameData[7] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 1 , 8 , 3 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 5-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 2 , 9 , 3 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[2] + GameData[5] + GameData[8] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 2 , 9 , 3 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1



            # 6-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 3 , 10 , 3 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[3] + GameData[6] + GameData[9] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 3 , 10 , 3 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 7-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 1 , 10 , 4 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[1] + GameData[5] + GameData[9] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 1 , 10 , 4 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1

            # 8-th loop ::
            if ( Play_Number == 0 ):
                counter  = 0
                sumation = 0
                for i in range ( 3 , 9 , 2 ):
                    if ( GameData[i] == -100 ):
                        counter += 1
                if ( counter == 1 ):
                    sumation = 15 - ( GameData[3] + GameData[5] + GameData[7] + 100 )
                    if ( sumation >= 0 and sumation < 10 ):
                        if ( sumation % 2 != 0 ):
                            if sumation not in computerArray:
                                for i in range ( 3 , 9 , 2 ):
                                    if ( GameData[i] == -100 ):
                                        GameData[i] = sumation
                                        computerArray.append( sumation )
                                        GamePosition[i] = "X"
                                        Play_Number = 1


            # Computer Turn
            if ( Play_Number == 0 ):
                # Check For Player Win
                defence = 0
                start   = 1
                end     = 4
                loop_end = 0
                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( start , end , 1 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( start , end , 1 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        start += 3
                        end   += 3
                        if ( end > 10 ):
                            break

                start = 1
                end   = 8
                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( start , end , 3 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( start , end , 3 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        start += 1
                        end   += 1
                        if ( end > 10 ):
                            break
                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( 1 , 10 , 4 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( 1 , 10 , 4 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        else:
                            break

                if ( defence == 0 ):
                    while ( True ):
                        counter = 0
                        for i in range ( 3 , 10 , 2 ):
                            if ( GameData[i] == -100 ):
                                counter += 1
                        if ( counter == 1 ):
                            for i in range ( 3 , 10 , 2 ):
                                if ( GameData[i] == -100 ):
                                    Random_Pos = i
                                    defence    = 1
                                    loop_end   = 1
                            if ( loop_end == 1 ):
                                break
                        else:
                            break
                        
                if ( defence == 0 ):
                    while ( True ):
                        Random_Pos = random.randint(1,9)
                        if ( GameData[ Random_Pos ] == -100 ):
                            break
                    
                while ( True ):
                    Random_Val = random.randint(0,9)
                    if ( Random_Val % 2 != 0 ):
                        if Random_Val not in computerArray:
                            break
                GameData[ Random_Pos ] = Random_Val
                GamePosition[ Random_Pos ] = "X"
                computerArray.append( Random_Val )


        time.sleep(1.2)
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
            print(" "*16  ,"=========================================")
            print(" "*16 , "|         COMPUTER IS THE WINNER        |")
            print(" "*16 , "=========================================")
            break

        counter = 0
        for i in range ( 1 , 10 ):
            if ( GamePosition[i] != "X" ):
                counter += 1
        if ( counter == 0 ):
            print(" "*16  ,"=========================================")
            print(" "*16 , "|               NO WINNER               |")
            print(" "*16 , "=========================================")
            break



    end = str( input("If tou want to play another game press (Y) key : ") )
    if ( end != "y" and end != "Y" ):
        break
