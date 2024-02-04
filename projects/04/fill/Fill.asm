// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.
(INPUT)
    @screen_val
    M=-1 
    @KBD
    D=M      
    @INS
    D;JNE   
    @screen_val
    M=0
    @INS
    0;JMP    
(INS)
    @SCREEN
    D=A
    @screen
    M=D
    @8192
    D=A
    @i
    M=D
    @LOOP
    0;JMP      
(LOOP)
    @i
    D=M      
    @INPUT
    D;JLE    
    @screen_val
    D=M      
    @screen
    A=M      
    M=D     
    @screen
    M=M+1 
    @i
    M=M-1    
    @LOOP
    0;JMP   