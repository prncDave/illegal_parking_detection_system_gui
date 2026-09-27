from guizero import Text, PushButton, Box
from features import cautionFont, cautionColor

#-----------------------------
#   PAGE 2 - VIOLATION DETAILS
#-----------------------------


class Page2:
    def __init__(self, app, show_page):
        self.box = Box(app, width="fill", height="fill")

        #---------------------
        # TEXT CONTENT
        self.title = Text(self.box, text="VIOLATION DETAILS")
        self.title.text_color = cautionColor
        self.title.text_size = 40
        self.title.bold = True
        self.title.tk.place(relx=0.5, rely=0.05, anchor="n")

        #----------------------------------
        # Buttons
        self.back_btn = PushButton(self.box, text="Back", padx=80, pady=35,
                                   command=lambda: show_page("page1"))
        self.back_btn.tk.config(highlightbackground="black", highlightthickness=6, relief="solid", bd=2)
        self.back_btn.tk.place(relx=0.5, rely=0.8, anchor="n")
        self.back_btn.text_size = 20
        self.back_btn.text_bold = True
        self.back_btn.font = cautionFont

    def show(self):
        self.box.show()

    def hide(self):
        self.box.hide()
