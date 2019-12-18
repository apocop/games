// Chips Game.

#include <iostream>
#include <ctime>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

struct player
{
	string name;
	int numWins;
};

// Function prototypes.
string FindPlayerName(player[], bool playerTurn);
void getUserNames(player[]);
int askMove(bool player1Turn, int chipsInPile, player[]);

// Maximum number of chips allowed.
const int MAX_CHIPS = 100;
const float MAX_TURN = .5;


int main()
{
	bool player1Turn = true;
	bool gameOver = false;
	
	int chipsInPile = 0;
	int chipsTaken = 0;
	
	char userChoice;
	player Players[2];

	// Seed the random number generator.
	srand(time(0));

	ofstream outFile;
	outFile.open("chips_win_record.txt", ios::app);
	
	// Get players' names.
	string playerNames[2];
	getUserNames(Players);
	
	do{	
		// Create a random number of chips in the pile.
		chipsInPile = (rand() % MAX_CHIPS) + 1;
		cout << "\nThis round will start with " << chipsInPile << " chips in the pile.\n";
		gameOver = false;
		int moveCounter = 0;
		
		while (gameOver == false)
		{
			chipsTaken = askMove(player1Turn, chipsInPile, Players);
			
			chipsInPile = chipsInPile - chipsTaken;
			cout << "There are " << chipsInPile << " left in the pile.\n";
			moveCounter++;
			if (chipsInPile == 0)
			{
				gameOver = true;
				cout << FindPlayerName(Players, player1Turn) << ", congratulations you won!\n";
				outFile << FindPlayerName(Players, player1Turn) << " won in with " << moveCounter << " moves.\n";
			}
			else
			{
				player1Turn = !player1Turn;
			}
			
		}
		
		cout << "\nWould you like to play again? (Y/N):\n";
		cin >> userChoice;
		userChoice = tolower(userChoice);
   } while (userChoice == 'y');  
	return 0;
}


string FindPlayerName(player Players[], bool playerTurn)
{
	if (playerTurn)
		return Players[0].name;
	else
		return Players[1].name;
}

void getUserNames(player Players[])
{
	cout << "Player 1, please enter your name: \n";
	cin >> Players[0].name;
	cout << "Player 2, please enter your name: \n";
	cout << "Enter 'AI' to play against the computer.\n";
	cin >> Players[1].name;
	cout << "\nThanks and good luck!\n";
	Players[0].numWins = 0;
	Players[1].numWins = 0;
	
}


int askMove(bool player1Turn, int chipsInPile, player Players[])
{
	int chipsTaken;
	int maxPerTurn;
	
	do
	{
		maxPerTurn = (chipsInPile * MAX_TURN);
		
		cout << FindPlayerName(Players, player1Turn) << ": How many chips would you like?\n";
		cout << "You can only take ";
		if (maxPerTurn == 0)
		{
			cout << "1\n";
		}
		else
		{
			cout << maxPerTurn << endl;
		}
		
		// AI Player plays turn.
		if (FindPlayerName(Players, player1Turn) == "AI")
		{
			if (maxPerTurn == 0)
			{
				chipsTaken = 1;
			}
			else
			{
				chipsTaken = (rand() % maxPerTurn) + 1;
			}
				
		}
		else
		{
			cin >> chipsTaken;
		}
			
	} while ((chipsTaken > maxPerTurn) && (chipsInPile > 1));
	return chipsTaken;
}

