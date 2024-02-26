class Translator:
    def __init__(self, file_name : str):
        self.file_name = file_name
        self.bool = 0
        self.sagment = self.sagment_table()
        self.arithmetic_op = self.arithmetic_operator_table()
        self.boolean_op = self.doolean_operator_table()
        self.pop_val_to_D = ['@SP', 'AM=M-1', 'D=M']
        self.pop_into_M = ['@SP', 'AM=M-1']
        self.increment = ['@SP', 'M=M+1']
        
        
    def set_file_name(self, file_name : str):
        self.file_name = file_name
        self.bool = 0
    

    def arithmetic(self, op : str):
        list = []
        if op == 'add' or op == 'sub' :
            list.extend(self.pop_val_to_D)
            list.extend(self.pop_into_M)
            list.append(self.arithmetic_op[op])
            list.extend(self.increment) 
    
        elif op == 'neg' or op == 'not':
            list = ['@SP', 'A=M-1', self.arithmetic_op[op]]
        elif op == 'or' or op == 'and':
            list.extend(self.pop_val_to_D)
            list.extend(['@SP', 'A=M-1', self.arithmetic_op[op]])
        return list
          

    def boolean(self ,op : str):
        list = []
        label = op + 'True' + str(self.bool)
        self.bool += 1
        list.extend(self.pop_val_to_D)
        list.extend(['@SP', 'A=M-1', 'D=M-D', 'M=-1', '@'+label, self.boolean_op[op],
                     '@SP', 'A=M-1', 'M=0', '('+label+')'])
        return list
        


    def push(self, segment : str, index : str):
        list = []
        if segment == 'constant':
            list = ['@' + index, 'D=A', '@SP', 'A=M', 'M=D' ]
        elif segment == 'static':
            list = ['@' + self.file_name + '.' + index, 'D=M', '@SP', 'A=M', 'M=D']
        elif segment == 'this' or segment == 'that' or segment == 'argument' or segment == 'local' :
            list = ['@' + index, 'D=A', '@'+self.sagment[segment], 'A=M+D', 'D=M', '@SP', 'A=M', 'M=D']
        elif segment == 'temp' or segment == 'pointer':
            list = ['@' + index, 'D=A', '@'+str(self.sagment[segment]), 'A=A+D', 'D=M', '@SP', 'A=M', 'M=D']

        list.extend(self.increment)
        return list


    def pop(self, segment : str, index : str):
        list = []
        if segment == 'static':
            list.extend(self.pop_val_to_D)
            list.extend(['@' + self.file_name + '.' + index, 'M=D'])
        if segment == 'this' or segment == 'that' or segment == 'argument' or segment == 'local' :
            list = ['@' + index, 'D=A', '@'+self.sagment[segment], 'D=M+D', '@R13', 'M=D']
            list.extend(self.pop_val_to_D)
            list.extend(['@R13', 'A=M', 'M=D'])
        if segment == 'temp' or segment == 'pointer':
            list = ['@' + index, 'D=A', '@'+str(self.sagment[segment]), 'D=A+D', '@R13', 'M=D']
            list.extend(self.pop_val_to_D)
            list.extend(['@R13', 'A=M', 'M=D'])
        
        return list

    
        
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
                'add': 'M=D+M',
                'sub': 'M=M-D',
                'neg': 'M=-M',
                'or': 'M=D|M',
                'and': 'M=D&M',
                'not': 'M=!M',
            }
    
    def doolean_operator_table(self):
        return {
            'eq': 'D;JEQ',
            'gt': 'D;JGT',
            'lt': 'D;JLT',
        }
    



    
