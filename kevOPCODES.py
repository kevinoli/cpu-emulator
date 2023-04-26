# OPCODES
# LOAD OPERATIONS
# LD R1, 0xABCD     - 00 RR AB CD       # Load register with given value
# LD R1, R2         - 01 RR 00 RR       # Load register with other register
# LD R1, $0x100     - 02 RR 01 00       # Load 16 bit address into register
# LD R1, S0         - 03 RR 00 S0       # Load REgister with stack value
#
# STORE OPERATIONS
# ST R1, $0x100     - 10 RR 01 00       # 16 bit write
# ST R1, R2         - 11 RR 00 R2       # 16 bit write to address in register
#
# COMPARE OPERATIONS
# CMP R1, R2        - 20 RR 00 RR       # Compare register to register
# CMP R1, 0xABCD    - 21 RR ABCD        # Compare register with given value
#
# BRANCH/JUMP OPERATIONS
# BEQ label         - 30 00 AB CD       # Branch if equal flag is set
# BGT label         - 31 00 AB CD       # Branch if greater than flag is set
# BLT label         - 32 00 AB CD       # Branch if less than flag is set
# BRA label         - 33 00 ABCD        # Unconditional branch
#
# MATH OPERATIONS
# ADD R1, 0xABCD    - 40 RR ABCD        # Add given value to value in register
# SUB R1, 0xABCD    - 41 RR ABCD        # Subtract given value to value in register
# ADD R1, R2        - 42 RR 00 RR       # Add register value to register value
# SUB R1, R2        - 43 RR 00 RR       # Subtract register value to register value
# 
# STACK OPERATIONS
# PUSH R1           - 50 RR 00 00       # Push value in register to stack
# PUSH $0x100       - 51 00 AB CD       # Push value from memory to stack
# PUSH 0xABCD       - 52 00 AB CD       # Push given value to stack
# POP               - 60 00 00 00       # Pop whatever is at the top of the stack
#
# HALT OPERATIONS
# HALT              - FE FE FF FF       # Stop the program completly
#
# NO OPERATION
# NOOP              - FF FF FF FF       # No operation code inputed

