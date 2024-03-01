import os
from Parser import Parser
from translator import Translator
from fileReader import FileReader

class VMtranslator:
    def __init__(self, path : str): 
        path  = path.replace(".vm", ".asm" )
        self._output_file = open(path , "w")

    def close_file(self):
        self._output_file.close()
        

    def prosses_file(self, path):
        """
        Processes the file and writes the output to the output file.
        """
        vm_lines = FileReader(path).get_file_content()
        parser_lines = Parser(vm_lines).get_file_content()
      
        file_name = os.path.basename(path)[:-3]

        self._output_file.write('\n//  ***** ' + file_name + ' ***** \n')
        
        asm_coder = Translator(file_name)

        for line in parser_lines:
            asm_list = []
            self._output_file.write('\n// ' + line[0] )
            command_type = line[1]
            if command_type == "C_ARITHMETIC":
                asm_list = asm_coder.arithmetic(line[2])
            elif command_type == "C_BOOL":
                asm_list = asm_coder.boolean(line[2])
            elif command_type == "C_PUSH":
                asm_list = asm_coder.push(line[2], line[3])
            elif command_type == "C_POP":
                asm_list = asm_coder.pop(line[2], line[3])
            for line in asm_list:
                self._output_file.write(line + '\n')