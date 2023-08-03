# This is a bracket counting tool for CTF challenges
# It counts only pairs of a variety of brackets in a file
# provided by the user.
# ToDo:
# 1) Option: filename from stdin
# 2) Option: charList for different bracket-types stdin

# Setup
def __main__():
    brkFile = open('brackets.txt', 'r')
    bracketCounter(["[","]"], brkFile)
    brkFile.close()

def bracketCounter(bracketType, brkFile):
    brkDict = {}
    openBrk = 0
    closeBrk = 0
    result = ""
    for brkType in bracketType:
        brkDict[brkType:0]
    for brk in brkFile:
        for brkType in bracketType:
        # If clause for counting
            if brk == brkType:
                openBrk += 1

        closeBrk += 1

        # Decide on result
        if openBrk <= closeBrk:
            result.__add__(f"{openBrk}")
        else:
            result.__add__(f"{closeBrk}")
        




