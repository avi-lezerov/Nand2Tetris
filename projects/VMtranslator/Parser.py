class Parser:
  
    def __init__(self, file_lines ):
        self.line = "None"
        self.command = "None"
        self.dic = self.dictionary()
        self.file_lines = file_lines
 

    def get_file_content(self):
        list = []
        for line in self.file_lines:
            sigle_line = []
            sigle_line.append(line)
            line = line.split()
            sigle_line.append(self.dic[line[0]])
            if sigle_line[1] == "C_ARITHMETIC" or sigle_line[1] == "C_BOOL":
                sigle_line.append(line[0])
            else:
                sigle_line.append(line[1])
                sigle_line.append(line[2])
            list.append(sigle_line)
        
        return list

    

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