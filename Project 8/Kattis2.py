from math import atan,tan, degrees, radians
lista =[5,10,15,20,25,30,40,45]

for i in lista:
    Wheelbase = 2.760
    Wheeltrack = 1.627
    BackWhidht = 1.874
    """Calculate the other wheelsangle we use cot*theta - cot*phi = Backwidth /Wheelbase """
    Phi = degrees(atan(1 / ((BackWhidht / Wheelbase) + 1 / (tan(radians(i))))))
    Phi = (Phi + i)/2
    print(Phi)