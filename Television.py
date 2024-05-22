from television_class import TV

#create objects required for the television class
def main():
    # create a code for the required result for tv1

    tv1 = TV()
    tv1.turn_on()
    tv1.set_volume(3)
    tv1.set_channel(30)
#print the result for tv1
    print(f"tv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
#create a code for tge required result for tv2
#print the result for tv2

main()