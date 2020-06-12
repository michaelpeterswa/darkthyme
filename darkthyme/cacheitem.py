import datetime

TEN_THOUSAND = 10000


class CacheItem(object):
    def __init__(self, key, obj, dur=TEN_THOUSAND):
        self.key = key
        self.obj = obj
        self.dur = dur  # in seconds
        self.time = datetime.datetime.now()

    def __setKey__(self, val):
        self.key = val

    def __getKey__(self):
        return self.key

    def __setObject__(self, val):
        self.obj = val

    def getObject(self):
        return self.obj

    def __getObjectStr__(self):
        return str(self.obj)

    def __setDuration__(self, val):
        self.dur = val

    def __getDuration__(self):
        return self.dur

    def __getTime__(self):
        return self.time

    def isExpired(self):
        duration = datetime.timedelta(seconds=self.dur)
        expiry = self.time + duration

        if expiry < datetime.datetime.now():
            return True
        else:
            return False

    # def printItem(self):

    #     print("------------------------")
    #     print("Key: %s" % self.__getKey__())
    #     print("Object: " + self.__getObjectStr__())
    #     print("Duration: %s" % self.__getDuration__())
    #     print("TimeCreated: %s" % self.__getTime__())
    #     print("------------------------")
