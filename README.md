<!-- ABOUT THE PROJECT -->
# Central Processing Unit Emulator

## Project Outline

​​Design your own computer and instruction set.  It can be simple like MARIE but have your twist on OPCODES and why you chose them.  It should have a valid ISA, which means all the bits are defined in the machine code and how they are decoded.  You don't have to define all the logical circuits, just block diagrams, but you should define the micro-instructions or steps that each of your opcodes implements.  The ASM part could be an example program.   If it is more than 16 opcodes then you don't have to build an assembler and/or an emulator.  You can build an interpreter that reads the assembly code test and executes it directly.  The issue to handle is forward references, normally it's easier to make two passes over the code, the first to find the addresses (labels) and the second time to execute the code.  Using a fixed instruction size makes this easier.  See me if you need extra guidance.

* The project involved designing an emulation of a central processing unit (CPU) with a 16-bit architecture and an instruction set. The CPU had the ability to fetch and decode instructions, manipulate memory, stack, and registers, and perform basic arithmetic and logic operations. 
* The project included the development of an assembler to compile assembly code into machine code, and an emulator to execute the machine code which was then displayed through virtual memory. 
* The implementation was done in Python3 using Visual Studio Code and required defining an instruction set, designing an assembler, and developing a CPU emulator with control logic, a decoder, and a memory display function.

## Basic Design
1. Run assembler with assembly code file
   1. Take a file with assembly code and turn it into machine code and put it in a binary file
      1. Make one pass to find labels
      2. Make a pass to convert opcodes
2. Run the CPU emulator with the binary file
   1. Write the instructions to beginning of memory and start reading each instruction one by one
      1. Fetch each instruction from memory
      2. Decode the opcode and data
      3. Execute the instruction

## Assembler
1. Starts by clearing a binary file for the instructions to be written to
2. Read asm file and make a pass to find labels and write them to the binary file
3. Read asm file and make another pass to convert opcodes and write to binary file


## OPCode Conversion
1. Determine what operations needs to converted
2. Convert the instruction via the several operation functions
3. Write the conversion to the bin file


# Instruction Set Operation Codes
```asm
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
```

### Usage

To run program use run kevMAIN.py with python3 alongside kevASSEMBLER.py,kevCPUEMU.py and kevASM.asm

* Run:
   ```sh
   python3 kevMAIN.py
   ```
