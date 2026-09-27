from guizero import Text, PushButton, Box, CheckBox
from PIL import Image, ImageDraw, ImageTk
from features import cautionFont, cautionColor

CHECKBOX_SIZE = 36

#-----------------------------
#   Page 3 - Violation Proceeding
#
#-----------------------------

def make_checkbox_images(size):
    border = max(2, size // 12)
    off = Image.new("RGB", (size, size), "black")   
    ImageDraw.Draw(off).rectangle([border, border, size - 1 - border, size - 1 - border], fill="white")

    on = off.copy()
    points = [(size * 0.22, size * 0.52), (size * 0.42, size * 0.72), (size * 0.78, size * 0.28)]
    ImageDraw.Draw(on).line(points, fill="black", width=max(3, size // 8), joint="curve")

    return ImageTk.PhotoImage(off), ImageTk.PhotoImage(on)

class Page3:
    def __init__(self, app, show_page):
        self.box = Box(app, width="fill", height="fill")

        #---------------------
        #CONTAINERS
        self.top_frame = Box(self.box, width="fill", height=550)
        
        
        #CONTENT
        self.title_page3 = Text(self.top_frame, text="PENALTY FINES HAS BEEN ISSUED \n APPLIED ON YOUR VEHICLE")
        self.title_page3.font = cautionFont
        self.title_page3.text_size = 40
        self.title_page3.bold = True
        self.title_page3.text_color = cautionColor
        self.title_page3.tk.place(relx=0.5, rely=0.9, anchor="n")

        #law enforcement text
        self.law_enforcement_text = Text(self.top_frame, text="Under law enforcement: \nRepublic Act No. 4136 Sec.4 & Republic Act No. 7160 Sec. 391(a) \n\nViolation Number: 1234567890")
        self.law_enforcement_text.tk.config(padx=10, pady=400)
        self.law_enforcement_text.font = cautionFont
        self.law_enforcement_text.text_size = 23
        self.law_enforcement_text.bold = False
        self.law_enforcement_text.text_color = "black"
        self.law_enforcement_text.tk.config(justify="left")

        #checkbox
        self.checkbox = CheckBox(self.top_frame, text="I have read and agree to the terms and conditions", command=self.toggle_proceed)
        self.checkbox.font = cautionFont
        self.checkbox.text_size = 23
        self.checkbox.bold = False
        self.checkbox.text_color = "black"
        self.checkbox.tk.config(justify="left")
        self._cb_off, self._cb_on = make_checkbox_images(CHECKBOX_SIZE)
        # Windows Tk forces "sunken" (and a 1px content offset) when selected with indicatoron off,
        # so every state is sunken; bd=0 keeps the border invisible.
        self.checkbox.tk.config(image=self._cb_off, selectimage=self._cb_on, compound="left",
                                indicatoron=False, relief="sunken", offrelief="sunken", overrelief="sunken",
                                bd=0, highlightthickness=0, padx=10,
                                selectcolor=self.checkbox.tk.cget("bg"))
        self.checkbox.tk.place(relx=0.4, rely=0.9, anchor="s")

        #----------------------------------
        # Buttons
        self.proceed_btn = PushButton(self.box, text="PROCEED", padx=100, pady=30, command=lambda: show_page("page1"))
        self.proceed_btn.tk.config(highlightbackground="black", highlightthickness=6, relief="solid", bd=2)
        self.proceed_btn.tk.place(relx=0.8, rely=0.98, anchor="s")
        self.proceed_btn.text_size = 20
        self.proceed_btn.font = cautionFont
        self.proceed_btn.disable()


    def toggle_proceed(self):
        if self.checkbox.value == 1:
            self.proceed_btn.enable()
        else:
            self.proceed_btn.disable()

    def show(self):
        self.checkbox.value = 0
        self.proceed_btn.disable()
        self.box.show()

    def hide(self):
        self.box.hide()