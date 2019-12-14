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
	
	// Seed the random number generator.
	srand(time(0));
	
	// Start the game with a random number of chips in the pile.
	chipsInPile = (rand() % MAX_CHIPS) + 1;
	cout << "This round will start with " << chipsInPile << " chips in the pile.\n";
	cout << "You can only take " << static_cast<int>(chipsInPile * MAX_TURN) << endl;
	
	return 0;
}
