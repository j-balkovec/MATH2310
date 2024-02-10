#include <iostream>
#include <thread>
#include <string>
#include "test_.h"

void func() {
  // Test case 1
  bool condition1 = true;
  TEST::ASSERT(condition1, "Test case 1 failed", "test_function"); //pass

  // Test case 2
  bool condition2 = false;
  TEST::ASSERT(condition2, "Test case 2 failed", "test_function"); //fail
}

inline void info(const std::string& func, const std::string& file) {
    std::cout << "[running " << func << ", in " << file << "]" << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(2));
}

int main() {
  info(__func__,__FILE__);
  func();
  return 0;
}