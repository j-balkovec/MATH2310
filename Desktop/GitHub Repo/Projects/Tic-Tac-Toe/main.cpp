/** DOCUMENTATION
 * @file p3.cpp
 * @author Jakob Balkovec
 * @typedef Project 3
 * @brief Driver code for my Project 3 ("TIC-TAC_TOE with classes")
 */

#include <cstdlib>
#include <iostream>
#include "board.h"
#include "player.h"

char const YES = 'J';
int const MAX = 9;
int const MIN = 1;
char const SYMBOLX = 'X';
char const SYMBOLO = 'O';
std::string const PVP = "PvP";
std::string const AI = "AI";

/** DOCUMENTATION
 * @brief Prompts the user to enter their name and returns it.
 * @return std::string the name entered by the user.
 */
std::string name() {
  std::string name_1;
  std::cout << "Vnesi svoje ime: ";
  std::cin >> name_1;
  std::cin.ignore();
  std::cout << std::endl;
  return name_1;
}

/** DOCUMENTATION
 * @brief Prompts the user to enter their symbol and returns it.
 * @return char The symbol entered by the user.
 */
char symbol() {
  char symbol_1;
  std::cout << "Vnesi svoj simbol: ";
  std::cin >> symbol_1;
  std::cin.ignore();
  std::cout << std::endl;
  return symbol_1;
}

/** DOCUMENTATION
 * @brief Displays a welcome message to the player
 */
void welcome() {
  std::cout << "*** Pozdravljeni v Jakobovi Igri Tic-Tac-Toe! *** \n\n";
  std::cout << "Pritisni [Enter] za nadaljevanje ";
  std::cin.ignore();
  
  std::cout << "\n\n*** Nacina igranja ***\n\n";
  std::cout << "[PvP] -> igralec proti igralcu\n";
  std::cout << "[AI]  -> igra proti racunalniku\n";
  std::cout << "\n\n";
}

/** DOCUMENTATION
 * @brief Displays a goodbye message to the player
 */
void goodbye() {
  std::cout << "\nOk, Hvala za obisk!\n";
  std::cin.ignore();
}

/** DOCUMENTATION
 * @brief AI model promts an introduction to the player
 */
void AI_model() {
  std::cout << "\nPozdravljen/a sem " << PLAYER << " in danes bom s teboj igral igro TIC-TAC-TOE!\n";
  std::cout << "Pritisni [Enter] za nadaljevanje! ";
  std::cin.ignore();
}

/** DOCUMENTATION
 * @brief Prompts the player to select the mode he wishes to play
 * @return string type value that indicates the mode he wishes to play
 */
std::string select_mode() {
  std::string mode;
  std::cout << "Izberite nacin igre: ";
  std::cin >> mode;
  while(mode != "PvP" && mode!= "AI") {
    std::cout << "Tega nacina igre ne prepoznam... Opcije [AI, PvP]\n";
    std::cout << "Ponovno vnesi nacin igre: ";
    std::cin >> mode;
    std::cin.ignore();
  }
  return mode;
}

/** DOCUMENTATION
 * @brief Promtes the player if he wishes to play agian
 * @return a char type value indicating whether the player wants to play agin
 */
char play_again() {
  char choice;
  std::cout << std::endl;
  std::cout << "Bi radi igral/a ponovno? (J/N): ";
  std::cin >> choice;
  return choice;
}

/** DOCUMENTATION
 * @brief The main function of the Tic-Tac-Toe game.
 *
 * This function initializes the players, gets the size of the board from the user, 
 * creates the board, displays the board, takes input from the players, 
 * updates the board, checks the winner, announces the winner, displays the scores, 
 * and finally, asks the user if they want to play again.
 * If the user does not want to play again, 
 * the function calls the `goodbye` function.
 */
int main(int argc, char *argv[]) {
  std::cout << std::endl << std::endl;
  welcome();
  std::string mode = select_mode();
  char choice;
  
  if(mode == "PvP") {
    std::string name_1, name_2;
    char symbol_1, symbol_2;
    
    name_1 = name();
    symbol_1 = symbol();
    Player player_1(name_1, symbol_1);
    std::cout << std::endl;
    std::cout << "[***  " << player_1.get_name() << " ima simbol " << player_1.get_symbol() << "  ***]" << std::endl;
    
    name_2 = name();
    symbol_2 = symbol();
    Player player_2(name_2, symbol_2);
    std::cout << std::endl;
    std::cout << "[***  " << player_2.get_name() << " ima simbol " << player_2.get_symbol() << "  ***]" << std::endl;
    
    Board gameboard;
    do {
      gameboard.take_turn(player_1, player_2);
      choice = play_again();
    }while (choice == YES);
    if (choice != YES) {
      goodbye();
    }
    
  } else if(mode == "AI"){
    AI_model();
    std::cout << std::endl << std::endl;
    
    std::string name_1 = name();
    Player player_1(name_1, 'X');
    std::cout << std::endl;
    std::cout << "[***  " << player_1.get_name() << " ima simbol " << player_1.get_symbol() << "  ***]" << std::endl;
    
    Player ai_model(PLAYER, 'O');
    Board gameboard;
    do {
      gameboard.ai_take_turn(player_1, ai_model);
      choice = play_again();
    }while (choice == YES);
    if (choice != YES) {
      goodbye();
    }
  }
  std::cout << std::endl << std::endl;
  return EXIT_SUCCESS;
}

///@endcond -> end of file
