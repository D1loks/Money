from Functions import change_currency, information


def on_combobox_selected(event, text_input, text_output, com_input, com_output, label_name1, label_buy1, label_sell1,
                         label_name2, label_buy2, label_sell2,
                         label_name3, label_buy3, label_sell3,
                         label_name4, label_buy4, label_sell4,
                         label_name5, label_buy5, label_sell5):
    change_currency(event, text_input, text_output, com_input, com_output)
    information(com_input, label_name1, label_buy1, label_sell1,
                label_name2, label_buy2, label_sell2,
                label_name3, label_buy3, label_sell3,
                label_name4, label_buy4, label_sell4,
                label_name5, label_buy5, label_sell5)
