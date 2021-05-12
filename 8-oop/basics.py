class Singleton(object):
    __shared = None

    def __init__(self):
        if Singleton.__shared:
            raise Exception("Already instantiated")
        Singleton.__shared = self

    @classmethod
    def getInstance(cls):
        return Singleton.__shared or Singleton()

# Factory method in terms of dictionary 

_CARD_METHODS = {
        int: lambda : defaultdict(int)
        bool: lambda : defaultdict(bool)
        }

def createDS(dsType):
    return _CARD_METHODS[dsType]()
