from tkinter import messagebox, Label, Frame, Tk

root = Tk


def information(com_input, root):
    currencies_info_uan = [
        {"name": "USD", "buy": "38.38🔼", "sell": "38.52🔼"},
        {"name": "EUR", "buy": "42.00🔼", "sell": "42.20🔼"},
        {"name": "GBP", "buy": "48.20🔼", "sell": "49.20🔼"},
        {"name": "CHF", "buy": "43.20🔼", "sell": "43.50🔼"},
        {"name": "PLN", "buy": "9.67🔼", "sell": "10.18🔼"}
    ]
    currencies_info_usd = [
        {"name": "UAN", "buy": "0.022🔼", "sell": "0.026🔼"},
        {"name": "EUR", "buy": "0.81🔼", "sell": "0.91🔼"},
        {"name": "GBP", "buy": "0.69🔼", "sell": "0.78🔼"},
        {"name": "CHF", "buy": "0.80🔼", "sell": "0.88🔼"},
        {"name": "PLN", "buy": "3.70🔼", "sell": "3.93🔼"}
    ]
    currencies_info_eur = [
        {"name": "UAN", "buy": "0.019🔼", "sell": "0.024🔼"},
        {"name": "USD", "buy": "0.85🔼", "sell": "0.91🔼"},
        {"name": "GBP", "buy": "1.11🔼", "sell": "1.17🔼"},
        {"name": "CHF", "buy": "1.00🔼", "sell": "1.04🔼"},
        {"name": "PLN", "buy": "0.21🔼", "sell": "0.23🔼"}
    ]
    currencies_info_gbp = [
        {"name": "UAN", "buy": "0.017🔼", "sell": "0.020🔼"},
        {"name": "USD", "buy": "0.73🔼", "sell": "0.78🔼"},
        {"name": "EUR", "buy": "0.82🔼", "sell": "0.85🔼"},
        {"name": "CHF", "buy": "0.85🔼", "sell": "0.89🔼"},
        {"name": "PLN", "buy": "0.18🔼", "sell": "0.20🔼"}
    ]
    currencies_info_chf = [
        {"name": "UAN", "buy": "0.020🔼", "sell": "0.023🔼"},
        {"name": "USD", "buy": "0.85🔼", "sell": "0.88🔼"},
        {"name": "EUR", "buy": "0.94🔼", "sell": "0.96🔼"},
        {"name": "GBP", "buy": "1.10🔼", "sell": "1.13🔼"},
        {"name": "PLN", "buy": "0.19🔼", "sell": "0.22🔼"}
    ]
    currencies_info_pln = [
        {"name": "UAN", "buy": "0.8🔼", "sell": "0.10🔼"},
        {"name": "USD", "buy": "3.89🔼", "sell": "3.93🔼"},
        {"name": "EUR", "buy": "4.27🔼", "sell": "4.30🔼"},
        {"name": "GBP", "buy": "5.02🔼", "sell": "5.06🔼"},
        {"name": "CHF", "buy": "4.46🔼", "sell": "4.48🔼"}
    ]
    if com_input.get() == "UAN ₴":
        for currency_info in currencies_info_uan:
            currency_frame = Frame(root)
            currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
            Label.config(currency_frame, text=f"{currency_info['name']}", font="helvetica", fg="#354a53").pack(
                side="left",
                padx=(0, 10))
            Label.config(currency_frame, text=currency_info['buy'], font="helvetica", fg="#354a53").pack(side="left",
                                                                                                         padx=(50, 30))
            Label.config(currency_frame, text=currency_info['sell'], font="helvetica", fg="#354a53").pack(side="left")
    elif com_input.get() == "USD $":
        for currency_info in currencies_info_usd:
            currency_frame = Frame(root)
            currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
            Label.config(currency_frame, text=f"{currency_info['name']}", font="helvetica", fg="#354a53").pack(
                side="left",
                padx=(0, 10))
            Label.config(currency_frame, text=currency_info['buy'], font="helvetica", fg="#354a53").pack(side="left",
                                                                                                         padx=(50, 30))
            Label.config(currency_frame, text=currency_info['sell'], font="helvetica", fg="#354a53").pack(side="left")
    elif com_input.get() == "EUR €":
        for currency_info in currencies_info_eur:
            currency_frame = Frame(root)
            currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
            Label.config(currency_frame, text=f"{currency_info['name']}", font="helvetica", fg="#354a53").pack(
                side="left",
                padx=(0, 10))
            Label.config(currency_frame, text=currency_info['buy'], font="helvetica", fg="#354a53").pack(side="left",
                                                                                                         padx=(50, 30))
            Label.config(currency_frame, text=currency_info['sell'], font="helvetica", fg="#354a53").pack(side="left")
    elif com_input.get() == "GBP £":
        for currency_info in currencies_info_gbp:
            currency_frame = Frame(root)
            currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
            Label.config(currency_frame, text=f"{currency_info['name']}", font="helvetica", fg="#354a53").pack(
                side="left",
                padx=(0, 10))
            Label.config(currency_frame, text=currency_info['buy'], font="helvetica", fg="#354a53").pack(side="left",
                                                                                                         padx=(50, 30))
            Label.config(currency_frame, text=currency_info['sell'], font="helvetica", fg="#354a53").pack(side="left")
    elif com_input.get() == "CHF ₣":
        for currency_info in currencies_info_chf:
            currency_frame = Frame(root)
            currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
            Label.config(currency_frame, text=f"{currency_info['name']}", font="helvetica", fg="#354a53").pack(
                side="left",
                padx=(0, 10))
            Label.config(currency_frame, text=currency_info['buy'], font="helvetica", fg="#354a53").pack(side="left",
                                                                                                         padx=(50, 30))
            Label.config(currency_frame, text=currency_info['sell'], font="helvetica", fg="#354a53").pack(side="left")
    elif com_input.get() == "PLN zł":
        for currency_info in currencies_info_pln:
            currency_frame = Frame(root)
            currency_frame.pack(pady=(10, 0), padx=40, anchor="w")
            Label.config(currency_frame, text=f"{currency_info['name']}", font="helvetica", fg="#354a53").pack(
                side="left",
                padx=(0, 10))
            Label.config(currency_frame, text=currency_info['buy'], font="helvetica", fg="#354a53").pack(side="left",
                                                                                                         padx=(50, 30))
            Label.config(currency_frame, text=currency_info['sell'], font="helvetica", fg="#354a53").pack(side="left")


def change_currency(event, text_input, text_output, com_input, com_output):
    currency_to_uan_trade = {
        "USD$_to_UAN₴": 38.18,
        "EUR€_to_UAN₴": 42,
        "GBP£_to_UAN₴": 49,
        "CHF₣_to_UAN₴": 43.50,
        "PLNzł_to_UAN₴": 10
    }
    currency_to_usd_trade = {
        "UAN₴_to_USD$": 0.026,
        "EUR€_to_USD$": 0.91,
        "GBP£_to_USD$": 0.78,
        "CHF₣_to_USD$": 0.88,
        "PLNzł_to_USD$": 3.93
    }
    currency_to_eur_trade = {
        "UAN₴_to_EUR€": 0.024,
        "USD$_to_EUR€": 0.91,
        "GBP£_to_EUR€": 1.17,
        "CHF₣_to_EUR€": 1.04,
        "PLNzł_to_EUR€": 0.23
    }
    currency_to_gbp_trade = {
        "UAN₴_to_GBP£": 0.020,
        "USD$_to_GBP£": 0.78,
        "EUR€_to_GBP£": 0.85,
        "CHF₣_to_GBP£": 0.89,
        "PLNzł_to_GBP£": 0.20
    }
    currency_to_chf_trade = {
        "UAN₴_to_CHF₣": 0.023,
        "USD$_to_CHF₣": 0.88,
        "EUR€_to_CHF₣": 0.96,
        "GBP£_to_CHF₣": 1.13,
        "PLNzł_to_CHF₣": 0.22
    }
    currency_to_pln_trade = {
        "UAN₴_to_PLNzł": 0.10,
        "USD$_to_PLNzł": 3.93,
        "EUR€_to_PLNzł": 4.30,
        "GBP£_to_PLNzł": 5.06,
        "CHF₣_to_PLNzł": 4.48
    }
    try:
        if com_input.get() == com_output.get():
            text_output.delete("1.0", "end-1c")
            text_input.delete("1.0", "end-1c")
            messagebox.showerror("Error", "Input and output currencies can't be the same")
        elif com_input.get() == "USD $" and com_output.get() == "UAN ₴":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_uan_trade["USD$_to_UAN₴"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "EUR €" and com_output.get() == "UAN ₴":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_uan_trade["EUR€_to_UAN₴"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "GBP £" and com_output.get() == "UAN ₴":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_uan_trade["GBP£_to_UAN₴"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "CHF ₣" and com_output.get() == "UAN ₴":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_uan_trade["CHF₣_to_UAN₴"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "PLN zł" and com_output.get() == "UAN ₴":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_uan_trade["PLNzł_to_UAN₴"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "UAN ₴" and com_output.get() == "USD $":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_usd_trade["UAN₴_to_USD$"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "EUR €" and com_output.get() == "USD $":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_usd_trade["EUR€_to_USD$"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "GBP £" and com_output.get() == "USD $":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_usd_trade["GBP£_to_USD$"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "CHF ₣" and com_output.get() == "USD $":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_usd_trade["CHF₣_to_USD$"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "PLN zł" and com_output.get() == "USD $":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_usd_trade["PLNzł_to_USD$"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "UAN ₴" and com_output.get() == "EUR €":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_eur_trade["UAN₴_to_EUR€"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "USD $" and com_output.get() == "EUR €":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_eur_trade["USD$_to_EUR€"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "GBP £" and com_output.get() == "EUR €":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_eur_trade["GBP£_to_EUR€"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "CHF ₣" and com_output.get() == "EUR €":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_eur_trade["CHF₣_to_EUR€"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "PLN zł" and com_output.get() == "EUR €":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_eur_trade["PLNzł_to_EUR€"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "UAN ₴" and com_output.get() == "GBP £":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_gbp_trade["UAN₴_to_GBP£"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "USD $" and com_output.get() == "GBP £":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_gbp_trade["USD$_to_GBP£"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "EUR €" and com_output.get() == "GBP £":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_gbp_trade["EUR€_to_GBP£"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "CHF ₣" and com_output.get() == "GBP £":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_gbp_trade["CHF₣_to_GBP£"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "PLN zł" and com_output.get() == "GBP £":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_gbp_trade["PLNzł_to_GBP£"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "UAN ₴" and com_output.get() == "CHF ₣":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_chf_trade["UAN₴_to_CHF₣"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "USD $" and com_output.get() == "CHF ₣":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_chf_trade["USD$_to_CHF₣"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "EUR €" and com_output.get() == "CHF ₣":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_chf_trade["EUR€_to_CHF₣"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "GBP £" and com_output.get() == "CHF ₣":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_chf_trade["GBP£_to_CHF₣"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "PLN zł" and com_output.get() == "CHF ₣":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_chf_trade["PLNzł_to_CHF₣"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "UAN ₴" and com_output.get() == "PLN zł":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_pln_trade["UAN₴_to_PLNzł"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "USD $" and com_output.get() == "PLN zł":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_pln_trade["USD$_to_PLNzł"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "EUR €" and com_output.get() == "PLN zł":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_pln_trade["EUR€_to_PLNzł"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "GBP £" and com_output.get() == "PLN zł":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_pln_trade["GBP£_to_PLNzł"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))
        elif com_input.get() == "CHF ₣" and com_output.get() == "PLN zł":
            result = float(text_input.get("1.0", "end-1c")) * currency_to_pln_trade["CHF₣_to_PLNzł"]
            print(round(result, 2))
            text_output.delete("1.0", "end-1c")
            text_output.insert("end-1c", str(round(result, 2)))

    except ValueError:
        text_output.delete("1.0", "end-1c")
        text_input.delete("1.0", "end-1c")
        messagebox.showerror("Помилка", "Введіть коректне числове значення")
