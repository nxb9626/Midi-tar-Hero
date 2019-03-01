# -------------------------------------------------------------------------------
# Name:        	WiiTar.py
# Purpose:		read input from guitar hero controller and translate it to rtmidi
# Author:      Noah Britton
#

import time
import cwiid
import rtmidi_python as rtmidi


# from rtmidi.midiutil import open_midioutput
# from rtmidi.midiconstants import (NOTE_OFF, NOTE_ON)

def setupRtMidi():
    midiout = rtmidi.MidiOut()
    # available_ports = midiout.get_ports()

    midiout.open_port(0)

    return midiout


def start_note(midi_out, x):
    note_on = [0x90, int(x), 1]
    midi_out.send_message(note_on)


def stop_note(midi_out, x):
    note_off = [0x80, int(x), 0]
    midi_out.send_message(note_off)


def connect_wiimote():
    ###PROGRAM
    print 'Press button 1 + 2 on your Wii Remote...'
    time.sleep(1)

    wm = cwiid.Wiimote()
    print 'Wii Remote connected...'
    print '\nPress the PLUS button to disconnect the Wii and end the application'
    time.sleep(1)
    return wm


def main():
    ###SETUP FOR SYNTH
    midi_out = setupRtMidi()

    ###SETUP FOR WIIMOTE
    wm = connect_wiimote()

    ###SETUP FOR NOTES
    notes = {
        # notes for downstrum
        1: - 12,
        121: - 10,
        89: - 8,
        113: - 6,
        81: - 4,
        25: - 2,
        49: 0,
        17: 2,
        65: 4,
        9: 6,
        33: 8,
        129: 10,
        193: 12,
        137: 14,
        161: 16,
        225: 18,
        169: 20,
        233: 22,
        # notes for upstrum
        16504: - 11,
        16472: - 9,
        16496: - 7,
        16464: - 5,
        16408: - 3,
        16432: - 1,
        16400: 1,
        16448: 3,
        16392: 5,
        16416: 7,
        16512: 9,
        16576: 11,
        16520: 13,
        16544: 15,
        16608: 17,
        16552: 19,
        16616: 21,
        # inputs for increasing octave
        20600: "upOctave",
        20568: "upOctave",
        20592: "upOctave",
        20560: "upOctave",
        20504: "upOctave",
        20528: "upOctave",
        20496: "upOctave",
        20544: "upOctave",
        20488: "upOctave",
        20512: "upOctave",
        20608: "upOctave",
        20672: "upOctave",
        20616: "upOctave",
        20640: "upOctave",
        20704: "upOctave",
        20648: "upOctave",
        4096: "upOctave",
        # inputs for decreasing octave
        17528: "downOctave",
        17496: "downOctave",
        17520: "downOctave",
        17488: "downOctave",
        17432: "downOctave",
        17456: "downOctave",
        17424: "downOctave",
        17472: "downOctave",
        17416: "downOctave",
        17440: "downOctave",
        17536: "downOctave",
        17600: "downOctave",
        17544: "downOctave",
        17568: "downOctave",
        17632: "downOctave",
        17576: "downOctave",
        17640: "downOctave",
        1024: "downOctave"
        # potential future inputs
    }
    # INIT STATE OF WIITAR
    wm.rpt_mode = cwiid.RPT_CLASSIC  # | cwiid.RPT_BTN | cwiid.RPT_ACC
    wm_butt = 0
    current_note = 0
    current_octave = 60
    inputs_read = False
    poll_delay = .01

    while True:
        curr_butt = wm.state['classic']
        wm_butt = curr_butt['buttons']



if __name__ == '__main__':
    main()
