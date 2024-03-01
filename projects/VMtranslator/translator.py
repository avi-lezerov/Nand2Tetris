pop_val_to_D = ['@SP', 'AM=M-1', 'D=M']
pop_into_M = ['@SP', 'AM=M-1']
increment = ['@SP', 'M=M+1']

sagment_table = {
                'argument': 'ARG',
                'local': 'LCL',
                'this': 'THIS',
                'that': 'THAT',
                'temp': 'R5',
                'pointer': 3,
                'temp': 5,
                'static': 16,
            }


arithmetic_table  = {
                'add': 'M=D+M',
                'sub': 'M=M-D',
                'neg': 'M=-M',
                'or': 'M=D|M',
                'and': 'M=D&M',
                'not': 'M=!M',
            }
    
doolean_table = {
            'eq': 'D;JEQ',
            'gt': 'D;JGT',
            'lt': 'D;JLT',
        }
    

class Translator:
    def __init__(self, file_name : str):
        self.file_name = file_name
        self.bool = 0
       
        

    def arithmetic(self, op : str):
        list = []
        if op == 'add' or op == 'sub' :
            list.extend(pop_val_to_D)
            list.extend(pop_into_M)
            list.append(self.arithmetic_op[op])
            list.extend(increment) 
    
        elif op == 'neg' or op == 'not':
            list = ['@SP', 'A=M-1', arithmetic_table[op]]
        elif op == 'or' or op == 'and':
            list.extend(pop_val_to_D)
            list.extend(['@SP', 'A=M-1', arithmetic_table[op]])
        return list
          

    def boolean(self ,op : str):
        list = []
        label = op + 'True' + str(self.bool)
        self.bool += 1
        list.extend(pop_val_to_D)
        list.extend(['@SP', 'A=M-1', 'D=M-D', 'M=-1', '@'+label, doolean_table[op],
                     '@SP', 'A=M-1', 'M=0', '('+label+')'])
        return list
        


    def push(self, segment : str, index : str):
        list = []
        if segment == 'constant':
            list = ['@' + index, 'D=A', '@SP', 'A=M', 'M=D' ]
        elif segment == 'static':
            list = ['@' + self.file_name + '.' + index, 'D=M', '@SP', 'A=M', 'M=D']
        elif segment == 'this' or segment == 'that' or segment == 'argument' or segment == 'local' :
            list = ['@' + index, 'D=A', '@'+ sagment_table[segment], 'A=M+D', 'D=M', '@SP', 'A=M', 'M=D']
        elif segment == 'temp' or segment == 'pointer':
            list = ['@' + index, 'D=A', '@'+str(sagment_table[segment]), 'A=A+D', 'D=M', '@SP', 'A=M', 'M=D']

        list.extend(self.increment)
        return list


    def pop(self, segment : str, index : str):
        list = []
        if segment == 'static':
            list.extend(pop_val_to_D)
            list.extend(['@' + self.file_name + '.' + index, 'M=D'])
        if segment == 'this' or segment == 'that' or segment == 'argument' or segment == 'local' :
            list = ['@' + index, 'D=A', '@'+sagment_table[segment], 'D=M+D', '@R13', 'M=D']
            list.extend(pop_val_to_D)
            list.extend(['@R13', 'A=M', 'M=D'])
        if segment == 'temp' or segment == 'pointer':
            list = ['@' + index, 'D=A', '@'+str(sagment_table[segment]), 'D=A+D', '@R13', 'M=D']
            list.extend(pop_val_to_D)
            list.extend(['@R13', 'A=M', 'M=D'])
        
        return list