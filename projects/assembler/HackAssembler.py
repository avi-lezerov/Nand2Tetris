import os
import sys
from Parser import Parser
import Code
from SymbolTable import SymbolTable


class HackAssembler:
   
   
    def __init__(self, path):
        """
        Initializes the HackAssembler object and opens the input file/stream.

        Args:
            file (str): The name of the input file.
        """
        self.path = path
        temp = os.path.splitext(path)[0] + ".hack"
        directory = os.path.dirname(path)
        new_path = os.path.join(directory, temp)
    
        
        self._symbol_table = SymbolTable()
        self._address = 16
        self._output_file = open(new_path , "w")



    def _first_pass(self):
        """
        Adds all the labels to the symbol table.
        """
        p = Parser(self.path)
        while p.has_more_lines():
            p.next_line()
            if p.instruction_type() == "L_INSTRUCTION":
                self._symbol_table.add_entry(p.symbol(), p.get_line_number()+1) # +1 because the line of the next instruction
        p._close_file()


    def _second_pass(self):
        """
        Translates the assembly code to binary.
        """
        p = Parser(self.path)
        while p.has_more_lines():
            p.next_line()
            if p.instruction_type() == "C_INSTRUCTION":
                self._output_file.write(self.c_instruction(p))
            elif p.instruction_type() == "A_INSTRUCTION":
                self._output_file.write(self.a_instruction(p))
        p._close_file()
        self._output_file.close()


    def a_instruction(self, p: Parser):
        """
        returns the binary representation of the A instruction.

        Args:
            p (Parser): The parser object.

        Returns:
            str: The binary representation of the A instruction.
        """
        str = ""
        symbol = p.symbol()
        if self._symbol_table.contains(symbol):
            str = self._symbol_table.get_address(symbol)+ "\n"
        else:
            if symbol.isdigit():
                str = "0" + format(int(symbol), "015b") + "\n"
            else:
                self._symbol_table.add_entry(symbol, self._address)
                str = self._symbol_table.get_address(symbol)+ "\n"
                self._address += 1
        return str

    def c_instruction(self, p: Parser):
        """
        returns the binary representation of the C instruction.

        Args:
            p (Parser): The parser object.
        
        Returns:
            str: The binary representation of the C instruction.
        """
        return "111" + Code.comp(p.comp()) + Code.dest(p.dest()) + Code.jump(p.jump()) + "\n"
       
    def run(self):
        """
        Runs the HackAssembler by performing the two-pass assembly process.
        """
        self._first_pass()
        self._second_pass()