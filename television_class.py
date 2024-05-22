#create a constructor for channel, volume level and on
class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False
#create a method for both turn on and off
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

#crete a method for getting channel
    def get_channel(self):
        return self.channel

#create a method for setting channel and limit it to 1-120
    def set_channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

#create a method for getting volume
    def get_volume(self):
        return self.volume_level

#create a method for setting volume and limit it 1-7
    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level

#create a method for increasing the channel
    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1
#create a method for decreasing the channel
    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1
#cheate a method for increasing volume
    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1
#create a method for decreasing volume
    def volume_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1