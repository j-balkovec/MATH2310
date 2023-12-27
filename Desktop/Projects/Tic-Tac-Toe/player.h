/** DOCUMENTATION
 * @file player.h
 * @author Jakob Balkovec
 * @brief Header file for the Player class.
 * This file defines the Player class, 
 * which represents a player in the Tic-Tac-Toe game.
 */

//#pragma once
#ifndef PLAYER_H
#define PLAYER_H

#include <string>
#include <random>

std::string const PLAYER = "AI Model Yoshua";

class Player {
protected:
  char symbol;
  int points;
  std::string name;
  int row;
  int col;
  
public:
  Player(std::string name, char symbol);
  virtual ~Player() {} // virtual destructor
  char get_symbol();
  void award_point();
  int get_points();
  std::string get_name();
  int random_number();
  int make_row();
  int make_col();
};
#endif //PLAYER_H
