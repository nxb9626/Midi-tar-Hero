
class inputToNote:
    """takes input number and return command"""

    def __init__(self):
        self.current_octave = 60

    def remove_strum(self, input_int):
        if input_int > 16000:
            return input_int-16384
        elif input_int % 2 ==1:
            return input_int -1
        else:
            return input_int

    def is_strumming(self, input_int):
        return input_int > 16000 or self.is_strumming_up(input_int)

    def is_strumming_up(self, input_int):
        return input_int % 2 == 1

    def get_note_from_code(self, input_int):
        notes = {
            #0: -12,
            120: -10,
            88: -8,
            112: -7,
            80: -5,
            24: -3,
            48: -1,
            16:	0,
            64:	2,
            8:	4,
            32:	5,
            128:	7,
            192:	9,
            136:	11,
            160:	12,
            224:	14,
            168:	16,
            232:	17
        }
        return notes.get(input_int)

    def whatNote(self, input_int):
        if self.is_strumming(input_int):
            note = self.remove_strum(input_int)
            if note == input_int:
                return None
            else:
                note = self.get_note_from_code(note)
                if(note == None):
                    return None
                if(self.is_strumming_up(input_int)):
                    note +=1
                return note + self.current_octave

        return

    def whatWhammy(self, input_wam):
        return input_wam-15
