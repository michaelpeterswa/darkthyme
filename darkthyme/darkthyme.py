# Cache class
# Michael Peters
from cacheitem import CacheItem


class DarkThyme:
    def __init__(self):
        self.__dict = {}

    def printContents(self):
        print("dict contents:")
        print(self.__dict)

    def set(self, key, value, duration):
        object = CacheItem(key, value, duration)
        self.__dict[key] = object

    def get(self, key):
        self.removeExpiredKeys()
        return self.__dict.get(key)

    def removeExpiredKeys(self):
        for key, val in list(self.__dict.items()):
            if val.isExpired():
                result = self.__dict.pop(key)
                print("Key Removed: %s" % key)
