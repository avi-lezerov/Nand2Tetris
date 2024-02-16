import sys
import os
from HackAssembler import HackAssembler

      
def main():
        """
        Main function that runs the HackAssembler.
        """
        if len(sys.argv) != 2 or not sys.argv[1].endswith(".asm") or not os.path.exists(sys.argv[1]): 
                raise ValueError("Usage: python main.py <file.asm>")
        path = sys.argv[1]
        
        file_name = os.path.basename(path)
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        assembler = HackAssembler(file_path)
        assembler.run()

        

           
              
           
if __name__ == "__main__":
    main()
