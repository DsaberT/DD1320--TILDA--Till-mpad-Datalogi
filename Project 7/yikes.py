class DictHash():
    def __init__(self):
        self.dictionary = {}
    def Store(self, nyckel, data):
        self.dictionary[nyckel] = data
    def Search(self, nyckel):
        if nyckel in self.dictionary:
            return self.dictionary[nyckel]
    def __getitem__(self, nyckel):
        return self.Search(nyckel)
    def __contains__(self, nyckel):
        if  nyckel in self.dictionary:
            return True
        else:
            return False

class Node:
   def __init__(self, key = "", data = None):
      self.key = key
      self.data = data

class Hashtable:

   def __init__(self, size):
       self.size = size*2
       self.hashlist = [None]*self.size

   def store(self, nyckel, data):
       Hindex = self.hashfunction(nyckel)
       while self.hashlist[Hindex] != None:
            Hindex = self.hashfix(Hindex)
       self.hashlist[Hindex] = Node(nyckel, data)


   def search(self, nyckel):
       Hindex = self.hashfunction(nyckel)
       while self.hashlist[Hindex] != None:
           if self.hashlist[Hindex].key == nyckel:
               return self.hashlist[Hindex].data
           else:
               Hindex = self.hashfix(Hindex)
       raise KeyError

   def hashfunction(self, nyckel):
      nummer = 0
      for bokstav in nyckel:
          nummer = (nummer*32 + ord(bokstav))

      return nummer%self.size

   def hashfix(self, index):
       return (index + 1)%self.size