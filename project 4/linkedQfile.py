class Node:
    def __init__(self, value, nextobject=None):
        self.value = value
        self.nextobject = nextobject

class LinkedQ:
    def __init__(self):                                 #Initierar en länkad lista med toma pekare
        self._first = None
        self._last = None

    def Queue(self):                                    # Sätter listans pekare till första och sista noden
        self._first = None
        self._last = None

    def enqueue(self, x):                               # kollar om leken är tom för då blir det första kortet som läggs till
        nynode = Node(x)                                # i leken kommer då vara både fösta och sista,
        if self._first == None:                         # Därefter placeras alla nya kort längsbak en efter en.
            self._first = nynode
            self._last = nynode
        else:
            self._last.nextobject = nynode              #ser till att objektet efter får ett värde så inte listan stannar efter första
            self._last = nynode

    def dequeue(self):
        topstack = self._first.value                  # Tar ut värdet på översta kortet
        self._first = self._first.nextobject          # Sätter att nästa kort är det översta
        return topstack                               # skickar tillbaks värdet på översta kortet innan switchen

    def isEmpty(self):
        if self._first == None:                          # kollar om det finns något kort överst eller inte.
            return True
        else:
            return False



