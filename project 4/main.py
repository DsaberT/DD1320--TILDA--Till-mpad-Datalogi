from bfs import *
from linkedQfile import *
from bintreeFile import *
"""svenska = sve()
makeChildren("söt", svenska)"""

startord = str(input("Välj startord: "))
slutord = str(input("Välj slutord: "))

gamla = Bintree()
q = LinkedQ()
papanod = ParentNode(startord)
q.enqueue(papanod)
svenska = sve()

while not q.isEmpty():
    nod = q.dequeue()
    makeChildren(nod, svenska, q, gamla)
    if nod.word == slutord:
        print("En väg finns till", slutord)
        nod.writechain(nod)
        break
    else:
        pass
if nod.word != slutord:
    print("En väg finns inte", slutord)
else:
    pass



