// Chips Game.

#include <iostream>
#include <ctime>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

// Function prototypes.
string FindPlayerName(string names[], bool playerTurn);
void getUserNames(string players[]);
int askMove(bool player1Turn, int chipsInPile, string names[]);


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
	// Seed the random number generator.
	srand(time(0));

	ofstream outFile;
	outFile.open("chips_win_record.txt", ios::app);
	
	// Get players' names.
	string playerNames[2];
	getUserNames(playerNames);
	
	do{	
		// Create a random number of chips in the pile.
		chipsInPile = (rand() % MAX_CHIPS) + 1;
		cout << "\nThis round will start with " << chipsInPile << " chips in the pile.\n";
		gameOver = false;
		int moveCounter = 0;
		
		while (gameOver == false)
		{
			chipsTaken = askMove(player1Turn, chipsInPile, playerNames);
			
			chipsInPile = chipsInPile - chipsTaken;
			cout << "There are " << chipsInPile << " left in the pile.\n";
			moveCounter++;
			if (chipsInPile == 0)
			{
				gameOver = true;
				cout << FindPlayerName(playerNames, player1Turn) << ", congratulations you won!\n";
				outFile << FindPlayerName(playerNames, player1Turn) << " won in with " << moveCounter << " moves.\n";
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


string FindPlayerName(string names[], bool playerTurn)
{
	if (playerTurn)
		return names[0];
	else
		return names[1];
}

void getUserNames(string players[])
{
	cout << "Player 1, please enter your name: \n";
	cin >> players[0];
	cout << "Player 2, please enter your name: \n";
	cout << "Enter 'AI' to play against the computer.\n";
	cin >> players[1];
	cout << "\nThanks and good luck!\n";
}


int askMove(bool player1Turn, int chipsInPile, string names[])
{
	int chipsTaken;
	int maxPerTurn;
	
	do
	{
		maxPerTurn = (chipsInPile * MAX_TURN);
		
		cout << FindPlayerName(names, player1Turn) << ": How many chips would you like?\n";
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
		if (FindPlayerName(names, player1Turn) == "AI")
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

