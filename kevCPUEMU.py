# -----------------------------------------------------------------------------
# Initaliztion of faux memory, stack, registers, and flags
# -----------------------------------------------------------------------------
pc = 0
# Runtime flags
# Change to true if you want more imformation
showMemory = False
showMemoryStream = False
showMachine = False
# Registers
registers = [1,2,3,4,5,6,7,8]
# Memory using byte array with 64kb
main_memory = bytearray(65535)
starting_address = 0xFBFF
# Compare flaggs
flag_eq = 0
flag_gt = 0
flag_lt = 0
# Stack
stack = list()

# -----------------------------------------------------------------------------
# Displays the last 64 bits of memory starting at address 0xFFBF
# -----------------------------------------------------------------------------
def displayMemory():
    x = 0
    cur = starting_address
    end = starting_address + 64
    while cur < end:
        line = ""
        while x < 32:
            c = main_memory[cur] & 0xFF
            if c < 32: # non-printable characters
                line = line + " "
            else:
                line = line + str(chr(c))
            x = x + 1
            cur = cur + 1
        print(line)
        x = 0

# -----------------------------------------------------------------------------
# Decodes the opcodes from binary code and executes instructions
# The opcode is the first byte or op, the register is the second byte or 'mode'.
# The last two bytes are the data or address (depending on the opcode)
# -----------------------------------------------------------------------------
def decode(pc, opcode, data):
    global flag_eq, flag_gt, flag_lt, main_memory, registers
    op = opcode >> 8
    mode = opcode & 0xFF
    if op == 0x00: registers[mode] = data                           # LD data to register
    elif op == 0x01: registers[mode] = registers[data & 0xFF]       # LD from register
    elif op == 0x02: registers[mode] = main_memory[data]            # LD from memory
    elif op == 0x03: registers[mode] = stack[(data + 1)*(-1)]       # LD from stack
    elif op == 0x10: main_memory[data] = registers[mode]            # ST to memory from reg
    elif op == 0x11: main_memory[registers[data]] = registers[mode] # ST 16 bit write to addr in second reg
    elif op == 0x20:                                                # CMP R1, R2
        if registers[mode] == registers[data & 0xFF]: flag_eq = 1   # If equal set flag to 1
        elif registers[mode] > registers[data & 0xFF]: flag_gt = 1  # If greater than set flag to 1
        elif registers[mode] < registers[data & 0xFF]: flag_lt = 1  # If less than set flag to 1
    elif op == 0x21:                                                # CMP R1, 0xABCD
        if registers[mode] == data: flag_eq = 1
        elif registers[mode] > data: flag_gt = 1
        elif registers[mode] < data: flag_lt = 1
    elif op == 0x30:                    # BEQ label - 30 00 AB CD # If Z flag is set
        if flag_eq == 1: pc = data
    elif op == 0x31:                    # BGT label - 31 00 AB CD # If GT flag is set
        if flag_gt == 1: pc = data
    elif op == 0x32:                    # BLT label - 32 00 AB CD # If LT flag is set
        if flag_lt == 1: pc = data
    elif op == 0x33:  pc = data         # BRA label
    elif op == 0x40: registers[mode] = (registers[mode] + data) & 0xFFFF                    # ADD R1, 0xABCD - 40 RR AB CD
    elif op == 0x41: registers[mode] = (registers[mode] - data) & 0xFFFF                    # SUB R1, 0xABCD - 41 RR AB CD
    elif op == 0x42: registers[mode] = (registers[mode] + registers[data & 0xFF]) & 0xFFFF  # ADD R1, R2 - 40 RR 00 RR
    elif op == 0x43: registers[mode] = (registers[mode] - registers[data & 0xFF]) & 0xFFFF  # SUB R1, R2 - 41 RR AB CD
    elif op == 0x50: stack.append(registers[mode])          # PUSH from register
    elif op == 0x51: stack.append(main_memory[data])        # PUSH from memory
    elif op == 0x52: stack.append(data)                     # PUSH from value
    elif op == 0x60: stack.pop()                            # POP element from stack
    elif op == 0xFE: pc = 0xFFFF                            # HALT - Jump to end of memory
    elif op != 0xFF:    # NOOP
        print("ILLEGAL OP CODE")
        exit(0)
    return pc

# -----------------------------------------------------------------------------
# Emulation on a CPU using the pre-initailized memory, stack, registers, and
# flags. Pulling from the file kevASM.asm and assembleing it into a binary file
# then decoding each line and performing accordingly.
# -----------------------------------------------------------------------------
def cpuEmulator(file):
    # Initialize values
    global pc, showMachine, showMemory, showMemoryStream
    
    # Open kevMC.bin for reading can copying
    with open(file, mode='rb') as file:
        code = bytearray(file.read())
        
    # Copy instructions into begining of memory
    line= list()
    decision = input("Would you like to see the machine code? (y/n) ")
    if decision.upper() == 'Y':
        showMachine = True
    for count in range(len(code)):
        main_memory[count] = code[count]
        # If you want to print the instruction hex code uncomment
        if showMachine == True:
            if count%4==3:
                line.append(hex(code[count]))
                print(line)
                line.clear()
            else:
                line.append(hex(code[count]))

    # Begin CPU emulations
    print("\nExecution-------------------------")
    print("Running CPU emulation....")
    decision = input("Would you like to see the memory as the program runs? (y/n) ")
    if decision.upper() == 'Y':
        showMemoryStream = True
    if showMemoryStream == True: 
        print("Printing memory as CPU runs....")
        
    while pc < len(code):
        # Fetches the instruction from beinging of memory
        byte1 = main_memory[pc] << 8 | main_memory[pc+1]
        byte2 = main_memory[pc+2] << 8 | main_memory[pc+3]
        # Decodes the instruction and executes accordingly
        pc = decode(pc + 4, byte1, byte2)
        
        # Prints memory each time somthing is stored in memory
        # Only if showMemory is ture
        if showMemoryStream == True:
            if((str(hex(byte1 >> 8))[2])=='1'):
                displayMemory()
    decision = input("Would you like to see the final memory output? (y/n) ")
    if decision.upper() == 'Y':
        showMemory = True
    if showMemory == True:
        print("Printing data saved into memmory....")
        displayMemory()
    print("done.")
