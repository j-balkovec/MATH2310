from __init__ import *
import time
import os

_PRINT = print("\n\n")
def test_assert() -> None:
    ASSERT(True)  # pass
    ASSERT(False, "")  # fail
    return None

def main() -> int:
    test_assert()
    print()
    return 0
  

  
if __name__ == "__main__":
    file_name = os.path.basename(__file__)
    print(f"[running {main.__name__}, in {file_name}]\n\n")
    time.sleep(2)
    main()