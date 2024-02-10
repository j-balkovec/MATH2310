/**
 * Print the test as passed.
 *
 * @param {string} funcName - the name of the function being tested
 * @return {undefined} no return value
 */
function _printPass(funcName = "") {
  console.log(`%c[TEST ${funcName} PASSED]`, "color: green");
}

/**
 * Prints a fail message with an optional custom message and function name.
 *
 * @param {string} message - The custom message to be displayed.
 * @param {string} funcName - The name of the function that failed.
 */
function _printFail(message = "", funcName = "") {
  console.log(`%c[TEST ${funcName} FAILED]`, "color: red");
  if (message !== "") {
    console.error(message);
  }
}

/**
 * Invoke the specified function and log the current time.
 *
 * @param {string} funcName - The name of the function to invoke.
 */
function _invoke(funcName) {
  const currentTime = new Date().toLocaleTimeString();
  console.log(`%c[TIME: ${currentTime}] __${funcName}::INVOKED__`, "color: yellow");
}

/**
 * Asserts a condition and prints a pass or fail message.
 *
 * @param {boolean} condition - The condition to be evaluated.
 * @param {string} [message=""] - The fail message to be printed.
 * @param {string} [funcName=""] - The name of the function being tested.
 * @return {undefined} No return value.
 */
function ASSERT(condition, message = "", funcName = "") {
  _invoke("ASSERT");
  if (condition) {
    _printPass(funcName);
  } else {
    _printFail(message, funcName);
  }
}

/**
 * Check if the expected value is equal to the actual value.
 *
 * @param {type} expected - the expected value
 * @param {type} actual - the actual value
 * @param {string} message - an optional message to display if the values are not equal
 * @param {string} funcName - an optional name of the function being tested
 */
function ASSERT_EQUAL(expected, actual, message = "", funcName = "") {
  _invoke("ASSERT");
  if (expected === actual) {
    _printPass(funcName);
  } else {
    _printFail(message, funcName);
    console.log(`\n[expected]: ${expected} -> [actual]: ${actual}`);
  }
}

/**
 * Logs an assertion message if the expected value is not equal to the actual value.
 *
 * @param {type} notExpected - the value that is not expected
 * @param {type} actual - the actual value
 * @param {string} [message=""] - an optional message to display if the assertion fails
 * @param {string} [funcName=""] - an optional function name to include in the assertion message
 */
function ASSERT_NOT_EQUAL(notExpected, actual, message = "", funcName = "") {
  _invoke("ASSERT");
  if (notExpected !== actual) {
    _printPass(funcName);
  } else {
    _printFail(message, funcName);
    console.log(`\n[expected]: ${notExpected} -> [actual]: ${actual}`);
  }
}

/**
 * Asserts that a given condition is true. If the condition is true, the function
 * prints a pass message. Otherwise, it prints a fail message with an optional
 * custom message and the name of the function.
 *
 * @param {boolean} condition - The condition to be checked.
 * @param {string} [message=""] - An optional custom message to be displayed
 *     when the condition is false.
 * @param {string} [funcName=""] - An optional name of the function to be
 *     displayed when the condition is false.
 */
function ASSERT_TRUE(condition, message = "", funcName = "") {
  _invoke("ASSERT");
  if (condition) {
    _printPass(funcName);
  } else {
    _printFail(message, funcName);
  }
}

/**
 * Asserts that a given condition is false. If the condition is false,
 * the function prints a pass message. If the condition is true, the
 * function prints a fail message along with an optional custom message.
 *
 * @param {boolean} condition - The condition to be evaluated.
 * @param {string} [message=""] - An optional custom message to be displayed
 *     if the condition is true.
 * @param {string} [funcName=""] - An optional name of the function where
 *     the assertion is made.
 * @return {undefined} This function does not return anything.
 */
function ASSERT_FALSE(condition, message = "", funcName = "") {
  _invoke("ASSERT");
  if (!condition) {
    _printPass(funcName);
  } else {
    _printFail(message, funcName);
  }
}
/**
 * Assertion function to check if the expected value is included in the actual value.
 *
 * @param {any} expected - The value that is expected to be included.
 * @param {any} actual - The value to be checked.
 * @param {string} message - Optional message to be displayed on failure.
 * @param {string} funcName - Optional name of the function being tested.
 */
function ASSERT_IN(expected, actual, message = "", funcName = "") {
  _invoke("ASSERT");
  if (actual.includes(expected)) {
    _printPass(funcName);
  } else {
    _printFail(message, funcName);
  }
}

/**
 * Asserts that the given value is not in the actual value.
 *
 * @param {any} notExpected - The value that is not expected to be in the actual value.
 * @param {any[]} actual - The actual value to check.
 * @param {string} [message=""] - An optional message to display if the assertion fails.
 * @param {string} [funcName=""] - An optional name of the function being tested.
 */
function ASSERT_NOT_IN(notExpected, actual, message = "", funcName = "") {
  _invoke("ASSERT");
  if (!actual.includes(notExpected)) {
    _printPass(funcName);
  } else {
    _printFail(message, funcName);
  }
}

/**
 * Asserts that a specific exception is thrown when executing a statement.
 *
 * @param {function} statement - The statement to be executed.
 * @param {function} expectedException - The expected exception type.
 * @param {string} message - An optional message to display on failure.
 * @param {string} funcName - An optional name of the function being tested.
 */
function ASSERT_THROW(statement, expectedException, message = "", funcName = "") {
  _invoke("ASSERT");
  try {
    statement();
    _printFail(message, funcName);
    console.log(`[expected exception]: ${expectedException}`);
  } catch (ex) {
    if (ex instanceof expectedException) {
      _printPass(funcName);
    } else {
      _printFail(message, funcName);
      console.log(`[unexpected exception type]: ${ex.constructor.name}`);
      console.trace();
    }
  }
}

/**
 * Executes a statement and checks if it throws an exception. If no exception is thrown, the test is considered passed.
 *
 * @param {function} statement - The statement to execute.
 * @param {string} [message=""] - An optional message to display if the test fails.
 * @param {string} [funcName=""] - An optional name of the function being tested.
 */
function ASSERT_NO_THROW(statement, message = "", funcName = "") {
  _invoke("ASSERT");
  try {
    statement();
    __printPass(funcName);
  } catch (ex) {
    __printFail(message, funcName);
    console.log("[unexpected exception type]:", ex.constructor.name);
    console.trace();
  }
}

function main() {
  ASSERT(true); //pass
  ASSERT(false); //fail
}

main();
