from TV import TV

# test class for TV class
def main():
    
    # initialize tv object
    tv = TV(20, 2, True)
    tv.turnOn()
    tv.turnOff()
    tv.turnOn()
    
    # get and set channel
    print(tv.getChannel())
    tv.setChannel(3)
    
    # get and set volume
    print(tv.getVolume())
    tv.setVolume(5)
    print(tv.getVolume())
    
    # channel adjustment
    tv.channelUp()
    tv.channelDown()
    
    # volume adjustment
    tv.volumeUp()
    tv.volumeDown()
    
if __name__ == "__main__":
    main()