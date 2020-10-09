import time
import math
def CPM(start_timestamp:int,n:int):
    seconds = abs(int(time.time()) - int(start_timestamp))
    cpm = 0
    # Dividing by 0 raises an error
    try:
        cpm = n / seconds * 60
    except:
        pass
    return cpm


def run_test(n,delay):
    """n : int
        delay : float , In seconds"""
    start = time.time()
    for x in range(n):
        current_cpm = CPM(start,x)
        time.sleep(delay)
        print(int(current_cpm))

def quick_test(n,seconds):
    start = time.time() - seconds
    current_cpm = CPM(start,n)
    print(int(current_cpm))


# If the delay is 1 second then CPM should reutrn 60, a 2 second delay would return 30 and so on.
# The accuracy will increase over time
# run_test(100,0.500)

# Checked 60 combos in 60 seconds would return 60 cpm and so on
# quick_test(60,60)
