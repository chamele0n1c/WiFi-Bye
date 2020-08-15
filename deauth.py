import os, sys
from subprocess import Popen

def main():
        global numberOfCards
        print("Please Enter how many cards you will use 4max")
        cards = []
	config = []
	bssidSwitch = []
	chnnlSwitch = []

        try:

                numberOfCards = input("Number of cards(4max): ")

                if numberOfCards < 1 or numberOfCards > 4:

                        print("Too many or not enough cards...")
                        sys.exit(1)

                for x in range(numberOfCards):

                        x = x + 1
                        cards.append(raw_input("Enter Interface %d : " % x))
			os.system("clear")

        except TypeError:
                sys.exit(1)

        for i in cards:
                print "Monitor Iface read: %s" % i

        answer = bool(raw_input("Correct Wlans?(True, False) --> "))

        if not answer:

                #user terminate
                print "Incorrect Wlan Exiting"
                sys.exit(1)

        else:
                print "Wlan's Confirmed"
                os.system("sleep 3")
                os.system("clear")
		os.system("airmon-ng check kill")

	os.system("clear")

	for i in cards:

		os.system("clear")

		print "INTERFACE: %s" % i
		print "MAX AP TARGETS: 3
		swcmod = input("Enter the number of AP's BSSID's to switch on this card(1-3): ")

		if swcmod > 3 or swcmod < 1:

			os.system("clear")
			print "Failed AP switch index either 1 2 or 3"
			sys.exit(1)

		config.append(swcmod)

		for i in range(swcmod):

			bssidSwitch.append(raw_input("Enter BSSID #%d -)> " % (i+1)))
			chnnlSwitch.append(input("Enter Channel #%d -)> " % (i+1)))

        for i in config:

		if i == "1":
			Popen(['xterm', '-e', 'python commKill single %s %d %s' % (bssidSwitch[0], chnnlSwitch[0], cards[0])])
			bssidSwitch.pop(0)
			chnnlSwitch.pop(0)
			config.pop(0)
			cards.pop(0)

		if i == 2:
			Popen(['xterm', '-e', 'python commKill 2 %s %d %s %d %s' % (bssidSwitch[0], chnnlSwitch[0], bssidSwitch[1], chnnlSwitch[1], cards[0])])
			bssidSwitch.pop(0)
			chnnlSwitch.pop(0)
			bssidSwitch.pop(0)
			chnnlSwitch.pop(0)
			cards.pop(0)

		if i == 3:
			Popen(['xterm', '-e', 'python commKill 3 %s %d %s %d %s %d %s' % (bssidSwitch[0], chnnlSwitch[0], bssidSwitch[1], chnnlSwitch[1], bssidSwitch[2], chnnlSwitch[2],  cards[0])])
			bssidSwitch.pop(0)
                        chnnlSwitch.pop(0)
                        bssidSwitch.pop(0)
                        chnnlSwitch.pop(0)
			bssidSwitch.pop(0)
                        chnnlSwitch.pop(0)
			cards.pop(0)

if __name__ == "__main__":
        main()
