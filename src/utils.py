
class LanguageCodes:
    # Language codes (ISO 639) for languages to be recognized during analysis.
    def __init__(self) -> None:
        self.language_code=["abq","ady","af", "ang","ar","as","ava","az","be","bg","bh","bho","bn","bs","ch_sim","ch_tra","che","cs","cy","da","dar","de","en","es","et","fa","fr","ga","gom","hi","hr","hu","id","inh","is","it","ja","kbd","kn","ko","ku","la","lbe","lez","lt","lv","mah","mai","mi","mn","mr","ms","mt","ne","new","nl","no","oc","pi","pl","pt","ro","ru","rs_cyrillic","rs_latin","sck","sk","sl","sq","sv","sw","ta","tab","te","th","tjk","tl","tr","ug","uk","ur","uz","vi"]
    def get_code(self):
        return self.language_code