class TV:

    def __init__(self, channel=0, volumeLevel=0, on=False):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on

    def turnOn(self):
        self.on = True
        print("Is TV on: ", self.on)

    def turnOff(self):
        self.on = False
        print("Is TV on: ", self.on)

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        self.channel = channel if (channel <= 120 or channel >=0) else -1
        if self.volumeLevel == -1: return "max/min channel"
        print("Channel: ", self.volumeLevel)
        return self.channel

    def getVolume(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        self.volumeLevel = volumeLevel if (volumeLevel <= 120 or volumeLevel >=0) else -1
        if self.volumeLevel == -1: return "max/min volume"
        print("Volume: ", self.volumeLevel)
        return self.volumeLevel

    def channelUp(self):
        self.channel += 1
        print("Channel up: ", self.channel)

    def channelDown(self):
        self.channel -= 1
        print("Channel down: ", self.channel)

    def volumeUp(self):
        self.volumeLevel += 1
        print("Volume up: ", self.volumeLevel)

    def volumeDown(self):
        self.volumeLevel -= 1
        print("Volume down: ", self.volumeLevel)


