import sys
import os
from pprint import pprint

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
pprint(sys.path)


from pack_1.file_11 import a

print(a)

def func_2(n: int) -> int:
    return n + n


print(func_2(a))
