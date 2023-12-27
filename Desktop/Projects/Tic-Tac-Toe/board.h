/** DOCUMENTATION
 * @file board.h
 * @author Jakob Balkovec
 * @brief Header file for the Board class.
 * This file defines the Board class, 
 * which represents a board in the Tic-Tac-Toe game.
 */

//#pragma once
#ifndef BOARD_H
#define BOARD_H

#include "player.h"
#include <iostream>

class Board {
private:
  char** squares;
  int size;
  
public:
  Board();
  ~Board();
  void display();
  bool is_full();
  bool is_winner(Player player);
  void update(int row, int col, char player_symbol);
  void get_move_input(Player &player, int &row, int &col);
  bool occupied(int row, int col);
  void take_turn(Player &player);
  int random_numby();
  void take_turn(Player &player_1, Player &player_2);
  void ai_take_turn(Player &player_1, Player &ai_model);
  void ai_move(Player &ai_model, Board &game_board);
  bool ai_occupied(int row, int col);
};

#endif //BOARD_H
