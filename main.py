code = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    " ": " ",
    "0": "_____",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____."
}


def convert_text_to_morse():
    text = input("what do you wanna say?  ").lower()

    for letter in text:
        final = []
        new_letter = code[letter]
        final.append(new_letter)

        for element in final:
            mores_code = ""
            mores_code += element

        print(mores_code)


end = False
while end == False:
    convert_text_to_morse()
    response = input("wanna convert more?? y or n??  ").lower()
    if response == "y":
        continue
    elif response == "n":
        end = True
        print("OK BYE")
