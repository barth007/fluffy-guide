def decryption(beta_values: list, gamma_values: list):

    # Decrypting back the gamma values to get alpha values 
    decrypted_alpha_values = []
    for i in range(len(beta_values)):
        inverse = pow(gamma_values[i], -1, beta_values[i])
        decrypted_alpha_values.append(inverse)

    print("<<<<<<<<<<<<<<<<Executed decryption.py file successfully>>>>>>>>>>>>>>")
    print("-------------------------------------------------")
    print("DATA RECEIVED FROM CORONA GRAPH: ")
    print("beta values: ", beta_values)
    print("gamma values: ", gamma_values)
    print("-------------------------------------------------")
    print("decrypted values: ", decrypted_alpha_values)

    # Decrypting according to the above decrypted_alpha_values 
    decrypted_message = ''

    reciever_secret = None
    while reciever_secret == None:
        reciever_secret=int(input("enter your secret key (in form of integer): "))
        if isinstance(reciever_secret,int):
            print("your key is being used...")
        else:
            reciever_secret=None
    print(reciever_secret)

    s = reciever_secret 
    for val in decrypted_alpha_values:
        letter_position = (val - ((2 * s) // 2)) % 26 + 64 
        w = chr(letter_position)
        decrypted_message += w

    print("Decrypted text: ", decrypted_message.replace("XX", "\n"))
