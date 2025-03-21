import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def check_language(self,e):
        if self._view._ddlanguage.value in ["italian","english","spanish"]:
            self._view._lang_check.value="Selezione avvenuta correttamente!"
            self._view.page.update()

    def check_search(self,e):
        if self._view._ddsearch.value in ["Lineare","Default","Dicotomica"]:
            self._view._search_check.value = "Selezione avvenuta correttamente!"
            self._view.page.update()


    def handleSentence(self):
        txtIn = self._view._txtIn.value
        language = self._view._ddlanguage.value
        modality = self._view._ddsearch.value

        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = ""

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                # scrivo sulla pagina...
                #self._view.update()
                self._view.paroleErrate.value = paroleErrate
                self._view.time.value = str(t2 - t1)
                self._view.update_listview()

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                self._view.paroleErrate.value = paroleErrate
                self._view.time.value = str(t2 - t1)
                self._view.update_listview()


            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                self._view.paroleErrate.value = paroleErrate
                self._view.time.value = str(t2 - t1)
                self._view.update_listview()
            case _:
                return None

        # svuoto il TextField che contiene la frase
        self._view._txtIn.value = ""
        self._view.page.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

