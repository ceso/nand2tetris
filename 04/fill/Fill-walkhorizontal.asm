// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
   
(KEYCHECK) // infinite loop listening for keyboard events
  @SCREEN
  D=A
  @addrscr
  M=D

  @KBD
  D=M
  
  @BLACK
  D;JGT // if scancode > 0 goto BLACK
 
  @WHITE
  D;JMP // else goto WHITE
  
(BLACK)
  @colour
  M=-1 // set draw color val. to black: -1 (1111111111111111)
  @DRAW
  0;JMP // goto DRAW

(WHITE)
  @colour
  M=0 // set draw color val. to white: 0 (0000000000000000)
  @DRAW
  0;JMP // goto DRAW

(DRAW)
  @addrscr
  D=M
  @KBD
  D=D-A
  @KEYCHECK
  D;JEQ // if scancode == 0 goto KEYCHECK

  @colour
  D=M
  @addrscr
  A=M
  M=D // assign colour to the current screen position
  @addrscr
  M=M+1 // move into the next position
  @DRAW
  0;JMP // goto DRAW
