import time

def temporizado(n):
    timpo1=time.time()
    while n < 100:
        print('Holas')
        time.sleep(10)
        n -= 1
