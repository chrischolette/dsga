x_total=""
while True:
    x_input=str(raw_input("Enter a word (. ! or ? to end):"))
    x_total = x_total + " "+ x_input
    if x_input in (".", "!", "?"):
        print x_total
        break
    
    