#create a constructor for channel, volume level and on
class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
#create a method for both turn on and off
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

#crete a method for getting channel
#create a method for setting channel and limit it to 1-120
#create a method for getting volume
#create a method for setting volume and limit it 1-7
#create a method for increasing the channel
#create a method for decreasing the channel
#cheate a method for increasing volume
#create a method for decreasing volume
