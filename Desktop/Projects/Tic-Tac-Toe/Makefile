CXX=g++
CXXFLAGS=-std=c++11

SRCS=board.cpp player.cpp main.cpp
OBJS=$(SRCS:.cpp=.o)

all: TTT

TTT: $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o tictactoe

board.o: board.h board.cpp
	$(CXX) $(CXXFLAGS) -c board.cpp

player.o: player.h player.cpp board.h
	$(CXX) $(CXXFLAGS) -c player.cpp

main.o: board.h player.h main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp

clean:
	rm -f $(OBJS) tictactoe
