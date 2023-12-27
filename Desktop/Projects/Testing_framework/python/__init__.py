'''
Testing framework in Python

Jakob Balkovec Sat 17 Jun 2023

Purpose of this file is to rewrite the mock testing framework previously written in C++, in Python
'''

import traceback
from datetime import datetime
from typing import Any

"""__constants__"""
_YELLOW: str = "\033[33m"
_GREEN: str = "\033[32m"
_RED: str = "\033[31m"
_RESET: str = "\033[0m"  # white

"""__summary__
:desc: Prints a message indicating that a test has passed.

:param: func_name (str): The name of the function being tested. Defaults to an empty string.

:return: None
"""
@staticmethod
def _print_pass(func_name: str = "") -> None:
    print(_GREEN + "[TEST {} PASSED]\n".format(func_name) + _RESET)

"""__summary__
:desc: Prints a message indicating that a test has failed.

:param: func_name (str): The name of the function being tested. Defaults to an empty string.

:return: None
"""
@staticmethod
def _print_fail(message: str = "", func_name: str = "") -> None:
    print(_RED + "[TEST {} FAILED]".format(func_name) + _RESET)
    if message != "":
        print(message)

"""__summary__
:desc: Prints the given functions name and a message with the current time.

:param: func_name (str): The name of the function to invoke.

:return: None
"""    
@staticmethod
def _invoke(func_name: str) -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"{_YELLOW}[TIME: {current_time}] __{func_name}::INVOKED__{_RESET}")
    
"""__summary__
:desc: Asserts that a given condition is true. If the condition is true, the test passes,
       otherwise the test fails and an error message is printed. The error message is
       optional and can be used to provide extra information about the failure. The name
       of the function being tested is also optional and can be used to help identify the
       source of the failure.

:param condition: A boolean value that represents the condition being tested.
:param message: An optional string that contains an error message to print if the
                condition is false.
:param func_name: An optional string that contains the name of the function being
                  tested.
:return: None
"""
@staticmethod
def ASSERT(condition: Any, message: str = "", func_name: str = "") -> None:
  _invoke(ASSERT.__name__)
  if condition:
      _print_pass(func_name = func_name)
  else:
      _print_fail(message = message, func_name = func_name)
    
    
"""__summary__
:desc: A static method that takes in two arguments: expected and actual, 
       along with two optional arguments: message and func_name. 
       If the expected and actual values are equal, _print_pass() method is called.
       Otherwise, _print_fail() method is called with the message and func_name arguments,
       and a message is printed showing the expected and actual values. 

:param condition: A boolean value that represents the condition being tested.
:param message: An optional string that contains an error message to print if the
                condition is false.
:param func_name: An optional string that contains the name of the function being
                  tested.
:return: None
"""
@staticmethod
def ASSERT_EQUAL(expected: Any, actual: Any, message: str = "", func_name: str = "") -> None:
  print(f"\n__{ASSERT_EQUAL.__name__}::INVOKED__\n")
  if expected == actual:
      _print_pass(func_name = func_name)
  else:
      _print_fail(message = message,func_name = func_name)
      print("\n[expected]: {} -> [actual]: {}".format(expected, actual))
          
          
"""__summary__
:desc: A static method that asserts if a given `not_expected` value is equal to `actual`. 
       If they are not equal, it calls `_print_pass()` with the given `func_name`.
       If they are equal, it calls `_print_fail()` with the given `message` and `func_name`, 
       and also prints the expected and actual values.


:param: not_expected: The value that is not expected to be equal to `actual`.
:param: actual: The value to compare against `not_expected`.
:param: message (optional): A message to include with the failure print statement.
:param: func_name (optional): The name of the function being tested.

Returns:
- None
"""   
@staticmethod
def ASSERT_NOT_EQUAL(not_expected: Any, actual: Any, message: str = "", func_name: str = "") -> None:
  print(f"\n__{ASSERT_NOT_EQUAL.__name__}::INVOKED__\n")
  if not_expected != actual:
      _print_pass(func_name = func_name)
  else:
      _print_fail(message = message, func_name = func_name)
      print("\n[expected]: {} -> [actual]: {}".format(not_expected, actual))
    
    
"""__summary__
:desc: This static method is used to assert that the given condition is True. 
       If the condition is True, then the test passes and the function _print_pass() is called. 
       If the condition is False, then the test fails and the function _print_fail() is called. 
       The message parameter is an optional string that can be used to provide more information 
       about why the test may have failed. The func_name parameter is an optional string that 
       can be used to specify the name of the function being tested.

:param condition: A boolean value representing the condition to 
:param message: An optional string that provides more information about why the test may have failed.
:param func_name: An optional string that specifies the name of the function being tested.
:return: None.
"""
@staticmethod
def ASSERT_TRUE(condition: Any, message: str = "", func_name: str = "") -> None:
  print(f"\n__{ASSERT_TRUE.__name__}::INVOKED__\n")
  if condition:
    _print_pass(func_name = func_name)
  else:
    _print_fail(message = message, func_name = func_name)
    
    
"""__summary__
:desc: Determines if the condition is False, prints a pass message with the function
       name if the condition is False, and prints a fail message with the message 
       and function name parameters if the condition is True.

:param condition: A boolean value that is being tested.
:param message: A string message that will be printed if the condition is True. Default is an empty string.
:param func_name: A string that will be printed as the function name in the pass and fail messages. Default is an empty string.

:return: None
"""
@staticmethod
def ASSERT_FALSE(condition: Any, message: str = "", func_name: str = "") -> None:
  print(f"\n__{ASSERT_FALSE.__name__}::INVOKED__\n")
  if not condition:
    _print_pass(func_name = func_name)
  else:
    _print_fail(message = message, func_name = func_name)

    
"""__summary__
:desc: Asserts that the expected item is present in the actual iterable.
       Prints a pass message if the assertion passes, 
       otherwise prints a fail message with an optional 
       custom message and function name. 

:param expected: The expected element to search for in actual.
:type expected: Any
:param actual: The iterable to search for the expected element.
:type actual: Iterable
:param message: An optional message to print if the assertion fails. Defaults to "".
:type message: str
:param func_name: An optional function name to print if the assertion fails. Defaults to "".
:type func_name: str
:return: None
"""
@staticmethod
def ASSERT_IN(expected: Any, actual: Any, message: str = "", func_name: str = "") -> None:
  print(f"\n__{ASSERT_IN.__name__}::INVOKED__\n")
  if expected in actual:
    _print_pass(func_name = func_name)
  else:
    _print_fail(message = message, func_name = func_name)
    
    
"""__summary__
:desc: Checks if a value is not in another value and prints a pass or fail message.

:param not_expected: A value that is not expected to be in another value.
:param actual: The value being checked.
:param message: A custom message to be printed on failure.
:param func_name: The name of the function being tested.
:return: None
"""
@staticmethod
def ASSERT_NOT_IN(not_expected : Any, actual: Any, message: str = "", func_name: str = ""):
  print(f"\n__{ASSERT_NOT_IN.__name__}::INVOKED__\n")
  if not_expected in actual:
    _print_pass(func_name = func_name)
  else:
    _print_fail(message = message, func_name = func_name)
    
    
"""__summary__
:desc: Executes a given statement and prints a pass message if no exception is thrown.
       Otherwise, prints a fail message along with the type of exception thrown or traceback.

:param statement: A lambda expression representing the statement to be executed.
:type statement: lambda

:param message: An optional message to print in case of failure.
:type message: str

:param func_name: An optional name of the function being tested.
:type func_name: str

:return: None
"""
@staticmethod
def ASSERT_NO_THROW(statement: callable, message: str = "", func_name: str= "") -> None:
  print(f"\n__{ASSERT_NO_THROW.__name__}::INVOKED__\n")
  try:
      statement()
      _print_pass(func_name = func_name)
  except Exception as ex:
      _print_fail(message = message, func_name = func_name)
      print("[unexpected exception type]:", type(ex).__name__)
  except:
      _print_fail(message = message, func_name = func_name)
      print("[unexpected exception occurred]:")
      traceback.print_exc()


"""__summary__
:desc: This is a static method that asserts that a given statement raises an exception. 
       If the statement does not raise an exception, the method prints a failure message; 
       otherwise, it prints a pass message. The method takes in three 

:param statement: A lambda expression representing the statement to be executed.
:type statement: lambda

:param message: An optional message to print in case of failure.
:type message: str

:param func_name: An optional name of the function being tested.
:type func_name: str

:return: None
"""
@staticmethod
def ASSERT_THROW(statement: callable, message: str = "", func_name: str = "") -> None:
  print(f"\n__{ASSERT_THROW.__name__}::INVOKED__\n")
  try:
      statement()
      _print_fail(message = message, func_name = func_name)
  except Exception as ex:
      _print_pass(func_name = func_name)
  except:
      _print_fail(message = message, func_name = func_name)
      print("[unexpected exception occurred]:")
      traceback.print_exc()
      
          
"""__summary__
:desc: A static method that checks if a given value is greater than a given threshold.
       If the value is greater, it will print a passed message using a predefined function.
       If the value is not greater, it will print a failed message with the provided message
       and the values of the parameters. s

:param value: A number to be checked against the threshold.
:type value: int or float
:param threshold: A number which the value will be compared against.
:type threshold: int or float
:param message: A message to be printed if the check fails. Default is an empty string.
:type message: str
:param func_name: The name of the function being tested. Default is an empty string.
:type func_name: str

:return: None
"""      
@staticmethod
def ASSERT_GREATER(value: Any, threshold: Any, message: str = "", func_name: str = "") -> None:
    print(f"\n__{ASSERT_GREATER.__name__}::INVOKED__\n")
    if value > threshold:
        _print_pass(func_name)
    else:
        _print_fail(message, func_name)
        print("[value]: {} -> [threshold]: {}".format(value, threshold))

    
"""__summary__
:desc: A static method that compares the given value with a threshold and prints a pass message 
       if the value is smaller than the threshold; otherwise, print a fail message along with 
       the given message and the value and threshold that caused the fail.

:param value: a numeric value to be compared with the threshold.
:type value: float or int.
:param threshold: a numeric threshold value.
:type threshold: float or int.
:param message: an optional string message to be printed with the fail message.
:type message: str.
:param func_name: an optional string to specify the name of the function being tested.
:type func_name: str.
:return: None
"""
def ASSERT_LESS(value: Any, threshold: Any, message: str = "", func_name: str = "") -> None:
    print(f"\n__{ASSERT_LESS.__name__}::INVOKED__\n")
    if value < threshold:
        _print_pass(func_name)
    else:
        _print_fail(message, func_name)
        print("[value]: {} -> [threshold]: {}".format(value, threshold))
