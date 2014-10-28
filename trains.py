import urllib2
import json


class dbdata:
    def __init__(self):
        self.stationCodes = ['K04','N02']
        self.apiKey='kfgpmgvfgacx98de9q3xazww'
        self.grab()
        
    
    def grab(self):
       req= 'http://api.wmata.com/StationPrediction.svc/json/GetPrediction/'+ self.stationCodes[0] +',' + self.stationCodes[1] +'?api_key='+self.apiKey
       ret=urllib2.urlopen(req).read() 
       self.allTrains=json.loads(ret)['Trains']
       
    def get_trains(self):
        return self.allTrains
    
class train:
    
    
    def __init__(self,trainData):
        self.locationName=trainData['LocationName']
        self.dest=trainData['Destination']
        self.min=trainData['Min']
        
        colorDict={'OR':'Orange',
               'SV':'Silver'
               }
        if trainData['Line'] in ['OR','SV']:
            self.line=colorDict[trainData['Line']]
        
    def get_location(self):
        return self.locationName
    def get_dest(self):
        return self.dest
    def get_minutes(self):
        return self.min
    def get_line(self):
        return self.line
    
    
class station:
    def __init__(self,stationName,allData):
        self.name=stationName
        self.stationTrains=[]
        for item in allData:
            if item['LocationName']==stationName:
                self.stationTrains.append( train(item) )
                
                
    def get_trains(self):
        return self.stationTrains
    
    def get_name(self):
        return self.name
    