class TV:
    
    # initializes instance variables
    def __init__(self, channel=0, volumeLevel=0, on=False):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on
    
    # turn on the tv
    def turnOn(self):
        self.on = True
        print("Is TV on: ", self.on)
        
    # turn off the tv
    def turnOff(self):
        self.on = False
        print("Is TV on: ", self.on)
    
    # get the channel of the tv
    def getChannel(self):
        return self.channel
    
    # set the channel of the tv
    def setChannel(self, channel):
        self.channel = channel if (channel <= 120 or channel >=0) else -1
        if self.volumeLevel == -1: return "max/min channel"
        print("Channel: ", self.volumeLevel)
        return self.channel
    
    # get the volume
    def getVolume(self):
        return self.volumeLevel
    
    # set the volume
    def setVolume(self, volumeLevel):
        self.volumeLevel = volumeLevel if (volumeLevel <= 120 or volumeLevel >=0) else -1
        if self.volumeLevel == -1: return "max/min volume"
        print("Volume: ", self.volumeLevel)
        return self.volumeLevel
    
    # increase channel by one
    def channelUp(self):
        self.channel += 1
        print("Channel up: ", self.channel)
        
    # decrease channel by one
    def channelDown(self):
        self.channel -= 1
        print("Channel down: ", self.channel)

    # increase volume by one
    def volumeUp(self):
        self.volumeLevel += 1
        print("Volume up: ", self.volumeLevel)

    # decrease volume by one
    def volumeDown(self):
        self.volumeLevel -= 1
        print("Volume down: ", self.volumeLevel)


