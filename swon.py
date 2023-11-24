import random
import time
def locate(n,c):
     yy=n//80
     xx=n-(yy*80)
     print(f"\x1b[{yy};{xx}d\x1b[{c};30m ")    


print("\x1b[40;30m\x1bc")


if 0==0:
    l=list(range(80*25))
    for m in range(80*25-1):
        n=int(l.pop(random.randint(1,len(l)-1)))
        locate(n,43)
        time.sleep(0.1)
        