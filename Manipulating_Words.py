def Manipulating_Words():
    info = "Python is fine. Fun is good. Good is subjective"
    finds_index = info.index("subjective")
    # a. Extract the word 'subjective' without knowing its exact position.
    print(finds_index)
    # b. Extract every third word.
    every_third_word= info.split()[::3]