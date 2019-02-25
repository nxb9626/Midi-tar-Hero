# -------------------------------------------------------------------------------
# Name:        Wii Remote - connect to Bluetooth cwiid
# Purpose:
#
# Author:      Brian Hensley
#
# Created:     21/07/2012
# Copyright:   (c) Brian 2012
# -------------------------------------------------------------------------------
# !/usr/bin/env python

import time
import cwiid
import rtmidi

def main():
    print 'Press button 1 + 2 on your Wii Remote...'
    time.sleep(1)

    wm = cwiid.Wiimote()
    print 'Wii Remote connected...'
    print '\nPress the PLUS button to disconnect the Wii and end the application'
    time.sleep(1)

    Rumble = False
####				ONLY NEED RPT_CLASSIC
    wm.rpt_mode = cwiid.RPT_CLASSIC
    position = 50
    print 'starting position: ', position
    b = 0
    while True:
		
		a = wm.state['classic']
#		a = a['buttons']
#		b = wm.state['buttons']
		if b == a:
			continue

		print(a)
		b = a
#		print(bin(b))
#		print(wm.state)
		time.sleep(.01)


if __name__ == '__main__':
    main()
