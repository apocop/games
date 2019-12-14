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
	
	string playerName[2];
	cout << "Player 1, please enter your name: \n";
	cin >> playerName[0];
	cout << "Player 2, please enter your name: \n";
	cin >> playerName[1];
	
 
	
	// Seed the random number generator.
	srand(time(0));
	
	// Start the game with a random number of chips in the pile.
	chipsInPile = (rand() % MAX_CHIPS) + 1;
	
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
			cout << "This round will start with " << chipsInPile << " chips in the pile.\n";
			maxPerTurn = (chipsInPile * MAX_TURN);
			cout << "You can only take " << maxPerTurn << endl;
			cin >> chipsTaken;
		} while ((chipsTaken > maxPerTurn) && (chipsInPile > 1));
		
		chipsInPile = chipsInPile - chipsTaken;
		cout << "There are " << chipsInPile << " left in the pile.\n";
		if (chipsInPile == 0)
		{
			gameOver = true;
		}
		else
		{
			player1Turn = !player1Turn;
		}
		
	}
	
	
	return 0;
}

