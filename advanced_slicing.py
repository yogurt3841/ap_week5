def advanced_slice():
    

    # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # a. Extract the letters 'hij'.
    print(alphabet[7:11])
    #Find the occurance of 'hij' in the string
    hij_index = alphabet.index("hij")
    print(hij_index)
    # b. Extract every second letter starting from 'a' to 'm'.
    alphabet_segment = "abcdefghijklm" #index of substring
    result = alphabet_segment[::2]
    print(result)