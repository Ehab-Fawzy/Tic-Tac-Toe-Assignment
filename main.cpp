#include <iostream>
#include <iomanip>

using namespace std;


string Integer_To_String( int x ){
    string y = "0123456789";
    string z = "";
    for ( int i = 0; i < 10; i++ ){
        if ( x == i ){
            z = y[i];
        }
    }
    return z;
}

int main()
{
    // Variables Section
    string mess = "";
    int playernum = 1, index = 0, pos = 0, val = 0;

    // GameData
    int    GameData[10]     = {};
    string GameView[10]     = {};
    string GamePosition[10] = {"x" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" };
    for ( int i = 0; i < 10; i++ ){ GameData[i] = -100; }
    for ( int i = 0; i < 10; i++ ){ GameView[i] = " " ; }

    //Welcome Mess
    cout << "Welcome In Tic Tac Toe Game" << endl;
    cout << endl;
    cout << "This Is The Position Of The Game Board" << endl;

    cout << "|----|----|----| " << endl;
    cout << "| " << 1 << "  | " << 2 << "  | " << 3 << "  |" << endl;
    cout << "|----+----+----| " << endl;
    cout << "| " << 4 << "  | " << 5 << "  | " << 6 << "  |" << endl;
    cout << "|----+----+----| " << endl;
    cout << "| " << 7 << "  | " << 8 << "  | " << 9 << "  |" << endl;
    cout << "|----|----|----| " << endl;

    while( true ){
        cout << "Press (Y) key To Start Game : ";
        cin >> mess;
        if ( mess == "y" or mess == "Y" ){
            break;
        }
    }

    cout << endl;
    cout << "|----|----|----| "     << setw(50);
    cout << "|----|----|----| "     << endl;
    cout << "| " << GameView[1]     << "  | " << GameView[3]     << "  | " << GameView[3]     << "  |" << setw(36);
    cout << "| " << GamePosition[1] << "  | " << GamePosition[2] << "  | " << GamePosition[3] << "  |" << endl;
    cout << "|----+----+----| "     << setw(50);
    cout << "|----+----+----| "     << endl;
    cout << "| " << GameView[4]     << "  | " << GameView[5]     << "  | " << GameView[6]     << "  |" << setw(36);
    cout << "| " << GamePosition[4] << "  | " << GamePosition[5] << "  | " << GamePosition[6] << "  |" << endl;
    cout << "|----+----+----| "     << setw(50);
    cout << "|----+----+----| "     << endl;
    cout << "| " << GameView[7]     << "  | " << GameView[8]     << "  | " << GameView[9]     << "  |" << setw(36);
    cout << "| " << GamePosition[7] << "  | " << GamePosition[8] << "  | " << GamePosition[9] << "  |" << endl;
    cout << "|----|----|----| "     << setw(50);
    cout << "|----|----|----| "     << endl;
    cout << endl;

    cout << "Who Will Start ?  Player 1 or player 2 (Enter Number of Player) : ";
    while ( true ){
       cin  >>  index;
       if ( index == 1 or index == 2 ){
            break;
       }
       else{ cout << "Invalid Input " << endl; }
    }


    if ( index != playernum ){
        playernum = 2;
    }

    // main loop
    while( true ){
        cout << "\nPlayer " << playernum << " Turn" << endl;

        cout << "Choose Position : ";
        cin  >> pos;

        while ( true ){
            if ( pos > 9 or pos < 1 ){
                cout << "Oops! - Sorry Poistion Should Be In Range 1 TO 9 " << endl;
                cin  >> pos;
            }
            else{ break; }
        }

        cout << "Choose Value    : ";
        cin  >> val ;

        while ( true ){
            int check_pos = 0;
            for ( int i = 1; i < 10; i++ ){ if ( GameData[i] == val ){ check_pos = 1; } }
            if ( val > 9 or val < 0 ){
                cout << "Oops! - Sorry Value Should Be In Range 1 TO 9 " << endl;
                cout << "Choose Another Value : ";
                cin  >> val;
            }
            else if ( playernum == 1 and val % 2 == 0 ){
                cout << "Oops! - Sorry You Should Choose Odd Numbers " << endl;
                cout << "Choose Another Value : ";
                cin  >> val;
            }
            else if ( playernum == 2 and val % 2 != 0 ){
                cout << "Oops! - Sorry You Should Choose Even Numbers " << endl;
                cout << "Choose Another Value : ";
                cin  >> val;
            }
            else if ( check_pos == 1  ){
                cout << "Oops! - Sorry You Are Use This Value Before " << endl;
                cout << "Choose Another Value : ";
                cin  >> val;
            }
            else { break; }
        }

        GameData[ pos ]     = val;
        GamePosition[ pos ] = "x";
        GameView[ pos ]     = Integer_To_String(val);

        cout << endl;
        cout << "|----|----|----| "     << setw(50);
        cout << "|----|----|----| "     << endl;
        cout << "| " << GameView[1]     << "  | " << GameView[2]     << "  | " << GameView[3]     << "  |" << setw(36);
        cout << "| " << GamePosition[1] << "  | " << GamePosition[2] << "  | " << GamePosition[3] << "  |" << endl;
        cout << "|----+----+----| "     << setw(50);
        cout << "|----+----+----| "     << endl;
        cout << "| " << GameView[4]     << "  | " << GameView[5]     << "  | " << GameView[6]     << "  |" << setw(36);
        cout << "| " << GamePosition[4] << "  | " << GamePosition[5] << "  | " << GamePosition[6] << "  |" << endl;
        cout << "|----+----+----| "     << setw(50);
        cout << "|----+----+----| "     << endl;
        cout << "| " << GameView[7]     << "  | " << GameView[8]     << "  | " << GameView[9]     << "  |" << setw(36);
        cout << "| " << GamePosition[7] << "  | " << GamePosition[8] << "  | " << GamePosition[9] << "  |" << endl;
        cout << "|----|----|----| "     << setw(50);
        cout << "|----|----|----| "     << endl;
        cout << endl;

        int counter = 0;
        for ( int i = 1, j = 1 ; i < 10; i += 3, j++ ){
            if ( GameData[i] + GameData[i+1] + GameData[i+2] == 15 ){
                cout << "===========================" << endl;
                cout << "|   Player " << playernum << " The Winner   |" << endl;
                cout << "===========================" << endl;
                counter = 1;
                break;
            }
            if ( GameData[j] + GameData[j+3] + GameData[j+6] == 15 ){
                cout << "===========================" << endl;
                cout << "|   Player " << playernum << " The Winner   |" << endl;
                cout << "===========================" << endl;
                counter = 1;
                break;
            }
            if ( GameData[1] + GameData[5] + GameData[9] == 15 ){
                cout << "===========================" << endl;
                cout << "|   Player " << playernum << " The Winner   |" << endl;
                cout << "===========================" << endl;
                counter = 1;
                break;
            }
            if ( GameData[3] + GameData[5] + GameData[7] == 15 ){
                cout << "===========================" << endl;
                cout << "|   Player " << playernum << " The Winner   |" << endl;
                cout << "===========================" << endl;
                counter = 1;
                break;
            }
        }

        if ( counter == 1 ){ break; }

        counter = 0;

        for ( int i = 1 ; i < 10; i++ ){
            if ( GamePosition[i] != "x" or GamePosition[i] != "x" ){ counter += 1; }
        }
        if ( counter == 0 ){
            cout << "===========================" << endl;
            cout << "|        NO WINNER        |" << endl;
            cout << "===========================" << endl;
            break;
    }

        if ( playernum == 1 ){ playernum = 2; }
        else { playernum = 1; }
    }

    return 0;
}
/*

*/
