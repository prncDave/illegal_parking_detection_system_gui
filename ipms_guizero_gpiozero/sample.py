# main.py
import guizero
from guizero import App, Box, Text, PushButton
from sample_page1 import page1
from features import cautionFont

# -----------------------------
# APP INITIALIZATION
# -----------------------------
app = App(title="IPMS GUI", width=1024, height=700)
app.tk.resizable(False, False)

# -----------------------------
# NAVIGATION LOGIC
# -----------------------------
def go_to_page2():
    main_view.hide()
    details_view.show()

def go_to_page1():
    details_view.hide()
    main_view.show()

# -----------------------------
# PAGE INITIALIZATION
# -----------------------------
# 1. Instantiate Page 1 (Main Screen)
main_view = page1(app, on_ok_click=go_to_page2, on_details_click=go_to_page2)

# 2. Instantiate Page 2 / Secondary Frame (Hidden by default)
details_view = Box(app, width="fill", height="fill", visible=False)

p2_top = Box(details_view, width="fill", height=500)
p2_text = Text(p2_top, text="Details / Secondary Page", size=22, bold=True)
p2_text.tk.place(relx=0.5, rely=0.2, anchor="n")

p2_bottom = Box(details_view, width="fill", height=160, align="bottom")
back_btn = PushButton(p2_bottom, text="Back", command=go_to_page1)
back_btn.text_size = 18
back_btn.bold = True
back_btn.font = cautionFont
back_btn.tk.place(relx=0.1, rely=0.2)

# Run Application Loop
app.display()