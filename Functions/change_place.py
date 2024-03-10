def change_place(event, com_input, com_output):
    input_currency = com_input.get()
    output_currency = com_output.get()
    com_input.set(output_currency)
    com_output.set(input_currency)
