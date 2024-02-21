class Parser:
  
    def __init__(self, path):
        """
        Initializes the Parser object and opens the input file/stream.

        Args:
            file (str): The name of the input file.
        """
        try:
            self.file = open(path, "r")  
        except:
            raise ValueError("Error: File not found.")
        
        self.next_line = self.file.readline()
        self.line = "None"
        self.command = "None"
        self.dic= self.dictionary()
        
        
    def _close_file(self):
            """
            Closes the input file.
            """
            try :
               self.file.close()
            except:
                raise ValueError("Error: File not found.")
    
    def advance(self):
        self.command = self.next_line.split()

        while self.next_line == '' or self.next_line == '\n' or  (self.dic.get(self.command[0]) == None ):
            if self.next_line == '':
                self.command = ''
                self._close_file()
                return False
            self.next_line = self.file.readline()
            self.command = self.next_line.split()
            
        self.line = self.next_line
        self.command.insert(0, self.dic[self.command[0]])
        self.next_line = self.file.readline()
        return True

       

    def command_type(self) -> str:
            return self.command[0]
        
    
    def arg1(self) -> str:
        if self.command[0] == "C_ARITHMETIC" or self.command[0] == "C_BOOL":
            return self.command[1]
        else:
            return self.command[2]


    def arg2(self) -> int:
        if self.command[0] == "C_PUSH" or self.command[0] == "C_POP" or self.command[0] == "C_FUNCTION" or self.command[0] == "C_CALL":
            return self.command[3]
        

            


    def dictionary(self):
        return  {
                "pop" : "C_POP", 
                "push" : "C_PUSH",
                "add" : "C_ARITHMETIC",
                "sub" : "C_ARITHMETIC",
                "neg" : "C_ARITHMETIC",
                "and" : "C_ARITHMETIC",
                "or" : "C_ARITHMETIC",
                "not" : "C_ARITHMETIC",
                "eq" : "C_BOOL",
                "gt" : "C_BOOL",
                "lt" : "C_BOOL",
                "goto" : "C_GOTO",
                "if-goto" : "C_IF",
                "function" : "C_FUNCTION",
                "return" : "C_RETURN",
                "call" : "C_CALL"
            }