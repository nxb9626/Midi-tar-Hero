import cwiid
import time
import midiController
import wiiMote
import InputToNote


def main():
    wm = wiiMote.wiiMote()
    midi = midiController.midiController()
    converter = InputToNote.inputToNote()
    while True:
        butt = wm.get_buttons()
        wamm = wm.get_wammy()
        note = converter.whatNote(butt)
        if note is None:
            continue
        note += wamm -15
        midi.start_note(note)
        print "starting: " + str(note)

        while butt == wm.get_buttons() and wamm == wm.get_wammy():
            time.sleep(.01)
            pass
        time.sleep(.01)
        midi.end_note(note)
        print "ending:" + str(note)

if __name__ == '__main__':
    main()