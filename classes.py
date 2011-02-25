#Filename: classes.py
#Author: Lee ying
#Centre No/Index No: 3024/
# Description: Support classes for music library
''' Super class Resource '''
class Resource:
    '''Constructor'''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired 
        self.__ResourceType = ResourceType
    ''' Resource number accessor '''
    def getResourceNo(self):
        return self.__ResourceNo
    
    ''' Title accessor '''
    def getTitle(self):
        return self.__Title
    
    ''' Date Acquired accessor '''
    def getDateAcquired(self):
        return self.__DateAcquired
    
    ''' Resource type accessor '''
    def getResourceType(self):
        return self.__ResourceType

    ''' Title modifier'''
    def setTitle(self,newTitle):
        self.__Title = newTitle
        
    ''' Date Acquired modifier'''
    def setDateAcquired(self,newDateAcquired):
        self.__DateAcquired = newDateAcquired
        
    ''' Resource type modifier'''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType
    '''Display helper function'''
    def display(self):
        return "{0:6}{1:35s}{2:7s}{3}".format(self.getResourceNo(), self.getTitle() , self.getDateAcquired() , self.getResourceType())


''' Subclass MusicCD '''
class MusicCD(Resource):
    ''' Constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks
    ''' Artist accessor '''
    def getArtist(self):
        return self.__Artist
    
    ''' Number of tracks accessor '''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    ''' Artist modifier'''
    def setArtist(self, newArtist):
        self.__Artist = newArtist
        
    ''' Number of tracks modifier'''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks
        
    ''' Display helper function'''
    def display(self):
        return "{0}{1:50}{2}".format(super().display(),self.getArtist(),self.getNoOfTracks())
               
''' Subclass FilmDVD '''
class FilmDVD(Resource):
    ''' Constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime
    ''' Artist accessor '''
    def getDirector(self):
        return self.__Director
    
    ''' Number of tracks accessor '''
    def getRunningTime(self):
        return self.__RunningTime

    ''' Director modifier'''
    def setDirector(self, newDirector):
        self.__Director = newDirector
        
    ''' Running Time modifier'''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime
        
    ''' Display helper function'''
    def display(self):
        return "{0}{1:50}{2}".format(super().display(),self.getDirector(),self.getRunningTime())

#main
##    r1 = Resource("00001", "Best Of Esther" , "030309" , "C")
##    print(r1.getResourceNo())
##
##    r1.setTitle("Shinee 2011")
##    print(r1.getTitle())
##
##    print(r1.display())
##
##    r2 = Resource("00002", "","","")
##    r2.setTitle("SUPERMAN COLLECTION")
##    r2.setDateAcquired("050510")
##    r2.setResourceType("C")
##    
##    print(r2.getTitle())
##    print(r2.display())

##cd1 = MusicCD("00003" , "FT COUNTRY", "070708" , "C" , "FTTTTTTT", 10)
##print(cd1.getResourceNo())# inherited method
##print(cd1.getArtist())#class method
##print(cd1.getNoOfTracks())
##print(cd1.display()) #overriding
##
##dvd1 = FilmDVD("00004","NEW TEMPLE","020211", "D" , "Mr HAHA" , 120)
##print(dvd1.display())
##
##resource_list = []
##resource_list.append(cd1)
##resource_list.append(dvd1)
##
##print(resource_list)
##for item in resource_list:
##    print(item.display()) #polymorphism
