import pygame

# Prints to game console with time refference.
def printToGameConsole(printMsg):
    # Print to console.
    consoleMsg = "[" + str(pygame.time.get_ticks()) + "]\t" + printMsg
    print(consoleMsg)

    # Print to log.
    try:
        logFile = open("console.log", "a")
        logFile.write(consoleMsg + "\n")
        logFile.close()
    except IOError:
        pass
