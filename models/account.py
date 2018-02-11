import requests
from models.gathering import Gather

class Account(Gather):
    def getAccountInfo(self):
        pass



if __name__ == '__main__':
    obj = Account()
    print(obj.getAccountInfo())