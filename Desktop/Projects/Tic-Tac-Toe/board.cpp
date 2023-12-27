/** DOCUMENTATION
 * @file board.cpp
 * @author Jakob Balkovec
 * @brief source file for my board in my TIC-TAC-TOE [p3]
 */

#include <ctime>
#include <unistd.h>
#include <iostream>
#include <iomanip>
#include "board.h"
#include "player.h"

int const BOARD = 3;

std::string const SPACE5  = "     ";
std::string const SPACE4  = "    ";
std::string const SPACE3  = "   ";
std::string const SPACE2  = "  ";

std::string const LABEL1  = "[1]";
std::string const LABEL2  = "[2]";
std::string const LABEL3  = "[3]";

float const PAUSE = 0.75;

std::string const HORLINE = "---+---+---";

char const        SPACE1  = ' ';

char const        SYMBOLX = 'X';
char const        SYMBOLO = 'O';

char const        LINE    = '|';
char const        YES     = 'Y';


/** DOCUMENTATION
 * @brief Constructor for Board class.
 * Initializes the size of the board and creates an 2D array of chars to represent the squares on the board.
 * Each square is initialized to a space character (' ').
 * @param size The size of the board (e.g. size=3 creates a 3x3 board).
 * @pre The input size must be a positive integer.
 * @post A new Board object will be created with 
 * the specified size and all squares initialized to ' '.
 */
Board::Board(){
  squares = new char*[BOARD];
  for (int i = 0; i < BOARD; i++)
    squares[i] = new char[BOARD];
  
  for (int i = 0; i < BOARD; i++)
    for (int j = 0; j < BOARD; j++)
      squares[i][j] = ' '; //fill em so it doesnt cause an error
}

/** DOCUMENTATION
 *  @brief The destructor for the Board class
 *  This destructor is responsible for freeing
 *  the memory that was dynamically allocated by the class.
 *  @pre The Board object must have been initialized.
 *  @post All dynamically allocated memory associated with 
 *  the Board object will be freed.
 */
Board::~Board(){
  for (int i = 0; i < BOARD; i++) {
    delete[] squares[i];
  }
  delete[] squares;
}

/** DOCUMENTATION
 *  @brief Displays the current state of the Board
 *  This function outputs the current state of the board,
 *  displaying the values of each square in a formatted manner.
 *  @param size The size of the board (number of squares on each side)
 *  @pre The input size must match the size of the current Board object.
 *  @post The current state of the Board will be displayed on the console.
 */
void Board::display() {
  std::cout << std::endl << std::endl;
  std::cout << SPACE5 << LABEL1 << SPACE1 << LABEL2 << SPACE1 << LABEL3 << std::endl; // probs shouldnt hardcode
  std::cout << std::endl;
  for (int i = 0; i < BOARD; i++) {
    std::cout << "[" << i + 1 << "]" << SPACE2; // numbers
    for (int j = 0; j < BOARD; j++) {         // only exectues twice for vertical lines
      std::cout << SPACE1 << squares[i][j];
      if (j < BOARD - 1) {
	std::cout << SPACE1 << LINE;
      }
    }
    std::cout << std::endl;
    if (i < BOARD - 1) {
      std::cout << SPACE5 << HORLINE << std::endl;
    }
  }
  std::cout << "\n\n";
}

/** DOCUMENTATION
 *  @brief Determines if the Board is full
 *  This function checks if all squares in the Board are filled.
 *  @return True if all squares are filled, false otherwise.
 *  @pre None.
 *  @post Returns true if board is full and false if board is empty.
 */
bool Board::is_full(){
  for (int i = 0; i < BOARD; i++) {
    for (int j = 0; j < BOARD; j++) {
      if (squares[i][j] == ' ')
	return false;
    }
  }
  return true;
}

/** DOCUMENTATION
 *  @brief Determines if a player has won
 *  This function checks if the specified player has won the 
 *  game by having a full row, column, or diagonal of their symbol.
 *  @param player The player to check for a win
 *  @return True if the player has won, false otherwise.
 *  @pre The input player must be a valid player in the game.
 *  @post The win status of the specified player will be determined.
 */
bool Board::is_winner(Player player) {
  // Check rows
  for (int i = 0; i < BOARD; i++) {
    int j;
    for (j = 0; j < BOARD; j++) {
      if (squares[i][j] != player.get_symbol()) {
        break;
      }
    }
    if (j == BOARD) {
      return true;
    }
  }
  
  // Check columns
  for (int i = 0; i < BOARD; i++) {
    int j;
    for (j = 0; j < BOARD; j++) {
      if (squares[j][i] != player.get_symbol()) {
        break;
      }
    }
    if (j == BOARD) {
      return true;
    }
  }
  
  // Check diagonal from top-left to bottom-right
  int i;
  for (i = 0; i < BOARD; i++) {
    if (squares[i][i] != player.get_symbol()) {
      break;
    }
  }
  if (i == BOARD) {
    return true;
  }
  
  // Check diagonal from top-right to bottom-left
  for (i = 0; i < BOARD; i++) {
    if (squares[i][BOARD - i - 1] != player.get_symbol()) {
      break;
    }
  }
  if (i == BOARD) {
    return true;
  }
  
  return false;
}

/** DOCUMENTATION
 * @brief updates the square on the board with the given symbol
 * @param row row number (starts from 1)
 * @param col column number (starts from 1)
 * @param player_symbol symbol to be updated on the board
 */
void Board::update(int row, int col, char player_symbol)
{
  squares[row][col] = player_symbol;
}

/** DOCUMENTATION
 * @brief       Asks player to input the row and column for their move
 * @param[in,out] player Reference to the player object to store their move
 * @pre player is initialized
 * @post row and column of player's move are stored in player object
 */
void Board::get_move_input(Player &player, int &row, int &col) {
  std::cout << std::endl;
  std::cout << "*** [" << player.get_name() << "] je na vrsti ***\n";
  std::cout << "[ROW]: ";
  std::cin >> row;
  
  //input validation
  while (row > BOARD || row < 0) {
    std::cout << "\nNapacen vnos!\n";
    std::cout << "Ponovno vnesi [ROW]: ";
    std::cin >> row;
  }
  std::cout << "[COL]: ";
  std::cin >> col;
  
  while (col > BOARD || col < 0) {
    std::cout << "\nNapacen vnos!\n";
    std::cout << "Ponovno vnesi [COL]: ";
    std::cin >> col;
  }
}

/** DOCUMENTATION
 * @brief Makes a move for the AI player on the given game board.
 * @param ai_model A reference to the AI player.
 * @param game_board A reference to the game board.
 * This method generates a random row and column for the AI player's move using the make_row() and make_col()
 * methods of the ai_model parameter.
 * It checks if the chosen cell on the game board is already occupied, and if not, it updates the cell with
 * the AI player's symbol.
 * If the chosen cell is already occupied, the method generates new row and column values until it finds an
 * unoccupied cell.
 * It also pauses the program for 1 second before making the move.
*/
void Board::ai_move(Player &ai_model, Board &game_board) {
  bool occupied = true;
  
  int col = ai_model.make_col();
  int row = ai_model.make_row();
  
  occupied = game_board.ai_occupied(row - 1, col - 1);
  
  if (!occupied) {
    game_board.update(row - 1, col - 1, ai_model.get_symbol());
  } else {
    while (occupied) {
      col = ai_model.make_col();
      row = ai_model.make_row();
      occupied = game_board.ai_occupied(row - 1, col - 1);
    }
    sleep(PAUSE);
    game_board.update(row - 1, col - 1, ai_model.get_symbol());
  }
}


/** DOCUMENTATION
 * @pre None.
 * @post Return true if the square is occupied, false otherwise.
 * @param row Row index of the square to be checked.
 * @param col Column index of the square to be checked.
 * @return True if the square is occupied, false otherwise.
 */
bool Board::occupied(int row, int col) { //should I pass by reference
  if(squares[row][col] != ' ') {
    std::cout << "To polje je ze zasedneo, poskusi ponovno!\n\n";
    return true;
  }
  return false;
}

/** DOCUMENTATION
 * @pre None.
 * @post Return true if the square is occupied, false otherwise.
 * @param row Row index of the square to be checked.
 * @param col Column index of the square to be checked.
 * @return True if the square is occupied, false otherwise.
 */
bool Board::ai_occupied(int row, int col) { //should I pass by reference
  if(squares[row][col] != ' ') {
    return true;
  }
  return false;
}

/** DOCUMENTATION
 * @brief       Asks player to input the row and column for their move
 * @param[in,out] player Reference to the player object to store their move
 * @pre player is initialized
 * @post row and column of player's move are stored in player object
 */
void Board::take_turn(Player &player_1, Player &player_2) {
  bool   can_place_1;
  bool   can_place_2;
  
  char   player_1_symbol = player_1.get_symbol();
  char   player_2_symbol = player_2.get_symbol();
  Board game_board;
  int   row = 0;                
  int   col = 0;             
  while (!game_board.is_full() && 
         !game_board.is_winner(player_1) && 
         !game_board.is_winner(player_2)){
    
    game_board.display();
    can_place_1 = true;
    while (can_place_1) {
      game_board.get_move_input(player_1, row, col);
      can_place_1 = game_board.occupied(row - 1, col - 1);
    }
    game_board.update(row - 1, col - 1, player_1_symbol);
    
    if (!game_board.is_full() && !game_board.is_winner(player_1) && !game_board.is_winner(player_2)) {
      
      game_board.display();
      
      can_place_2 = true;
      while (can_place_2 == true) {
	game_board.get_move_input(player_2, row, col);
	can_place_2 = game_board.occupied(row - 1, col - 1);
      }
      
      game_board.update(row - 1, col - 1, player_2_symbol);
    }
  }
  
  game_board.display();
  
  if (game_board.is_winner(player_1)) {
    std::cout << player_1.get_name() << "] je zmagal/a to igro!" << std::endl;
    player_1.award_point();
    std::cout << std::endl;
    
  } else if (game_board.is_winner(player_2)) {
    std::cout << player_2.get_name() << "] je zmagal/a to igro!" << std::endl;
    player_2.award_point();
    std::cout << std::endl;
    
  } else {
    std::cout << "Izenaceno!" << std::endl;
  }
  
  std::cout << "Igralec/ka [" << player_1.get_name() << "]: " << player_1.get_points() << " tock" << std::endl;
  std::cout << "Igralec/ka [" << player_2.get_name() << "]: " << player_2.get_points() << " tock" << std::endl;
}


/** DOCUMENTATION
 * @brief       Asks player to input the row and column for their move
 * @param[in,out] player Reference to the player object to store their move
 * @pre player is initialized
 * @post row and column of player's move are stored in player object
 */
void Board::ai_take_turn(Player &player_1, Player &ai_model) {
  bool   can_place_1;
  bool   can_place_2;
  
  char   player_1_symbol = player_1.get_symbol();
  char   player_2_symbol = ai_model.get_symbol();
  Board game_board; 
  int   row = 0;                
  int   col = 0;                
  while (!game_board.is_full() && 
         !game_board.is_winner(player_1) && 
         !game_board.is_winner(ai_model)){
    
    game_board.display(); 
    can_place_1 = true;
    while (can_place_1) {
      game_board.get_move_input(player_1, row, col);
      can_place_1 = game_board.occupied(row - 1, col - 1);
    }
    game_board.update(row - 1, col - 1, player_1_symbol);
    
    if (!game_board.is_full() && !game_board.is_winner(player_1) && !game_board.is_winner(ai_model)) {
      game_board.display();
      ai_move(ai_model, game_board);
    }
  }
  
  game_board.display();
  
  if (game_board.is_winner(player_1)) {
    std::cout << player_1.get_name() << "] je zmagal/a to igro!" << std::endl;
    player_1.award_point();
    std::cout << std::endl;
    
  } else if (game_board.is_winner(ai_model)) {
    std::cout << ai_model.get_name() << " je zmagal to igro!" << std::endl;
    ai_model.award_point();
    std::cout << std::endl;
    
  } else {
    std::cout << "Izenaceno!" << std::endl;
  }
  
  std::cout << "Igralec/ka [" << player_1.get_name() << "]: " << player_1.get_points() << " tock" << std::endl;
  std::cout << ai_model.get_name() << ": " << ai_model.get_points() << " tock" << std::endl;
}

///@endcond -> end of file
