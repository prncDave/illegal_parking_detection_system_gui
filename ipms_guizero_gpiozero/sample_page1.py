# page1.py
from guizero import Text, PushButton, Box
from features import cautionFont, textCaution1, textCaution2, cautionColor, cautionSize, globalText

def page1(app, on_ok_click, on_details_click):
    # Main container box for Page 1
    page_1 = Box(app, width="fill", height="fill", visible=True)

    # ----------------------
    # CONTAINERS
    # ----------------------
    top_frame = Box(page_1, width="fill", height=550)

    buttom_frame = Box(page_1, width=512, height=200)
    buttom_frame.tk.place(relx=0.1, rely=0.86)

    buttom_frame1 = Box(page_1, width=512, height=200)
    buttom_frame1.tk.place(relx=0.50, rely=0.7842674)

    # ----------------------
    # TEXT CONTENT
    # ----------------------
    top_frame_caution1 = Text(top_frame, text=textCaution1)
    top_frame_caution1.text_color = cautionColor
    top_frame_caution1.text_size = cautionSize
    top_frame_caution1.bold = True
    top_frame_caution1.tk.place(relx=0.5, rely=0, anchor="n")

    top_frame_caution2 = Text(top_frame, text=textCaution2)
    top_frame_caution2.text_color = cautionColor
    top_frame_caution2.text_size = cautionSize
    top_frame_caution2.bold = True
    top_frame_caution2.tk.place(relx=0.5, rely=0.13, anchor="n")

    # ----------------------
    # BUTTONS
    # ----------------------
    view_details = PushButton(
        buttom_frame, 
        text="View Details", 
        padx=60, 
        pady=35, 
        command=on_details_click
    )
    view_details.tk.config(highlightbackground="black", highlightthickness=6, relief="solid", bd=2)
    view_details.tk.place(relx=0.15, rely=0.05, anchor="n")
    view_details.text_size = 20
    view_details.text_bold = True
    view_details.font = cautionFont

    ok_btn = PushButton(
        buttom_frame1, 
        text="OK", 
        padx=100, 
        pady=35, 
        command=on_ok_click
    )
    ok_btn.tk.config(highlightbackground="black", highlightthickness=6, relief="solid", bd=2)
    ok_btn.tk.place(relx=0.7, rely=0.05, anchor="n")
    ok_btn.text_size = 20
    ok_btn.text_bold = True
    ok_btn.font = cautionFont

    return page_1