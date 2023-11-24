import numpy as np
import time
import os

A,B = 0,0
pi = 3.14
z = [0] * 1760
b = [' '] * 1760

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')


def donut():
    for j in range(int(6.28 * 100)):
        for i in range(int(6.28 * 100)):
            c = np.sin(i / 100.0)
            d = np.cos(j / 100.0)
            e = np.sin(A)
            f = np.sin(j / 100.0)
            g = np.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = np.cos(i / 100.0)
            m = np.cos(B)
            n = np.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

            if 22 > y > 0 and 0 < x < 80 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

def initialize():
    for i in range(1760):
        b[i] = ' '
        z[i] = 0


while(True):

    clear_terminal()
    initialize()
    donut()

    for k in range(0,1760):
        print(b[k], end = '\n' if k % 80 == 79 else '')

    A += 0.00004
    B += 0.00002

    #time.sleep(.03)    