CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRCS = main.cpp single_l.cpp

OBJS = $(SRCS:.cpp=.o)

TARGET = prog

$(TARGET): $(OBJS)
	@echo "Linking $(TARGET)..."
	$(CXX) $(CXXFLAGS) $^ -o $@

%.o: %.cpp
	@echo "Compiling $<..."
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	@echo "Cleaning..."
	rm -f $(OBJS) $(TARGET)
