import os
import sys
from Parser import Parser
from translator import Translator



class VMtranslator:
   
   
    def __init__(self, path):
       
        self.path = path
        temp = os.path.splitext(path)[0] + ".asm"
        directory = os.path.dirname(path)
        new_path = os.path.join(directory, temp)
        self._output_file = open(new_path , "w")

        self.run()
        self._output_file.close()

    def run(self):
        """
        Runs the VMtranslator.
        """
        self.prosses_file()


    def prosses_file(self):
        """
        Processes the file and writes the output to the output file.
        """
        command_type = ""
        asm_list = []
        parser = Parser(self.path)
        asm_coder = Translator(os.path.basename(self.path)[:-3])
        while  parser.advance():
            self._output_file.write('//'+ parser.line)
            command_type = parser.command_type()
            if command_type == "C_ARITHMETIC":
                asm_list = asm_coder.arithmetic(parser.arg1())
            elif command_type == "C_BOOL":
                asm_list = asm_coder.boolean(parser.arg1())
            elif command_type == "C_PUSH":
                asm_list = asm_coder.push(parser.arg1(), parser.arg2())
            elif command_type == "C_POP":
                asm_list = asm_coder.pop(parser.arg1(), parser.arg2())
            self.write(asm_list)

    def write(self, asm_list: list):
        """
        Writes the given list to the output file.
        """
        for line in asm_list:
            self._output_file.write(line + '\n')