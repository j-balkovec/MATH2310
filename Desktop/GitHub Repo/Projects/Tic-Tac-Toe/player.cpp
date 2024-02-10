/** DOCUMENTATION
 * @file player.cpp
 * @author Jakob Balkovec
 * @brief source file for my player in my TIC-TAC-TOE [p3]
 */

#include "player.h"
#include "board.h"
#include <iostream>


/** DODCUMENTATION
 * @brief Constructor for class Player
 * This constructor initializes the symbol and points
 * of a player.
 * @param symbol The symbol representing a player's moves
 * on the Tic-Tac-Toe board.
 */
Player::Player(std::string name, char symbol) : name(name), symbol(symbol){ 
  points = 0;
}

/** DOCUMENTATION
 * @brief Getter for the player's symbol
 * This function returns the symbol representing a player's moves
 * on the Tic-Tac-Toe board.
 * @return The symbol representing the player.
 */
char Player::get_symbol() {
  return symbol;
}

/** DOCUMENTATION
 * @brief Increments the player's points
 * This function increments the points of a player by 1.
 */
void Player::award_point() {
  this->points++;
}

/** DOCUMENTATION
 * @brief Getter for the player's points
 * This function returns the number of points a player has scored.
 * @return The number of points the player has scored.
 */
int Player::get_points() {
  return points;
}

/** DOCUMENTATION
 * @brief Getter for the player's name
 * This function returns the name of a player.
 * @return The name of the player.
 */
std::string Player::get_name() {
  return name;
}

/** DOCUMENTATION
 * @brief Generates a random number between 1 and 3
 * @return return an intiger
 */
int Player::random_number() {
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<> dis(1, 3);
  int random_number = dis(gen);
  return random_number;
}

/** DOCUMENTATION
 * @brief calls random_number() to get a row
 * @return returns an intiger (row)
 */
int Player::make_row() {
  row = random_number();
  return row;
}

/** DOCUMENTATION
 * @brief calls random_number() to get a col
 * @return returns an intiger (col)
 */
int Player::make_col() {
  col = random_number();
  return col;
}

///@endcond -> end of file