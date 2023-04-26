; ----------------------------------------------------
; start is written as teh starting label label
.start
; ----------------------------------------------------
; load register 1 with address 0xFBFF
LD R1, 0xFBFF
; ----------------------------------------------------
; set register 2 to the ascii value for H E L and O 
; and stores it in memory
; H
LD R2, 72
; store the value of register 2 (the character) to the 
; regester 1 (starting memor address
ST R2, R1
; move memory address 1 up
ADD R1, 1
; ----------------------------------------------------
; Rinse and repeat
; E
LD R2, 101
ST R2, R1
ADD R1, 1
; L
LD R2, 108
ST R2, R1
ADD R1, 1
; L
LD R2, 108
ST R2, R1
ADD R1, 1
; O
LD R2, 111
ST R2, R1
; ----------------------------------------------------
; Pushes the caracters for WORLD onto the stack backwards
; d
PUSH 100
; l
PUSH 108
; r
PUSH 114
; o
PUSH 111
; W
PUSH 87
; Space
PUSH 32
; ----------------------------------------------------
; loop to print from stack
; use register 3 as counter and set 6
LD R3, 0
; loop label
.worldloop
; move up memory address         
ADD R1, 1
; add one to counter       
ADD R3, 1
; load value at the top of the stack to register 4       
LD R2, S0
; store register 
ST R2, R1
; pop value at the top of stack off the stack       
POP
; loop 6 times
CMP R3, 6
; when register reaches 6 branch to end       
BEQ end
; branch always to loop label             
BRA worldloop
; ending label
.end