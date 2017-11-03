from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

def viz_model(model):
    SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# from https://github.com/Kcrong/separate-korean/blob/master/separater.py
class Separater:
    # BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    _BASE_CODE = 44032
    _CHOSUNG = 588
    _JUNGSUNG = 28

    _CHOSUNG_LIST = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ',
                     u'ㅌ', u'ㅍ', u'ㅎ']
    _JUNGSUNG_LIST = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ',
                      u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']
    _JONGSUNG_LIST = [u' ', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ',
                      u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

    ch = _BASE_CODE + (0 * _CHOSUNG + 2 * _JUNGSUNG)

    def __init__(self, word):
        self.word = word

    @property
    def sep_all(self):
        try:
            _all_ = list()

            for ch in self.word:
                for tmp in ch:
                    chbase = ord(tmp) - Separater._BASE_CODE

                    ch_1 = chbase // Separater._CHOSUNG
                    _all_.append(Separater._CHOSUNG_LIST[ch_1])

                    ch_2 = (chbase - (Separater._CHOSUNG * ch_1)) // Separater._JUNGSUNG
                    _all_.append(Separater._JUNGSUNG_LIST[ch_2])

                    ch_3 = (chbase - (Separater._CHOSUNG * ch_1) - (Separater._JUNGSUNG * ch_2))
                    _all_.append(Separater._JONGSUNG_LIST[ch_3])

            while True:
                try:
                    _all_.remove(' ')
                except ValueError:
                    break
        except:
            print(self.word)
            raise

        return _all_

    @property
    def chosung(self):
        all_chosung = list()
        for ch in self.word:
            for tmp in ch:
                all_chosung.append(Separater._CHOSUNG_LIST[((ord(tmp) - Separater._BASE_CODE) // Separater._CHOSUNG)])
        return all_chosung

    @property
    def jungsung(self):
        all_jungsung = list()

        for ch in self.word:
            for tmp in ch:
                chbase = ord(tmp) - Separater._BASE_CODE
                jungsung_idx = (chbase - (Separater._CHOSUNG * (chbase // Separater._CHOSUNG))) // Separater._JUNGSUNG
                all_jungsung.append(Separater._JUNGSUNG_LIST[jungsung_idx])
        return all_jungsung

    @property
    def jongsung(self):
        all_jongsung = list()

        for ch in self.word:
            for tmp in ch:
                chbase = ord(tmp) - Separater._BASE_CODE
                c_idx = chbase // Separater._CHOSUNG

                jongsung_idx = (chbase - (Separater._CHOSUNG * c_idx) - (
                    Separater._JUNGSUNG * ((chbase - (Separater._CHOSUNG * c_idx)) // Separater._JUNGSUNG)))
                all_jongsung.append(Separater._JONGSUNG_LIST[jongsung_idx])
        return all_jongsung


def sep_all(sent):
    return [let for letter in sent if letter != ' ' for let in Separater(letter).sep_all]
