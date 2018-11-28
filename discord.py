#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from os import system, name
import unicodedata

POLISH_CHARACTERS = {
    50309:'a',50311:'c',50329:'e',50562:'l',50564:'n',50099:'o',50587:'s',50618:'z',50620:'z',
    50308:'A',50310:'C',50328:'E',50561:'L',50563:'N',50067:'O',50586:'S',50617:'Z',50619:'Z',}

def encodePL(text):
    nrmtxt = unicodedata.normalize('NFC',text)
    i = 0
    ret_str = []
    while i < len(nrmtxt):
        if ord(text[i])>128: # non ASCII character
            fbyte = ord(text[i])
            sbyte = ord(text[i+1])
            lkey = (fbyte << 8) + sbyte
            ret_str.append(POLISH_CHARACTERS.get(lkey))
            i = i+1
        else: # pure ASCII character
            ret_str.append(text[i])
        i = i+1
    return ' '.join(ret_str)


def writeMessage():
    messages = []
    while True:
        message = input("Wpisz wiadomość lub naciśnij ENTER aby zakończyć: ")
        if message == "":
            break
        message = encodePL(message)
        messages.append(message.lower())
    return messages


def change(messages):
    newMessage = []
    l = 0

    for line in messages:
        lineNewMessage = ""
        for mark in line:
            if mark == ' ':
                lineNewMessage += "    "
                continue
            lineNewMessage += " :regional_indicator_" + mark + ":"
            # lineNewMessage += mark
        newMessage.append(lineNewMessage)
        l += 1
    return newMessage


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def displaysMessage(newMessage):
    clear()
    for line in newMessage:
        print(line)


while True:
    displaysMessage(change(writeMessage()))
    end = input()
    if end == "":
        continue
