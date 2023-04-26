Central Processing Unit Emulator
The project involved designing an emulation of a central processing unit (CPU) with a 16-bit architecture and an instruction set. The CPU had the ability to fetch and decode instructions, manipulate memory, stack, and registers, and perform basic arithmetic and logic operations. 
The project included the development of an assembler to compile assembly code into machine code, and an emulator to execute the machine code which was then displayed through virtual memory. 
The implementation was done in Python3 using Visual Studio Code and required defining an instruction set, designing an assembler, and developing a CPU emulator with control logic, a decoder, and a memory display function.


Basic Design
Run assembler with assembly code file
Take a file with assembly code and turn it into machine code and put it in a binary file
Make one pass to find labels
Make a pass to convert opcodes


Run the CPU emulator with the binary file
Write the instructions to beginning of memory and start reading each instruction one by one
Fetch each instruction from memory
Decode the opcode and data
Execute the instruction

Assembler
Starts by clearing a binary file for the instructions to be written to
Read asm file and make a pass to find labels and write them to the binary file
Read asm file and make another pass to convert opcodes and write to binary file

OPCode Conversion
Determine what operations needs to converted
Convert the instruction via the several operation functions
Write the conversion to the bin file

OPCODES
LOAD OPERATIONS
LD R1, 0xABCD     - 00 RR AB CD       Load register with given value
LD R1, R2         - 01 RR 00 RR       Load register with other register
LD R1, $0x100     - 02 RR 01 00       Load 16 bit address into register
LD R1, S0         - 03 RR 00 S0       Load REgister with stack value
#
STORE OPERATIONS
ST R1, $0x100     - 10 RR 01 00       16 bit write
ST R1, R2         - 11 RR 00 R2       16 bit write to address in register
#
COMPARE OPERATIONS
CMP R1, R2        - 20 RR 00 RR       Compare register to register
CMP R1, 0xABCD    - 21 RR ABCD        Compare register with given value
#
BRANCH/JUMP OPERATIONS
BEQ label         - 30 00 AB CD       Branch if equal flag is set
BGT label         - 31 00 AB CD       Branch if greater than flag is set
BLT label         - 32 00 AB CD       Branch if less than flag is set
BRA label         - 33 00 ABCD        Unconditional branch
#
MATH OPERATIONS
ADD R1, 0xABCD    - 40 RR ABCD        Add given value to value in register
SUB R1, 0xABCD    - 41 RR ABCD        Subtract given value to value in register
ADD R1, R2        - 42 RR 00 RR       Add register value to register value
SUB R1, R2        - 43 RR 00 RR       Subtract register value to register value

STACK OPERATIONS
PUSH R1           - 50 RR 00 00       Push value in register to stack
PUSH $0x100       - 51 00 AB CD       Push value from memory to stack
PUSH 0xABCD       - 52 00 AB CD       Push given value to stack
POP               - 60 00 00 00       Pop whatever is at the top of the stack
#
HALT OPERATIONS
HALT              - FE FE FF FF       Stop the program completly
#
NO OPERATION
NOOP              - FF FF FF FF       No operation code inputed


