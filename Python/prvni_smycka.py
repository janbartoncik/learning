from asyncio import FastChildWatcher
from ctypes.wintypes import HFONT, HHOOK
from email.errors import FirstHeaderLineIsContinuationDefect


n = 5000
while n > 0 :
    print(n)
    n = n - 10
print("BOOOM!!!")