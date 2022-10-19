from songclass import *
from sokfunk import *
import timeit

n = 500000
list = Song.text()
list = list[0:n]
sista = list[499999]
testartist = sista.artistnamn
linjtid = timeit.timeit(stmt=lambda: linsok(list, testartist), number=1000)
print("Linjärsökningen tog", round(linjtid, 4), "sekunder")
