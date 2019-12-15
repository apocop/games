// Chips Game.

#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

// Maximum number of chips allowed.
const int MAX_CHIPS = 100;
const float MAX_TURN = .5;
int main()
{
	bool player1Turn = true;
	bool gameOver = false;
	
	int chipsInPile = 0;
	int chipsTaken = 0;
	int maxPerTurn = 0;
	
	char userChoice;
	// Seed the random number generator.
	srand(time(0));
	
	// Get players' names.
	string playerName[2];
	cout << "Player 1, please enter your name: \n";
	cin >> playerName[0];
	cout << "Player 2, please enter your name: \n";
	cin >> playerName[1];
	cout << "\nThanks and good luck!\n";

	
	do{	
		// Create a random number of chips in the pile.
		chipsInPile = (rand() % MAX_CHIPS) + 1;
		cout << "\nThis round will start with " << chipsInPile << " chips in the pile.\n";
		gameOver = false;
		
		while (gameOver == false)
		{
			do
			{
				if (player1Turn)
				{
					cout << playerName[0] << ": How many chips would you like?\n";
				}
				else
				{
					cout << playerName[1] << ": How many chips would you like?\n";
				}
				maxPerTurn = (chipsInPile * MAX_TURN);
				
				cout << "You can only take ";
				
				if (maxPerTurn == 0)
				{
					cout << " 1\n";
				}
				else
				{
					cout << maxPerTurn << endl;
				}
				
				cin >> chipsTaken;
				
			} while ((chipsTaken > maxPerTurn) && (chipsInPile > 1));
			
			chipsInPile = chipsInPile - chipsTaken;
			cout << "There are " << chipsInPile << " left in the pile.\n";
			if (chipsInPile == 0)
			{
				gameOver = true;
				// Declare winner.
				if (player1Turn)
				{
					cout << playerName[1] << ", congratulations you won!\n";
				}
				else
				{
					cout << playerName[0] << ", congratulations you won!\n";
				}
			}
			else
			{
				player1Turn = !player1Turn;
			}
			
		}
		
		cout << "\nWould you like to play again? (Y/N):\n";
		cin >> userChoice;
		
   } while ((userChoice == 'y') || (userChoice == 'Y'));  
	return 0;
}

