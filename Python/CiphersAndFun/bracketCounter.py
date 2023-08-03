# This is a bracket counting tool for CTF challenges
# It counts only pairs of a variety of brackets in a file
# provided by the user.
# ToDo:
# 1) Option: filename from stdin
# 2) Option: charList for different bracket-types stdin

# Setup
def __main__():
    brkFile = open('brackets.txt', 'r')
    bracketCounter(["[]"], brkFile)
    brkFile.close()

def bracketCounter(bracketType, brkFile):
    openBrk = 0
    closeBrk = 0
    result = f"The pairs of {bracketType} are "
    for brk in brkFile.read():
        # If clause for counting
        if brk == "[":
            openBrk += 1
        elif brk == "]":
            closeBrk += 1
        else:
            continue
        # Decide on result
    if openBrk <= closeBrk:
        result += str(openBrk)
    else:
        result += str(closeBrk)
    print(result)

if __name__ == __main__():
    main()
        




