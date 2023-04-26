import re
showAssemble = False
# -----------------------------------------------------------------------------
# Each OP code type is categoried so that it can sort between different 
# instructions with differnt paremeters. Each OP code has a functions that is
# refrenced in convertOPs() and puts each instruction into a binary file
# -----------------------------------------------------------------------------
def load(code):
    r = int(code[1].upper()[1])
    # Determine if register is valid
    if r >= 0 and r <= 7:
        a1 = code[2]
        # Figure out which load opereration to assebmle
        if   a1[0] == 'R':  writeBin("kevMC.bin", [0x01, r, 0, (int(a1[1:], 0))])                               # Register
        elif a1[0] == '$':  writeBin("kevMC.bin", [0x02, r, (int(a1[1:], 0)) >> 8, (int(a1[1:], 0)) & 0xFF])    # Address
        elif a1[0] == 'S':  writeBin("kevMC.bin", [0x03, r, 0, (int(a1[1:], 0))])                               # Stack
        else:               writeBin("kevMC.bin", [0x00, r, (int(a1, 0)) >> 8, (int(a1, 0)) & 0xFF])            # Value
    else:
        # Register Error Message
        print("Invalid register name",str(code[1].upper()))
        exit()

def store(code):
    r = int(code[1].upper()[1])
    # Determine if register is valid
    if r >= 0 and r <= 7:
        a1 = code[2]
        # Figure out which store opereration to assebmle
        if a1[0] == '$':    writeBin("kevMC.bin", [0x10, r, (int(a1[1:], 0)) >> 8, (int(a1[1:], 0)) & 0xFF]) # Address
        elif a1[0] == 'R':  writeBin("kevMC.bin", [0x11, r, 0, (int(a1[1:], 0))]) # Address in register
        else:
            print("Invalid mode")
            exit()
    else:
        # Register Error Message
        print("Invalid register name",str(code[1].upper()))
        exit()
        
def compare(code):
    r = int(code[1].upper()[1])
    # Determine if register is valid
    if r >= 0 and r <= 7:
        a1 = code[2]
        # Figure out which compare opereration to assebmle
        if a1[0] == 'R': writeBin("kevMC.bin", [0x20, r, 0, (int(a1[1:], 0))]) # Register
        else: writeBin("kevMC.bin", [0x21, r, (int(a1, 0)) >> 8, (int(a1, 0)) & 0xFF]) # Value
    else:
        # Register error message
        print("Invalid register name",str(code[1].upper()))
        exit()

def branch(code):
    # Check that given label is valid
    if code[1] in labels:
        # Determine which break operation to asseble
        if code[0].upper() == "BEQ": writeBin("kevMC.bin", [0x30, 0, (labels[code[1]]) >> 8, (labels[code[1]]) & 0xFF])     # If equal
        elif code[0].upper() == "BGT": writeBin("kevMC.bin", [0x31, 0, (labels[code[1]]) >> 8, (labels[code[1]]) & 0xFF])   # If greater than
        elif code[0].upper() == "BLT": writeBin("kevMC.bin", [0x32, 0, (labels[code[1]]) >> 8, (labels[code[1]]) & 0xFF])   # If less than
        elif code[0].upper() == "BRA": writeBin("kevMC.bin", [0x33, 0, (labels[code[1]]) >> 8, (labels[code[1]]) & 0xFF])   # Always
    else:
        # Label error message
        print("Unknown label", (code[1]))
        exit()

def add(code):
    r = int(code[1].upper()[1])
    # Determine if register is valid
    if r >= 0 and r <= 7:
        a1 = code[2]
        # Figure out which addition opereration to assebmle
        if a1[0] == 'R': writeBin("kevMC.bin", [0x42, r, 0, (int(a1[1:], 0))]) # Register
        else: writeBin("kevMC.bin", [0x40, r, (int(a1, 0)) >> 8, (int(a1, 0)) & 0xFF]) # Value
    else:
        # Register error message
        print("Invalid register name", (code[1].upper()))
        exit()
        
def sub(code):
    r = int(code[1].upper()[1])
    # Determine if register is valid
    if r >= 0 and r <= 7:
        a1 = code[2]
        # Figure out which subtraction opereration to assebmle
        if a1[0] == 'R': writeBin("kevMC.bin", [0x43, r, 0, (int(a1[1:], 0))]) # Register
        else: writeBin("kevMC.bin", [0x41, r, (int(a1, 0)) >> 8, (int(a1, 0)) & 0xFF]) # Value
    else:
        # Error regester message
        print("Invalid register name", (code[1].upper()))
        exit()
        
def push(code):
    a1 = code[1]
    # Determine what value is going to pushed onto the stack and convert it
    if a1[0] == 'R': writeBin("kevMC.bin", [0x50, (int(a1[1:], 0)), 00, 00]) # Register
    elif a1[0] == '$': writeBin("kevMC.bin", [0x51, 0, (int(a1[1:], 0)) >> 8, (int(a1[1:], 0)) & 0xFF]) # Address
    elif a1.isdigit(): writeBin("kevMC.bin", [0x52, 0, (int(a1, 0)) >> 8, (int(a1, 0)) & 0xFF]) # Value
    else:
        # Value error message
        print("Invalid push value", (code[1].upper()))
        exit()
def pop():
    writeBin("kevMC.bin", [0x60, 0, 0, 0])
    
def halt():
    writeBin("kevMC.bin", [0xFE, 0xFE, 0xFF, 0xFF])
    
def noop():
    writeBin("kevMC.bin", [0xFF, 0xFF, 0xFF, 0xFF])
    
# -----------------------------------------------------------------------------
# Converts each line of code from kevASM.asm using a predefined ISA into binary
# using the different conversion functions and the writeBin() function
# -----------------------------------------------------------------------------
def convertOPs(file):
    for line in file:
        # Ignore labels and comments
        if line[0]=='.' or line[0]==';': continue
        line = line.replace('\n', '').replace('\r', '')
        code = re.split(r'[, ]',line)
        if '' in code: code.remove('')
        code[0].upper()
        if showAssemble == True: print(str(code))
        #print(str(code))
        # write to binary file by opcodes
        if code[0] == "LD":             load(code)      # load opcode
        elif code[0] == "ST":           store(code)     # different storre opcodes
        elif code[0] == "CMP":          compare(code)   # compare opcode
        elif (code[0])[0] == 'B':       branch(code)    # any branch opcodes
        elif code[0] == "ADD":          add(code)       # add opcodes
        elif code[0] == "SUB":          sub(code)       # sub opcode
        elif code[0] == "PUSH":         push(code)      # push opcodes
        elif code[0] == "POP":          pop()           # pop opcode
        elif code[0] == "HALT":         halt()          # halt opcode
        elif code[0] == "NOOP":         noop()          # no opcode
        else: # any opcode that isnt recognized will end the program
            print("Unknown operand \n",str(code[0]))
            exit()

# -----------------------------------------------------------------------------
# The first pass of the assembler through kevASM.asm to find labels that are 
# marked with '.' and ignore comments that are notated with a ';'
# -----------------------------------------------------------------------------
labels = {}
def parseLabels(file):
    linenum = 0
    for line in file:
        line = line.replace('\n', '').replace('\r', '')
        if line[0]==';': continue       # Comment    
        if line[0]=='.':                # Labels
            labels[line[1:]] = linenum*4
            if showAssemble == True: print ("Label: " + line[1:] + " @ " + format(linenum*4, '#04x'))
        else:
            linenum+= 1

# -----------------------------------------------------------------------------
# Takes binary input and puts it into a bytearray that is stored in kevMC.bin
# -----------------------------------------------------------------------------
def writeBin(bin, b):
    with open(bin, "ab") as binary_file: binary_file.write(bytearray(b))

# -----------------------------------------------------------------------------
# Assembly functin that clears the binary file kevMC.bin and takes the file 
# kevASM.asm and assembles it into a the binary file. It begins with one pass 
# using the parseLabels function to get the address of the labels and another 
# pass to convert the operation codes defined in the kevOPCODES.py file
# -----------------------------------------------------------------------------
def assemble(file):
    global labels, showAssemble
    # Open bin file in writte mode to clear the contents to prepare for writing
    with open('kevMC.bin', "wb") as binary_file: binary_file.close()
    decision = input("Would you like to see the code being assembled? (y/n) ")
    if decision.upper() == 'Y':
        showAssemble = True
    # Make pass once to get address of each label
    parseLabels(open(file))
    # Make another pass ignoring labels and convertiong OP codes
    convertOPs(open(file))
    return

