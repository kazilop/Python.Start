# Пример использования !
#cprint("Пример")
#cprint("test", "blue")
#cprint("test2", "red", "bg_blue", "bold")
#cprint("test2", "purple", "under")


def cprint(text, *args):

    color = ""
    style = ""
    bg_color = ""
    newtext = text

    if len(args) == 2:
        if args[0].lower() == "red":
            color = "31"
        if args[0].lower() == "green":
            color = "32"
        if args[0].lower() == "yellow":
            color = "33"
        if args[0].lower() == "blue":
            color = "34"
        if args[0].lower() == "purple":
            color = "35"
        if args[0].lower() == "cyan":
            color = "36"
        if args[0].lower() == "grey":
            color = "37"
        if args[0].lower() == "white":
            color = "38"

        if args[1] == "bold":
            style = "1;"
        if args[1].lower() == "bg_black":
            bg_color = ";40"
        if args[1].lower() == "bg_red":
            bg_color = ";41"
        if args[1].lower() == "bg_green":
            bg_color = ";42"
        if args[1].lower() == "bg_yellow":
            bg_color = ";43"
        if args[1].lower() == "bg_blue":
            bg_color = ";44"
        if args[1].lower() == "bg_purple":
            bg_color = ";45"
        if args[1].lower() == "bg_cyan":
            bg_color = ";46"
        if args[1].lower() == "bg_white":
            bg_color = ";47"

        if args[1] == "bold":
            style = "1;"
        if args[1] == "norm":
            style = "0;"
        if args[1] == "under":
            style = "4;"

        newtext = f'\x1b[{style}{color}{bg_color}m{text}\x1b[0m'

    if len(args) == 1:
        #color = args[0]
        if args[0].lower() == "red":
            color = "31"
        if args[0].lower() == "green":
            color = "32"
        if args[0].lower() == "yellow":
            color = "33"
        if args[0].lower() == "blue":
            color = "34"
        if args[0].lower() == "purple":
            color = "35"
        if args[0].lower() == "cyan":
            color = "36"
        if args[0].lower() == "grey":
            color = "37"
        if args[0].lower() == "white":
            color = "38"
        newtext = f'\x1b[{color}m{text}\x1b[0m'

    if len(args) == 3:
        if args[2] == "bold":
            style = "1;"
        if args[2] == "norm":
            style = "0;"
        if args[2] == "under":
            style = "4;"

        if args[1] == "bold":
            style = "1;"
        if args[1].lower() == "bg_black":
            bg_color = ";40"
        if args[1].lower() == "bg_red":
            bg_color = ";41"
        if args[1].lower() == "bg_green":
            bg_color = ";42"
        if args[1].lower() == "bg_yellow":
            bg_color = ";43"
        if args[1].lower() == "bg_blue":
            bg_color = ";44"
        if args[1].lower() == "bg_purple":
            bg_color = ";45"
        if args[1].lower() == "bg_cyan":
            bg_color = ";46"
        if args[1].lower() == "bg_white":
            bg_color = ";47"

        if args[1] == "bold":
            style = "1;"
        if args[1] == "norm":
            style = "0;"
        if args[1] == "under":
            style = "4;"

        if args[0].lower() == "black":
            color = "30"

        if args[0].lower() == "red":
            color = "31"
        if args[0].lower() == "green":
            color = "32"
        if args[0].lower() == "yellow":
            color = "33"
        if args[0].lower() == "blue":
            color = "34"
        if args[0].lower() == "purple":
            color = "35"
        if args[0].lower() == "cyan":
            color = "36"
        if args[0].lower() == "grey":
            color = "37"
        if args[0].lower() == "white":
            color = "38"

        if args[1] == "bold":
            style = "1;"
        if args[1].lower() == "bg_black":
            bg_color = ";40"
        if args[1].lower() == "bg_red":
            bg_color = ";41"
        if args[1].lower() == "bg_green":
            bg_color = ";42"
        if args[1].lower() == "bg_yellow":
            bg_color = ";43"
        if args[1].lower() == "bg_blue":
            bg_color = ";44"
        if args[1].lower() == "bg_purple":
            bg_color = ";45"
        if args[1].lower() == "bg_cyan":
            bg_color = ";46"
        if args[1].lower() == "bg_white":
            bg_color = ";47"

        if args[1] == "bold":
            style = "1;"
        if args[1] == "norm":
            style = "0;"
        if args[1] == "under":
            style = "4;"

        newtext = f'\x1b[{style}{color}{bg_color}m{text}\x1b[0m'

    print(newtext)
    return True


