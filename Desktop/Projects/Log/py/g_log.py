"""__[g_log] Logging Library__
@author:
    Jakob Balkovec

@date:
    July 7, 2023

@version:
    1.0

@license:
    Copyright (c) 2023 Jakob Balkovec

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

@file:
    g_log.py

@description:
    This script contains a logging library implemented through the `g_log` class.
    It provides functionality for logging messages with different severity levels.
    The script also includes a filter function for filtering log entries based on log levels.
    
@usage:
    Run this script with the necessary dependencies installed and provide
    the program will output the log files with the provided data
    
@example:
    $ python g_log.py
"""

"""__imports__"""
import traceback
import sys
import os
from datetime import datetime
from typing import Callable, TypeVar, Optional, List
import time
import inspect
from threading import Lock
from py.license import _LICENSE

"""__remove_all_logging_files__
find {/path/to/wd} -type f -name "*.log" -exec rm {} +
"""

"""__severity_levels__
Levels increase with severity in the following manner:
"""
_LEVEL = {
  0: "DEBUG", #debug
  1: "INFO", #informal
  2: "WARNING", #warning-non-important
  3: "ERROR", #severe-important
  4: "CRITICAL" #critical
}

"""__T__
Define a generic type ==> (typename = T)
"""
T = TypeVar('T')

"""__flags__
_exc_info: bool -> Provides more detailed information about the exception
_traceback: bool -> Provides more detailed information about the traceback
_accurate: bool -> Provides a more detailed date/time format of the log entry

        - _acurate: bool = True
        {yyyy-mm-dd hh:mm:ss}
        
        - _acurate: bool = False
        {hh:mm:ss}
"""
_exc_info: bool = True
_traceback: bool = True
_accurate: bool = False

"""__constants__
_MAX_FILES: int -> The maximum number of log files to keep
_MAX_SIZEOF: int -> The maximum size of a log file in bytes
"""
_MAX_FILES: int = 10
_MAX_SIZEOF: int = 1024

"""_summary_
Defines the g_log class which is used to store log entries

:usage: logger = g_log()
"""
class g_log:
    
    """__private_variables__
    filename: str -> The name of the log file
    
    max_file_count: int -> fully customizable to fit your needs through 
                           the predefined constant _MAX_FILES
                            
    max_file_size: int -> fully customizable to fit your needs through 
                          the predefined constant _MAX_SIZEOF
    """
    filename: str
    max_file_count: int = _MAX_FILES 
    max_file_size: int = _MAX_SIZEOF
    
    """
    COnstructor, initializes a new instance of the `g_log` class.
    
    It sets up the initial state of the object by:
    
    - Determining the base filename using os.path.splitext(os.path.basename(__file__))[0]
    - Generating a unique filename for the log file using the get_unique_filename() method.
    - Initializing an empty list for filters.
    - Creating a Lock() object for thread safety.
    """
    def __init__(self):
        base_filename = os.path.splitext(os.path.basename(__file__))[0]
        self.filename = self.get_unique_filename(base_filename, ".log")
        self.filters = []
        self.lock = Lock() 

    """__summary__
    :desc: This function prints the license information stored in the `_LICENSE` variable.
    
    :param: self: The instance of the class.

    :return: None
    """
    def print_license(self) -> None:
        license_text = f"\n{_LICENSE}\n"
        print(license_text, end="")
        return None
    
    """__summary__
    :desc: Generate a unique filename with the given base filename and extension.

    :param: base_filename (str): The base filename.
    :param: extension (str): The file extension.

    :return: str: The unique filename.
    """
    def get_unique_filename(self, base_filename: str, extension: str) -> str:
        file_name = f"{base_filename}_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}{extension}"
        return file_name
    
    """_summary__
    :desc: Get the line number of the given function within the file it is defined.

    :param: func (Callable[..., T]): The function to get the line number of.

    :return int: The line number of the function within the file it is defined, or None if the line number cannot be determined.
    """
    def get_line_number(self, func: Callable[..., T]) -> Optional[int]:
        return inspect.findsource(func)[1] - 1 if inspect.isfunction(func) else None
    
    """__summary__
    :desc: Adds a filter function to the list of filters.
    
    :param: filter_func (Callable[[str], bool]): The filter function to be added.

    :return: None: This function does not return anything.
    """
    def add_filter(self, filter_func: Callable[[str], bool]) -> None:
        self.filters.append(filter_func)
        return None

    """__summary__
    :desc: Determines if a log entry should be logged based on the filters.

    :param: log_entry (str): The log entry to evaluate.

    :return: bool: True if the log entry should be logged, False otherwise.
    """
    def should_log(self, log_entry: str) -> bool:
        return all(filter_func(log_entry) for filter_func in self.filters)
    
    """__summary__
    :desc: Logs a message with a given condition, message, level, and optional function.

    :param: condition (Optional[str]): The condition for the log message. Defaults to None.
    :param: message (str): The log message.
    :param: level (int): The log level.
    :param: func (Optional[Callable[..., T]]): The optional function to be logged. Defaults to None.

    :return: str: The log entry.

    :raise: ValueError: If the log level is invalid.
    """    
    def log(self, condition: Optional[str], message: str, level: int, func: Optional[Callable[..., T]] = None) -> str:
        self.lock.acquire() 
        if level not in _LEVEL:
            raise ValueError("[invalid log level]")
        
        level_str = _LEVEL[level]
        
        condition_str = condition if condition is not None else "[No Condition]"
        func_str = func.__name__ if func is not None else "[No Function]"
        log_entry = f"[{self.get_timestamp()}]::[{level_str}] {condition_str} {func_str}(): {message}"

        if func is not None:
            if _exc_info:
                try:
                    """_summary_
                    If the Callable object throws an error it will be 
                    handled with _exc_info and _traceback if set to "True"
                    """
                    if not self.should_log(log_entry):
                        return ""
                    else:
                        log_entry += f"\n[func definition] >>> {func.__name__}() line: {self.get_line_number(func)}"
                        start_time = time.time(); func(); end_time = time.time()
                        execution_time = end_time - start_time
                        log_entry += f"\n[execution time] >>> {round(execution_time)} seconds for {func.__name__}"
                    
                except Exception as error:
                    exception_type, exception_value, exception_traceback = sys.exc_info()
                    
                    exception_str = f"{exception_type.__name__}: {exception_value}"
                    stack_trace = traceback.format_tb(exception_traceback)
                    stack_trace_str = "\n".join(stack_trace)

                    log_entry += f"\n\n*** ERROR ***\n{exception_str}\n{stack_trace_str}"
                    
                    """
                    exception_type, exception_value, exception_traceback = sys.exc_info()
                    log_entry += f"\n[exc info]: {exception_type.__name__}: {exception_value}"
                    """
                    if _traceback:
                        trace = traceback.format_tb(exception_traceback)
                        log_entry += f"\n[traceback]: \n" + "\n".join(trace)
                finally:
                    self.lock.release()
        else:
            pass
        
        self.write_to_file(log_entry)
        return log_entry

    """__summary__
    :desc: Get the current timestamp.

    :param: self: The instance of the class.
    
    :return: str: The current timestamp in the format '%H:%M:%S' if `_accurate` is False,
                  otherwise in the format '%Y-%m-%d %H:%M:%S'.
    """
    def get_timestamp(self) -> str:
        return datetime.now().strftime('%H:%M:%S') if not _accurate else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    """__summary__
    Writes the given log entry to a file.
    
    :param: log_entry (str): The log entry to be written to the file.
    
    :return: None
    """
    def write_to_file(self, log_entry: str) -> None:
        self.lock.acquire() 
        try:
            if os.path.isfile(self.filename) and os.path.getsize(self.filename) >= self.max_file_size:
                self.rotate_files()

            with open(self.filename, 'a') as file:
                file.write(log_entry + '\n')
        finally:
            self.lock.release()
        return None

    """__summary__
    :desc: Rotate files by renaming the current file, creating a backup with a timestamp,
    and deleting excess backups if the maximum file count is reached.

    :param: None

    :return: None
    """
    def rotate_files(self) -> None:
        try:
            timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

            backup_filename = f"{self.filename}_{timestamp}.log"
            os.rename(self.filename, backup_filename)

            existing_backups = sorted(
                [filename for filename in os.listdir() if filename.startswith(self.filename)],
                reverse=True)
            
            if len(existing_backups) >= self.max_file_count:
                for i in range(self.max_file_count, len(existing_backups)):
                    os.remove(existing_backups[i])
        finally:
            self.lock.release()
        return None

"""__summary__
:desc: Filter the log entry by log level.

:param: log_entry (str): The log entry to filter.
:param: levels (List[str]): The list of log levels to filter by.

:return: bool: True if the log entry's log level is in the provided list of levels, False otherwise.
"""
@staticmethod
def filter_by_log_level(log_entry: str, levels: List[str]) -> bool:
    log_level = log_entry.split('::', 1)[1].split(']', 1)[0].strip()
    return log_level in levels

"""_summary_
TESTING THE G_LOG
"""
def raise_error() -> None:
    raise ValueError("This is an error raised in TEST")

def main() -> None:
    logger = g_log()
    logger.print_license()
    log_filter = lambda log_entry: filter_by_log_level(log_entry, ['INFO', 'DEBUG', 'WARNING'])
    log_entries = [
        (None, "message", 0, raise_error),
        (None, "message", 1, raise_error),
        (None, "message", 3, raise_error)
    ]
    logged_entries = [entry for entry in log_entries if log_filter(entry)]
    for entry in logged_entries:
        logger.log(*entry)
    
if __name__ == "__main__":
    main()