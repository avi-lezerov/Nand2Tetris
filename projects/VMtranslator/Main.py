import sys
import os
from VMtranslator_writer import VMtranslator

   
def main():
    if len(sys.argv) != 2  or not os.path.exists(sys.argv[1]): 
        raise ValueError("Usage: python main.py <file.asm>")
    
    end_with = ".vm"
    path = sys.argv[1]
    

    if os.path.isfile(path) and path.endswith(end_with):
        single_file(path)
    else:
        for file in os.listdir(path):
                if file.endswith(end_with):
                    single_file(os.path.join(path, file))

    
def single_file(path):
    file_path = os.path.abspath(path)  # Normalize the path to absolute
    VMtr = VMtranslator(file_path)
    VMtr.prosses_file()
         
                          
if __name__ == "__main__":
    main()

