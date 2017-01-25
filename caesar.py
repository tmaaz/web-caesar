import string
import sys
from sys import argv


def rotate_character(char, rot):
    if char.isalpha():
        if char.isupper():
            myCase = True
            char = char.lower()
        else:
            myCase = False
        newCode = alphabet_position(char)
        tempAlpha = (int(newCode) + int(rot))
        newAlpha = (tempAlpha % 26)
        new_alpha = (string.ascii_lowercase[newAlpha - 1])
        if myCase == True:
            new_alpha = new_alpha.upper()
    else:
        new_alpha = char
    return new_alpha


def alphabet_position(letter):
    if letter.isupper():
        myCodeA = ord(letter) - 64
    else:
        myCodeA = ord(letter) - 96
    return myCodeA


def encrypt(text, rot):
    newText = ""
    for x in range(len(text)):
        letter = text[x]
        new_alpha = rotate_character(letter, rot)
        newText = newText + new_alpha
    return newText
