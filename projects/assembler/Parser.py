class Parser:
  
    def __init__(self, path):
        """
        Initializes the Parser object and opens the input file/stream.

        Args:
            file (str): The name of the input file.
        """
        self._line = "None"
        self.line_number = -1
        try:
            self._file = open(path, "r")  
        except:
            raise ValueError("Error: File not found.")
        
    def _close_file(self):
            """
            Closes the input file.
            """
            try:
                self._file.close()
            except:
                return

    def has_more_lines(self) -> bool:
        """
        Determines if there are more lines in the input file.

        Returns:
            bool: True if there are more lines in the input file, False otherwise.
        """
        return self._line != ''


    def next_line(self):
        """
        Reads the next line from the input file and makes it the current line.

        Returns:
            bool: True if the next line was read, False otherwise.
        """
        if self.has_more_lines():
            line = self._file.readline()
            temp = line.strip()

            # jamp comments or empty lines
            while temp.startswith("//") or line == '\n'  :
                line = self._file.readline()
                temp = line.strip()

            self._line = line.strip()
            if self.instruction_type() != "L_INSTRUCTION":
                self.line_number += 1
                
        else:
            self._close_file()

    def instruction_type(self):
        """
        Determines the type of instruction.

        Returns:
            str: The type of instruction. Possible values are "A_INSTRUCTION", "C_INSTRUCTION", or "L_INSTRUCTION".
        """
        type = None
        
        if self._line.startswith("@"):
            type = "A_INSTRUCTION"
        elif self._line.startswith("(") and self._line.endswith(")"):
            type = "L_INSTRUCTION"
        elif self._line != '' :
            type = "C_INSTRUCTION"

        return type

    def symbol(self):
        """
        Extracts the symbol from the current instruction.

        Returns:
            str: The symbol extracted from the instruction.
        """
        if self._line[0] == "@":
            return self._line[1:]
        elif self.instruction_type() == "L_INSTRUCTION":
            return self._line[1:-1]
        
    def dest(self):
        """ 
        Extracts the dest mnemonic from the current C-instruction.

        Returns:
            str: The dest mnemonic.
        """
        if self._is_C_INSTRUCTION() :
            if self._line[1] == ";":
                return None
            elif "=" in self._line:
                return self._line[:self._line.index("=")]
        
    def comp(self):
        """
        Extracts the comp mnemonic from the current C-instruction.

        Returns:
            str: The comp mnemonic.
        """
        comp = None
        if not self._is_C_INSTRUCTION():
            return comp
        
        if ";" in self._line and "=" in self._line:
            comp = self._line[self._line.index("=")+ 1:self._line.index(";")]
        elif "=" in self._line:
            comp = self._line[self._line.index("=")+ 1:]
        elif ";" ==  self._line[1]:
            comp = self._line[0] 
        return comp
            
                
    
    def jump(self):
        """
        Extracts the jump mnemonic from the current C-instruction.

        Returns:
            str: The jump mnemonic.
        """
        if self._is_C_INSTRUCTION() :
            if ";" in self._line:
                return self._line[self._line.index(";")+1:]
           

    def _is_C_INSTRUCTION(self):
        return self.instruction_type() == "C_INSTRUCTION"

    def get_line_number(self):
        return self.line_number