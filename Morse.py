# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Morse:
    def __init__(self, text):
        self.matrix = [[]]
        self.text = text
    
    def letter_to_morse(self, letter):
        morse = {"a":[["."],["_"]], "b":[["_"],["."],["."],["."]], "c":[["_"],["."],["_"],["."]], \
                 "d":[["_"],["."],["."]], "e":[["."]], "f":[["."],["."],["_"],["."]], \
                 "g":[["_"],["_"],["."]], "h":[["."],["."],["."],["."]], "i":[["."],["."]], \
                 "j":[["."],["_"],["_"],["_"]], "k":[["_"],["."],["_"]], "l":[["."],["_"],["."],["."]], \
                 "m":[["_"],["_"]], "n":[["_"],["."]], "o":[["."],["."],["."]], \
                 "p":[["."],["_"],["_"],["."]], "q":[["_"],["_"],["."],["_"]], "r":[["."],["_"],["."]], \
                 "s":[["_"],["_"],["_"]], "t":[["_"]], "u":[["."],["."],["_"]], \
                 "v":[["."],["."],["."],["_"]], "w":[["."],["_"],["_"]], "x":[["_"],["."],["."],["_"]], \
                 "y":[["_"],["."],["_"],["_"]], "z":[["_"],["_"],["."],["."]], " ":[["/"]]}
        return morse[letter]

    def create_matrix(self):
        line = 0
        for i in self.text:
            if i == "\n":
                self.matrix[line].pop(-1)
                self.matrix.append([])
                line += 1
            elif i.isalpha():
                for j in self.letter_to_morse(i):
                    self.matrix[line].append(j)
                    self.matrix[line].append([" "])
                # self.matrix[line].extend(self.letter_to_morse(i))
                self.matrix[line].pop(-1)
                self.matrix[line].extend([["   "]])
            else:
                self.matrix[line].pop(-1)
                self.matrix[line].extend(self.letter_to_morse(" "))
        self.matrix[line].pop(-1)
        return self.matrix

    def process_matrix(self):
        maximum = -1
        for i in range(len(self.matrix)):
            temp = len(self.matrix[i])
            if temp >= maximum:
                maximum = temp
        for i in range(len(self.matrix)):
            while len(self.matrix[i]) < maximum:
                self.matrix[i].append([" "])
        return self.matrix
    
    def process_text(self):
        self.text = self.text.lower
        return self.text

    def __str__(self):
        display = ""
        for i in self.matrix:
            for j in i:
                display += str(j[0])
            display += "\n"
        return display

class Text:
    def __init__(self, encoded):
        self.text = ""
        self.encoded = encoded
    
    def morse_to_letter(self, code):
        morse = {"a":[["."],["_"]], "b":[["_"],["."],["."],["."]], "c":[["_"],["."],["_"],["."]], \
                 "d":[["_"],["."],["."]], "e":[["."]], "f":[["."],["."],["_"],["."]], \
                 "g":[["_"],["_"],["."]], "h":[["."],["."],["."],["."]], "i":[["."],["."]], \
                 "j":[["."],["_"],["_"],["_"]], "k":[["_"],["."],["_"]], "l":[["."],["_"],["."],["."]], \
                 "m":[["_"],["_"]], "n":[["_"],["."]], "o":[["."],["."],["."]], \
                 "p":[["."],["_"],["_"],["."]], "q":[["_"],["_"],["."],["_"]], "r":[["."],["_"],["."]], \
                 "s":[["_"],["_"],["_"]], "t":[["_"]], "u":[["."],["."],["_"]], \
                 "v":[["."],["."],["."],["_"]], "w":[["."],["_"],["_"]], "x":[["_"],["."],["."],["_"]], \
                 "y":[["_"],["."],["_"],["_"]], "z":[["_"],["_"],["."],["."]], " ":[["/"]]}
        for letter in morse.keys():
            if code == morse[letter]:
                return letter
    
    def decode(self):
        temp = []
        index = 0
        while index <= len(self.encoded) - 1:
            sign = self.encoded[index]
            if sign == "/":
                self.text += self.morse_to_letter(temp)
                self.text += " "
                temp = []
            elif sign != " ":
                if temp:
                    if temp[-1] == [" "]:
                        temp.pop(-1)
                temp.append([sign])
            else:
                if not temp:
                    pass
                elif temp[-1] == [" "]:
                    temp.pop(-1)
                    self.text += self.morse_to_letter(temp)
                    temp = []
                else:
                    temp.append([sign])
            index += 1
        self.text += self.morse_to_letter(temp)
        return self.text
    
    def __str__(self):
        display = self.text
        display += "\n"
        return display

# sampletext1 = "a rose by any other name would smell as sweet" #sample text
# sampletext2 = "were a rose to be named something else\nit would still smell as sweet\nstill have thorns\nand still be a thing of fragile beauty"
# samplecode = ". _/. _ .   . . .   _ _ _   ./_ . . .   _ . _ _/. _   _ .   _ . _ _/. . .   _   . . . .   .   . _ ./_ .   . _   _ _   ./. _ _   . . .   . . _   . _ . .   _ . ./_ _ _   _ _   .   . _ . .   . _ . ./. _   _ _ _/_ _ _   . _ _   .   .   _"

function = int(input("Type in 1 for text to morse, 2 for morse to text: "))
while function != -1:
    print()
    if function == 1:
        text = input("Please enter your text to be traslated into morse code, use 'slash n' between lines: \n")
        a = Morse(text)
        a.create_matrix()
        print()
        print("Morse code:")
        print(a)
    elif function == 2:
        code = input("Please enter your morse code to be translated into text, use ' ' between dash/dot, '   ' between letter, and '/' between words: \n")
        b = Text(code)
        b.decode()
        print()
        print("Text: ")
        print(b)
    else:
        print("Invalid function.")
    print("Type -1 to quit the program.")
    function = int(input("Type in 1 for text to morse, 2 for morse to text: "))