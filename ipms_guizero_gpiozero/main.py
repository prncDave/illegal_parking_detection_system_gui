from guizero import App
from page_1 import Page1
from page_2 import Page2
from page_3 import Page3
#-----------------------------
#   IPMS GUI - GUIZERO - GPIOZERO
#   Group 6 - CPE 2026    
#-----------------------------

app = App(title="IPMS GUI", width=1024, height=700, visible=True)
app.bg = "#E3E3E3"
app.tk.resizable(False, False)

pages = {}

def show_page(name):
    for page in pages.values():
        page.hide()
    pages[name].show()

pages["page1"] = Page1(app, show_page)
pages["page2"] = Page2(app, show_page)
pages["page3"] = Page3(app, show_page)
show_page("page1")
app.display()
