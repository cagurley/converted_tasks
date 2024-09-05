"""
Function module
"""

import datetime as dt
import os


def plog(log, line):
    try:
        with open(log, 'a') as f:
            line += '\n'
            f.write(line)
        print(line)
    except IOError:
        print('LOG FILE SHOULD NOT BE IN USE WHILE AGENT IS RUNNING. OPERATION HAS NOT BEEN LOGGED. TERMINATE AGENT BEFORE VIEWING.')


def get_now():
    return dt.datetime.now().astimezone()

def get_now_str():
    return get_now().strftime("%c")


def convert_dt_str(s):
    return dt.datetime.strptime(s, "%c")


def clear():
    return os.system("cls" if os.name == "nt" else "clear")
