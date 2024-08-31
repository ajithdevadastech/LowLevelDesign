class Movie:
    #constructor
    def __init__(self, title, year, genre):
        self.__title = title
        self.__year = year
        self.__genre = genre

    #get setters

    def settitle (self, title):
        self.__title = title

    def gettitle(self):
        return self.__title

    def setyear(self, year):
        self.__year = year

    def getyear(self):
        return self.__year

    def setgenre(self, genre):
        self.__genre = genre

    def getgenre(self):
        return self.__genre

    def printdetails(self):
        print(self.gettitle())
        print('---------------------')
        print(self.getyear())
        print('---------------------')
        print(self.getgenre())
        print('---------------------')

ob = Movie('kireedam', 1991, 'Thriller')
print(ob.printdetails())

ob.settitle('kauravar')
print(ob.printdetails())

