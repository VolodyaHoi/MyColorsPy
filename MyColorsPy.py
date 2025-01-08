# Project: MyColorsPy
# Version: 0.1
# Author : VolodyaHoi[7nation]

class Colors():
    '''You can use preset colors. F prefix - Foreground, B prefix - Background, S  prefix - Style'''
    def __init__(self):
        self.F_BLACK = "\033[30m"
        self.F_RED = "\033[31m"
        self.F_GREEN = "\033[32m"
        self.F_YELLOW = "\033[33m"
        self.F_BLUE = "\033[34m"
        self.F_PURPLE = "\033[35m"
        self.F_AQUA = "\033[36m"
        self.F_WHITE = "\033[37m"

        self.B_BLACK = "\033[40m"
        self.B_RED = "\033[41m"
        self.B_GREEN = "\033[42m"
        self.B_YELLOW = "\033[43m"
        self.B_BLUE = "\033[44m"
        self.B_PURPLE = "\033[45m"
        self.B_AQUA = "\033[46m"
        self.B_WHITE = "\033[47m"
        
        self.S_CLEAR = "\033[0m"
        self.S_BOLD = "\033[1m"
        self.S_PALE = "\033[2m"
        self.S_ITALIC = "\033[3m"
        self.S_UNDERLINE = "\033[4m"
        self.S_FLASH = "\033[5m"
        self.S_HIDE = "\033[8m"
        self.S_CROSS = "\033[9m"
        self.S_DOUBLEUL = "\033[21m"
        self.S_FRAME = "\033[51m"
        self.S_SURROUND = "\033[52m"
        self.S_CROSSOUT = "\033[53m"

    def custom(self, r : int, g : int, b : int, background : bool):
        '''You can set custom color for foreground or background (RGB).If you set incorrect RGB values you get '?' char instead color'''
        if r < 0 or g < 0 or b < 0:
            self.custom_color = "?"
        else:
            if background == False:
                self.custom_color = "\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"
            elif background == True:
                self.custom_color = "\033[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"
            else:
                self.custom_color = "?"
        return self.custom_color
        
