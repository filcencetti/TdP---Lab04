import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._txtIn = None
        self._lang_check=None
        self._search_check = None
        self.paroleErrate = None
        self.time = None

        # define the UI elements and populate the page

    def add_content(self):

        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self._lang_check = ft.Text()
        self._search_check = ft.Text()

        # Add your stuff here
        self._ddlanguage = ft.Dropdown(label="Seleziona la lingua",
                                       hint_text="Lingua",
                                       width=300,
                                       options=[ft.dropdown.Option("italian"),
                                                ft.dropdown.Option("english"),
                                                ft.dropdown.Option("spanish")],
                                       on_change=self.__controller.check_language)
        self.print_first_row()
        self._ddsearch = ft.Dropdown(alignment=ft.MainAxisAlignment.START,
                                     label="Tipo di ricerca",
                                     options=[ft.dropdown.Option("Default"),
                                                ft.dropdown.Option("Linear"),
                                                ft.dropdown.Option("Dichotomic")],
                                     hint_text="Ricerca",
                                     width=300,
                                     on_change=self.__controller.check_search)

        self._txtIn = ft.TextField(label="Inserisci il testo",
                                   width=500)



        self._btnStart = ft.ElevatedButton(text="Avvia ricerca",
                                           on_click=self.check_everything)

        self.print_second_row()

    def check_everything(self,e):

        self.paroleErrate = ft.Text()
        self.time = ft.Text()
        val = True
        if self._ddlanguage.value == "" or self._ddlanguage.value == None:
            self.page.add(ft.Text("Inserisci la lingua"))
            self.page.update()
        elif self._ddsearch.value == "" or self._ddsearch.value == None:
            self.page.add(ft.Text("Inserisci il tipo di ricerca"))
            self.page.update()
        elif self._txtIn.value == "" or self._txtIn.value == None:
            self.page.add(ft.Text("Inserisci il testo da correggere"))
            self.page.update()
        else:
            val = False
        if val == False:
            self.__controller.handleSentence()

    def print_first_row(self):
        row1 = ft.Row(controls=[self._ddlanguage, self._lang_check], alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row1)
        self.page.update()

    def print_second_row(self):
        row2 = ft.Row(controls=[self._ddsearch,self._txtIn,self._btnStart], alignment=ft.MainAxisAlignment.START)
        self.page.add(row2)

        row3 = ft.Row(controls=[self._search_check],alignment=ft.MainAxisAlignment.START)
        self.page.add(row3)
        self.page.update()

    def print_third_row(self):
        row4 = ft.Row(controls=[self._txtIn,self.paroleErrate, self.time])
        self.page.add(row4)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller


    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
