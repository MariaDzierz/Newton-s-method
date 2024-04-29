#python code
import time
import math

def newton(x0, f, fprim, eps, imax):
    i = 0
    while abs(f(x0)) > eps: #wartość bezwględna z funkcji w x0 musi być większa od tolernacji,
#bo gdy będzie bliska 0 to będzie przerwana pętla, nasze miejsce zerowe
        if abs(fprim(x0)) < eps: #jeśli będzie bliska 0 to algorytm nam się nie zbiegnie
            print('Wartość pochodnej bliska 0.') 
            return None #brak właściwego rozwiązania
        else:
            xi = x0 - f(x0)/fprim(x0)
            x0 = xi
            i += 1
        if i > imax:
            print('Za duża liczba iteracji.')
            return None #brak właściwego rozwiązania
    return x0


def fs(x):
    return x**2-2**x

def fsprim(x):
    return 2*x-2**x*math.log2(2)

time_start = time.perf_counter()
n = newton(-10, fs, fsprim, 1e-10, 100)
time_end = time.perf_counter() - time_start
if n != None:
    print(n, fs(n), f'czas wykonania:{time_end}')
else:
    print(n, 'Nie udało się znaleźć miejsca zerowego.')
