# for now this program will allow you to add a spell

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class CharInfo:
    def __init__(self, AS_str, AS_dex, AS_con, AS_int, AS_wis, AS_cha, AM_str, AM_dex, AM_con, AM_int, AM_wis, AM_cha, level, proficiency, splAtkBns, splSvDC):
        self.AS_str = AS_str
        self.AS_dex = AS_dex
        self.AS_con = AS_con
        self.AS_int = AS_int
        self.AS_wis = AS_wis
        self.AS_cha = AS_cha
        self.AM_str = AM_str
        self.AM_dex = AM_dex
        self.AM_con = AM_con
        self.AM_int = AM_int
        self.AM_wis = AM_wis
        self.AM_cha = AM_cha
        self.level = level
        self.proficiency = proficiency
        self.splAtkBns = splAtkBns
        self.splSvDC = splSvDC

    def set_AS_str(self, AS_str):
        self.AS_str = AS_str

    def set_AS_dex(self, AS_dex):
        self.AS_dex = AS_dex

    def set_AS_con(self, AS_con):
        self.AS_con = AS_con

    def set_AS_int(self, AS_int):
        self.AS_int = AS_int

    def set_AS_wis(self, AS_wis):
        self.AS_wis = AS_wis

    def set_AS_cha(self, AS_cha):
        self.AS_cha = AS_cha

    def set_AS_str(self, AS_str):
        self.AS_str = AS_str

    def set_AS_dex(self, AS_dex):
        self.AS_dex = AS_dex

    def set_AS_con(self, AS_con):
        self.AS_con = AS_con

    def set_AS_int(self, AS_int):
        self.AS_int = AS_int

    def set_AS_wis(self, AS_wis):
        self.AS_wis = AS_wis

    def set_AS_cha(self, AS_cha):
        self.AS_cha = AS_cha

    
        self.level = level
        self.proficiency = proficiency
        self.splAtkBns = splAtkBns
        self.splSvDC = splSvDC



class Megs_Spellcasting_Aid(App):
    def build(self):
        pass


if __name__ == '__main__':
    Megs_Spellcasting_Aid().run()
