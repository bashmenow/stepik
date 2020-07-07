import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def log(self, msg):
        print(msg)

    def append(self, object):
        super(LoggableList, self).append(object)
        self.log(object)


lst = LoggableList([1,2,3,4,5,67,])
lst.append(77)
print(lst)