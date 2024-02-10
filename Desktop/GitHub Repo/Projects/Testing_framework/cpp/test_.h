//
//  test_file.h
//  linked_list_xcode
//
//  Created by Jakob Balkovec on 13/06/2023.
//

  // static void printColoredMessage(const std::string& message, const std::string& color = "") {
  //   std::cout << color << message << COLOR_RESET;
  // }

#ifndef test_file_h
#define test_file_h

#include <functional>
#include <type_traits>
#include <string>
#include <iostream>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>

static const std::string COLOR_YELLOW = "\033[33m";
static const std::string COLOR_GREEN = "\033[32m";
static const std::string COLOR_RED = "\033[31m";
static const std::string COLOR_RESET = "\033[0m"; //white

class TEST {
private:
  /**
   * @brief A static function that returns the current timestamp as a string.
   * @return the current timestamp as a string
   */
  inline static std::string get_timestamp() {
      return __TIME__;
  }

  /**
   * Prints a message depending on the invoked function
   * @param func the name of the function to invoke
   * @throws ErrorType a description of any error that can occur
   */
  inline static void invoke(const char* func) {
    std::cout << COLOR_YELLOW << "\n[TIME: " << get_timestamp() << "]  __" << func << "::INVOKED\n";
  }

  /**
   * Prints a test passing message with an optional function name.
   * @param func_name an optional name of the function being tested
   * @return void
   * @throws none
   */
  inline static void PRINT_PASS(const std::string& func_name = "") {
    std::cout << COLOR_GREEN << "[TEST " << func_name << " PASSED]" << COLOR_RESET << std::endl;
  }
  
  /**
   * Prints a failure message for a test, including an optional message and function name.
   * @param message the message to include in the failure message (optional)
   * @param func_name the name of the function being tested (optional)
   * @return void
   * @throws none
   */
  inline static void PRINT_FAIL(const std::string& message= "", const std::string& func_name = "") {
    std::cout << COLOR_RED << "[TEST " << func_name << " FAILED]";
    if (!message.empty()) {
      std::cout << "  " << message;
    }
    std::cout << COLOR_RESET << std::endl;
  }
  
public:
  /**
   * A function that checks a boolean condition, prints a pass message if the condition is true,
   * otherwise prints a fail message with an optional custom message and function name.
   * @param condition the boolean condition to check
   * @param message an optional custom message to print in the fail message
   * @param func_name an optional function name to print in the fail message
   * @throws no exceptions thrown
   */
  template <typename T, typename = typename std::enable_if<std::is_same<T, bool>::value>::type>
  static void ASSERT(T condition, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    if (condition) {
      PRINT_PASS(func_name);
    } else {
      PRINT_FAIL(message, func_name);
    }
  }
  
  /**
   * Compares the expected and actual values and prints a pass or fail 
   * message with an optional custom message along with the expected and actual values.
   * @tparam T the data type of the expected and actual values
   * @param expected the expected value
   * @param actual the actual value
   * @param message an optional message to print on failure
   * @param func_name an optional function name to print in the pass or fail message
   * @return void
   */
  template <typename T, typename = typename std::enable_if<!std::is_same<T, std::string>::value>::type>
  static void ASSERT_EQUAL(const T& expected, const T& actual, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    if (expected == actual) {
      PRINT_PASS(func_name);
    } else {
      PRINT_FAIL(message, func_name);
      std::cout << "\n[expected]: " << expected << " ->  [actual]: " << actual << std::endl;
    }
  }
  
  /**
   * Compares the given actual and expected values and prints a pass message if they are not equal.
   * Otherwise, prints a fail message and the actual and not expected values.
   * @param notExpected the expected value
   * @param actual the actual value to be compared with the expected value
   * @param message an optional message to print if the comparison fails
   * @param func_name an optional name of the function for debugging purposes
   * @throws none
   */
  template <typename T, typename = typename std::enable_if<!std::is_same<T, std::string>::value>::type>
  static void ASSERT_NOT_EQUAL(const T& notExpected, const T& actual, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    if (notExpected != actual) {
      PRINT_PASS(func_name);
    } else {
      PRINT_FAIL(message, func_name);
      std::cout << "\n[not expected]: " << notExpected << " ->  [actual]: " << actual << std::endl;
    }
  }
  
  /**
   * A function that asserts whether a condition is true. If the condition is true,
   * prints a pass message; otherwise, prints a fail message.
   * @param condition a boolean representing the condition to be tested
   * @param message optional message to be printed in the event of a failure
   * @param func_name optional name of the function being tested
   * @throws none
   */
  template <typename T, typename = typename std::enable_if<std::is_same<T, bool>::value>::type>
  static void ASSERT_TRUE(bool condition, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    if (condition) {
      PRINT_PASS(func_name);
    } else {
      PRINT_FAIL(message, func_name);
    }
  }
  
  /**
   * Checks if a given condition is false and prints either a pass message or a fail 
   * message with a given function name and message.
   * @param condition boolean expression to check
   * @param message optional message to print if the condition is true
   * @param func_name optional function name to print with the fail message
   * @throws none
   */
  template <typename T, typename = typename std::enable_if<std::is_same<T, bool>::value>::type>
  static void ASSERT_FALSE(bool condition, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    if (!condition) {
      PRINT_PASS(func_name);
    } else {
      PRINT_FAIL(message, func_name);
    }
  }
  
  /**
   * Runs a statement and catches any exceptions of type ExceptionType.
   * If an exception of type ExceptionType is caught, the function will print a pass message.
   * If another type of exception is caught, the function will print a fail message 
   * and the type of exception thrown.
   * If no exception is thrown, the function will print a fail message.
   * @param statement the statement to run
   * @param message an optional message to print if the statement fails
   * @param func_name an optional name of the function being tested
   *
   * @throws ExceptionType if the statement throws an exception of this type
   */
  template <typename ExceptionType>
  static void ASSERT_THROW(const std::function<void()>& statement, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    try {
      statement();
      PRINT_FAIL(message, func_name);
    } catch (const ExceptionType&) {
      PRINT_PASS(func_name);
    } catch (...) {
      PRINT_FAIL(message, func_name);
      std::cout << "[expected exception type]: " << typeid(ExceptionType).name() << std::endl;
    }
  }
  
  /**
   * Method that takes in a std::function object, 
   * a string message, and a string function name. It attempts to execute the provided statement,
   * and if an exception of type ExceptionType is thrown, it prints a failed message and an 
   * optional error message and function name. If any other type of exception is thrown, it 
   * prints a failed message and an optional error message and function name.
   * @param statement The std::function object that is to be executed.
   * @param message Optional string error message to print alongside the failed message.
   * @param func_name Optional string function name to print alongside the failed message.
   * @throws ExceptionType If this type of exception is thrown by the statement.
   */
  template <typename ExceptionType>
  static void ASSERT_NO_THROW(const std::function<void()>& statement, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    try {
      statement();
      PRINT_PASS(func_name);
    } catch (const ExceptionType&) {
      PRINT_FAIL(message, func_name);
      std::cout << "[unexpected exception type]: " << typeid(ExceptionType).name() << std::endl;
    } catch (...) {
      PRINT_FAIL(message, func_name);
    }
  }
  
  /**
   * Compares the given value with a given threshold and prints a pass 
   * or fail message based on the comparison.
   * @param value the value to be compared
   * @param threshold the threshold value to compare against
   * @param message an optional message to be printed in case of a fail
   * @param func_name the name of the calling function
   * @throws None
   */
  template <typename T, typename = typename std::enable_if<!std::is_same<T, std::string>::value>::type>
  static void ASSERT_GREATER(const T& value, const T& threshold, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    if (value > threshold) {
      PRINT_PASS(func_name);
    } else {
      PRINT_FAIL(message, func_name);
      std::cout << "[value]: " << value << " -> [threshold]: " << threshold << std::endl;
    }
  }
  
  /**
   * Compares the given value with the given threshold and prints a message based on the result.
   * @param value the value to compare with the threshold
   * @param threshold the threshold to compare the value with
   * @param message an optional message to print if the comparison fails
   * @param func_name an optional function name to print in the pass/fail message
   * @throws N/A
   */
  template <typename T, typename = typename std::enable_if<!std::is_same<T, std::string>::value>::type>
  static void ASSERT_LESS(const T& value, const T& threshold, const std::string& message = "", const std::string& func_name = "") {
    invoke(__func__);
    if (value < threshold) {
      PRINT_PASS(func_name);
    } else {
      PRINT_FAIL(message, func_name);
      std::cout << "[value]: " << value << " -> [threshold]: " << threshold << std::endl;
    }
  }
};


#endif /* test_file_h */
