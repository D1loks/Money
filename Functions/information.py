def information(com_input, label_name1, label_buy1, label_sell1,
                label_name2, label_buy2, label_sell2,
                label_name3, label_buy3, label_sell3,
                label_name4, label_buy4, label_sell4,
                label_name5, label_buy5, label_sell5):
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
    labels = [label_name1, label_buy1, label_sell1,
              label_name2, label_buy2, label_sell2,
              label_name3, label_buy3, label_sell3,
              label_name4, label_buy4, label_sell4,
              label_name5, label_buy5, label_sell5]
    if com_input.get() == "UAN ₴":
        for i, label in enumerate(labels):
            label.config(
                text=f"{currencies_info_uan[i // 3]['name' if i % 3 == 0 else 'buy' if i % 3 == 1 else 'sell']}",
                font="helvetica")
    elif com_input.get() == "USD $":
        for i, label in enumerate(labels):
            label.config(
                text=f"{currencies_info_usd[i // 3]['name' if i % 3 == 0 else 'buy' if i % 3 == 1 else 'sell']}",
                font="helvetica")
    elif com_input.get() == "EUR €":
        for i, label in enumerate(labels):
            label.config(
                text=f"{currencies_info_eur[i // 3]['name' if i % 3 == 0 else 'buy' if i % 3 == 1 else 'sell']}",
                font="helvetica")
    elif com_input.get() == "GBP £":
        for i, label in enumerate(labels):
            label.config(
                text=f"{currencies_info_gbp[i // 3]['name' if i % 3 == 0 else 'buy' if i % 3 == 1 else 'sell']}",
                font="helvetica")
    elif com_input.get() == "CHF ₣":
        for i, label in enumerate(labels):
            label.config(
                text=f"{currencies_info_chf[i // 3]['name' if i % 3 == 0 else 'buy' if i % 3 == 1 else 'sell']}",
                font="helvetica")
    elif com_input.get() == "PLN zł":
        for i, label in enumerate(labels):
            label.config(
                text=f"{currencies_info_pln[i // 3]['name' if i % 3 == 0 else 'buy' if i % 3 == 1 else 'sell']}",
                font="helvetica")
