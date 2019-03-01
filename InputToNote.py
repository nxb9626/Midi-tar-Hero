
class inputToNote:
    """takes input number and return command"""

    def __init__(self):
        pass

    def strip_out_strum(self, string_rep):


        try:
            string_rep[-15] = "0"
            string_rep[-1] = "0"
        finally:
            "Don't actually care if this fails, it just means that the strum isn't pressed"
        return int(bin(string_rep))

    def is_strumming_up(self, string_rep):
        return string_rep[-1] == '1'


    def is_strumming_down(self, string_rep):
        return string_rep[-15] == '1'

    def check_if_strumming(self, string_rep):
        try:
            return string_rep[-15] =='1' or string_rep[-1] == '1'
        finally:
            return False

    def which_way_is_strumming(self, string_rep):

        if self.check_if_strumming(string_rep):
            if self.is_strumming_down(string_rep):
                return "down"
            elif self.is_strumming_up(string_rep):
                return "up"
            else:
                return "neither"

    def make_it_a_binary_string(self, input_int):
        return str(bin(input_int))

    def whatNote(self, input_int):
        string_rep = self.make_it_a_binary_string(input_int)
        sharp = False
        play_note = False

        if(self.check_if_strumming(string_rep)):
            play_note = True

            if(self.which_way_is_strumming(string_rep) == "up"):
                sharp = True
            else:
                sharp = False
