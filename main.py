from tkinter import Tk, Label, Text, Frame, Button
from tkinter.ttk import Combobox

from Functions import change_currency, change_place, on_combobox_selected

root = Tk()
root.configure(bg="#212121")
w = root.winfo_screenwidth() // 2 - 150
h = root.winfo_screenheight() // 2 - 200
root.geometry(f'550x500+{w}+{h}')

text_input = None
text_output = None
com_input = None
com_output = None

input_frame = Frame(root, bg="#212121")
input_frame.pack(pady=(35, 0), padx=40, anchor="w")

lab_input = Label(input_frame, text="Ви віддаєте", font="helvetica", fg="white", bg="#212121")
lab_input.pack(side="left")

currency_input = ["UAN ₴", "USD $", "EUR €", "GBP £", "CHF ₣", "PLN zł"]
currency_output = ["UAN ₴", "USD $", "EUR €", "GBP £", "CHF ₣", "PLN zł"]
com_input = Combobox(input_frame, font=("helvetica", 20), width=7, state="readonly", values=currency_input,
                     background="black", foreground="yellow")
com_input.set(currency_input[1])
com_input.bind("<<ComboboxSelected>>",
               lambda event: on_combobox_selected(event, text_input, text_output, com_input, com_output, label_name1,
                                                  label_buy1, label_sell1,
                                                  label_name2, label_buy2, label_sell2,
                                                  label_name3, label_buy3, label_sell3,
                                                  label_name4, label_buy4, label_sell4,
                                                  label_name5, label_buy5, label_sell5))
com_input.pack(side="left", padx=(10, 0))

text_input = Text(input_frame, width=20, height=2, font="helvetica")
text_input.bind("<Return>", lambda event: change_currency(event, text_input, text_output, com_input, com_output))
text_input.pack(side="left")

change_btn = Button(root, text="↕️", font="helvetica", background="black", foreground="yellow")
change_btn.bind("<ButtonRelease-1>", lambda event: change_place(event, com_input, com_output))
change_btn.pack(pady=(10, 0), padx=(400, 0))

output_frame = Frame(root, bg="#212121")
output_frame.pack(pady=(10, 0), padx=40, anchor="w")

lab_output = Label(output_frame, text="Ви отримаєте", font="helvetica", fg="white", bg="#212121")
lab_output.pack(side="left")

com_output = Combobox(output_frame, font=("helvetica", 20), width=7, state="readonly", values=currency_output,
                      background="black", foreground="yellow")
com_output.set(currency_output[0])
com_output.bind("<<ComboboxSelected>>",
                lambda event: change_currency(event, text_input, text_output, com_input, com_output))
com_output.pack(side="left", padx=(10, 0))

text_output = Text(output_frame, width=20, height=2, font="helvetica")
text_output.bind("<Return>", lambda event: change_currency(event, text_input, text_output, com_input, com_output))
text_output.pack(side="left")

# Additional labels
info_frame = Frame(root, bg="#212121")
info_frame.pack(pady=(10, 0), padx=40, anchor="w")

Label(info_frame, text="Валюта", font="helvetica", fg="white", bg="#212121").pack(side="left", padx=(0, 10))
Label(info_frame, text="Купівля", font="helvetica", fg="white", bg="#212121").pack(side="left", padx=(50, 30))
Label(info_frame, text="Продаж", font="helvetica", fg="white", bg="#212121").pack(side="left")
currencies_info_usd = [
    {"name": "UAN", "buy": "0.022🔼", "sell": "0.026🔼"},
    {"name": "EUR", "buy": "0.81🔼", "sell": "0.91🔼"},
    {"name": "GBP", "buy": "0.69🔼", "sell": "0.78🔼"},
    {"name": "CHF", "buy": "0.80🔼", "sell": "0.88🔼"},
    {"name": "PLN", "buy": "3.70🔼", "sell": "3.93🔼"}
]
currency_frame = Frame(root, bg="#212121")
currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
label_name1 = Label(currency_frame, text=f"{currencies_info_usd[0]['name']}", font="helvetica", fg="yellow",
                    bg="#212121")
label_buy1 = Label(currency_frame, text=currencies_info_usd[0]['buy'], font="helvetica", fg="white", bg="#212121")
label_sell1 = Label(currency_frame, text=currencies_info_usd[0]['sell'], font="helvetica", fg="white", bg="#212121")
label_name1.pack(side="left", padx=(0, 10))
label_buy1.pack(side="left", padx=(50, 30))
label_sell1.pack(side="left")
currency_frame = Frame(root, bg="#212121")
currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
label_name2 = Label(currency_frame, text=f"{currencies_info_usd[1]['name']}", font="helvetica", fg="yellow",
                    bg="#212121")
label_buy2 = Label(currency_frame, text=currencies_info_usd[1]['buy'], font="helvetica", fg="white", bg="#212121")
label_sell2 = Label(currency_frame, text=currencies_info_usd[1]['sell'], font="helvetica", fg="white", bg="#212121")
label_name2.pack(side="left", padx=(0, 10))
label_buy2.pack(side="left", padx=(50, 30))
label_sell2.pack(side="left")
currency_frame = Frame(root, bg="#212121")
currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
label_name3 = Label(currency_frame, text=f"{currencies_info_usd[2]['name']}", font="helvetica", fg="yellow",
                    bg="#212121")
label_buy3 = Label(currency_frame, text=currencies_info_usd[2]['buy'], font="helvetica", fg="white", bg="#212121")
label_sell3 = Label(currency_frame, text=currencies_info_usd[2]['sell'], font="helvetica", fg="white", bg="#212121")
label_name3.pack(side="left", padx=(0, 10))
label_buy3.pack(side="left", padx=(50, 30))
label_sell3.pack(side="left")
currency_frame = Frame(root, bg="#212121")
currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
label_name4 = Label(currency_frame, text=f"{currencies_info_usd[3]['name']}", font="helvetica", fg="yellow",
                    bg="#212121")
label_buy4 = Label(currency_frame, text=currencies_info_usd[3]['buy'], font="helvetica", fg="white", bg="#212121")
label_sell4 = Label(currency_frame, text=currencies_info_usd[3]['sell'], font="helvetica", fg="white", bg="#212121")
label_name4.pack(side="left", padx=(0, 10))
label_buy4.pack(side="left", padx=(50, 30))
label_sell4.pack(side="left")
currency_frame = Frame(root, bg="#212121")
currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
label_name5 = Label(currency_frame, text=f"{currencies_info_usd[4]['name']}", font="helvetica", fg="yellow",
                    bg="#212121")
label_buy5 = Label(currency_frame, text=currencies_info_usd[4]['buy'], font="helvetica", fg="white", bg="#212121")
label_sell5 = Label(currency_frame, text=currencies_info_usd[4]['sell'], font="helvetica", fg="white", bg="#212121")
label_name5.pack(side="left", padx=(0, 10))
label_buy5.pack(side="left", padx=(50, 30))
label_sell5.pack(side="left")
root.mainloop()
