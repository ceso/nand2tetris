// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// pseudo code
//  n = R0
//  i = 1
//  prod = 0
//
//LOOP:
//  if i > n goto STOP
//    prod = prod + R1
//    i = i + 1
//    goto LOOP
//END:
//  R2 = prod  

@R0
D=M
@n
M=D // n = R0
@i
M=1  // i = 0
@prod
M=0 // prod = 0

(LOOP)
  @i
  D=M
  @n
  D=D-M // i = i - n
  @STOP
  D;JGT // if i > n goto STOP
    @prod
    D=M
    @R1
    D=D+M 
    @prod
    M=D // prod = prod + R1
    @i
    M=M+1 // i = i + 1
    @LOOP
    0;JMP

(STOP)
  @prod
  D=M
  @R2
  M=D // RAM[2] = prod

(END)
  @END
  0;JMP
