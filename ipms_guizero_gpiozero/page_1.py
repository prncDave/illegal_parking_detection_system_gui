from pathlib import Path
from guizero import Text, PushButton, Box, Picture
from features import cautionFont, textCaution1, textCaution2, cautionColor, cautionSize

#-----------------------------
#   PAGE 1 - VIOLATION NOTICE
#-----------------------------

BASE_DIR = Path(__file__).parent


class Page1:
    def __init__(self, app, show_page):
        self.box = Box(app, width="fill", height="fill")

        #----------------------
        # CONTAINERS
        self.top_frame = Box(self.box, width="fill", height=550)

        self.buttom_frame = Box(self.box, width=512, height=200, align="left")
        self.buttom_frame.tk.place(relx=0.1, rely=0.86)

        self.buttom_frame1 = Box(self.box, width=512, height=200, align="right")
        self.buttom_frame1.tk.place(relx=0.50, rely=0.7842674)

        #---------------------
        # TEXT CONTENT
        self.top_frame_caution1 = Text(self.top_frame, text=textCaution1, align="top")
        self.top_frame_caution1.text_color = cautionColor
        self.top_frame_caution1.text_size = cautionSize
        self.top_frame_caution1.bold = True
        self.top_frame_caution1.tk.place(relx=0.5, rely=0, anchor="n")

        self.top_frame_caution2 = Text(self.top_frame, text=textCaution2, align="top")
        self.top_frame_caution2.text_color = cautionColor
        self.top_frame_caution2.text_size = cautionSize
        self.top_frame_caution2.bold = True
        self.top_frame_caution2.tk.place(relx=0.5, rely=.13, anchor="n")

        image_path = BASE_DIR / "sample.png"
        self.frame_title = Picture(self.top_frame, image=str(image_path), width=750, height=350)
        self.frame_title.tk.place(relx=0.5, rely=0.3, anchor="n")

        #----------------------------------
        # Buttons
        self.ok_btn = PushButton(self.buttom_frame1, text="OK", padx=100, pady=35, command=lambda: show_page("page3"))
        self.ok_btn.tk.config(highlightbackground="black", highlightthickness=6, relief="solid", bd=2)
        self.ok_btn.tk.place(relx=0.7, rely=0.05, anchor="n")
        self.ok_btn.text_size = 20
        self.ok_btn.text_bold = True
        self.ok_btn.font = cautionFont

        self.view_details = PushButton(self.buttom_frame, text="View Details", padx=60, pady=35,
                                       command=lambda: show_page("page2"))
        self.view_details.tk.config(highlightbackground="black", highlightthickness=6, relief="solid", bd=2)
        self.view_details.tk.place(relx=0.32, rely=0.05, anchor="n")
        self.view_details.text_size = 20
        self.view_details.text_bold = True
        self.view_details.font = cautionFont

    def show(self):
        self.box.show()

    def hide(self):
        self.box.hide()
