import os
from Parser import Parser
from translator import Translator

class VMtranslator:

    def __init__(self, path : str): 
        path  = path.replace(".vm", ".asm" )
        self._output_file = open(path , "w")

        

    def prosses_file(self, path):
        """
        Processes the file and writes the output to the output file.
        """
        command_type = ""
        asm_list = []
        parser = Parser(path)
        asm_coder = Translator(os.path.basename(path)[:-3])
        while  parser.advance():
            self._output_file.write('// '+ parser.line)
            command_type = parser.command_type()
            if command_type == "C_ARITHMETIC":
                asm_list = asm_coder.arithmetic(parser.arg1())
            elif command_type == "C_BOOL":
                asm_list = asm_coder.boolean(parser.arg1())
            elif command_type == "C_PUSH":
                asm_list = asm_coder.push(parser.arg1(), parser.arg2())
            elif command_type == "C_POP":
                asm_list = asm_coder.pop(parser.arg1(), parser.arg2())
            for line in asm_list:
                self._output_file.write(line + '\n')
            