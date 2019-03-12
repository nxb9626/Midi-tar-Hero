import cwiid
import time

class wiiMote:
    def __init__(self):
        print 'Press button 1 + 2 on your Wii Remote...'
        time.sleep(1)

        self.wm = cwiid.Wiimote()
        # time.sleep(4)
        self.wm.rpt_mode = cwiid.RPT_CLASSIC
        print 'Wii Remote connected...'
        print '\nPress the PLUS button to disconnect the Wii and end the application'
        time.sleep(1)



    def get_buttons(self):
        a = self.wm.state['classic']
        return a['buttons']

    def get_wammy(self):
        a = self.wm.state['classic']
        return a['r']