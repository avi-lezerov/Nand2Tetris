class Translator:
    
    def __init__(self, file_name : str):
        self.file_name = file_name
        self.bool = 0
        self.sagment = self.sagment_table()
        self.arithmetic_op = self.arithmetic_operator_table()
        self.boolean_op = self.doolean_operator_table()
        self.push_to_D = ['@SP' , 'A=M', 'M=D']
        self.pop_to_D = ['@SP', 'AM=M-1', 'D=M']
        self.haed_stack_to_A = ['@SP', 'A=M']
        self.increment = ['@SP', 'M=M+1']
        self.decrement = ['@SP', 'M=M-1']

        
        
    

    def arithmetic(self, op : str):
        self.asm_commands = []
        if op != 'neg' and op != 'not':
                self.asm_commands.extend(self.pop_to_D)
        self.asm_commands.extend(self.haed_stack_to_A)
        self.asm_commands.append(self.arithmetic_op[op])
        self.asm_commands.extend(self.increment)

        return self.asm_commands
         
          

    def boolean(self ,op : str):
        self.asm_commands = []
        self.asm_commands.extend(self.pop_to_D)
        self.asm_commands.extend(self.increment)
        self.asm_commands.extend(self.haed_stack_to_A)
        self.asm_commands.append('D=M-D')
        self.asm_commands.append('@BOOL' + str(self.bool))
        self.asm_commands.append(self.boolean_op[op])
        self.asm_commands.extend(self.haed_stack_to_A)
        self.asm_commands.append('M=0')
        self.asm_commands.append('@ENDBOOL' + str(self.bool))
        self.asm_commands.append('0;JMP')

        self.asm_commands.append('@BOOL' + str(self.bool))
        self.asm_commands.extend(self.haed_stack_to_A)
        self.asm_commands.append('M=-1')
        self.asm_commands.append('(ENDBOOL' + str(self.bool) + ')')
        self.bool += 1
        return self.asm_commands
        




    

    def push(self, segment : str, index : str):
        self.asm_commands = []
        self.segment_to_address(segment, index)
        if segment == 'constant':
            self.asm_commands.append('D=A')
        else:
            self.asm_commands.append('D=M')
        self.asm_commands.extend(self.push_to_D)
        self.asm_commands.extend(self.increment)

        return self.asm_commands

    
    def pop(self, segment : str, index : str):
        self.asm_commands = []
        self.segment_to_address(segment, index)
        self.asm_commands.extend(['D=A', '@R13', 'M=D'])
        self.asm_commands.extend(self.pop_to_D)
        self.asm_commands.extend(['@R13', 'A=M', 'M=D'])
     
        return self.asm_commands
      



    def segment_to_address(self, segment : str, index : str):
        address = self.sagment[segment] if segment != 'constant' else ''
        if segment == 'constant':
            self.asm_commands.append('@' + index)
        elif segment == 'static' :  
            self.asm_commands.append('@' + self.file_name + index)
        elif segment == 'pointer' or segment == 'temp' :
            self.asm_commands.append('@R' +str(address+ int(index)))
        else:
            self.asm_commands.append('@' + address)
            self.asm_commands.append('D=M')
            # self.asm_comands.append('@' + index)
            # self.asm_comands.append('A=D+A')
            if segment != 'static':
                self.asm_commands.append('@' + address)
                self.asm_commands.append('A=M+D')
            else:
                self.asm_commands.append('@' + self.file_name + index)
                self.asm_commands.append('A=A+D')
    
    
    
    def sagment_table(self) :
        return {
                'argument': 'ARG',
                'local': 'LCL',
                'this': 'THIS',
                'that': 'THAT',
                'temp': 'R5',
                'pointer': 3,
                'temp': 5,
                'static': 16,
            }
    
    def arithmetic_operator_table(self):
        return  {
                'add': 'M=M+D',
                'sub': 'M=M-D',
                'neg': 'M=-M',
                'or': 'M=M|D',
                'and': 'M=M&D',
                'not': 'M=!M',
            }
    
    def doolean_operator_table(self):
        return {
            'eq': 'D;JEQ',
            'gt': 'D;JGT',
            'lt': 'D;JLT',
        }
    



    
