def Laptops(processor,ram):
    if (processor >= 9) and (ram >= 32):
        return "You are very rich!"
    elif (processor < 9) and (ram >= 32):
        return "Still you can work on 32 gb ram!"
    elif (processor > 9) and (ram < 32):
        return "You have to increase your ram!"
    else:
        return "You are little bit old!"

print(Laptops(,))
