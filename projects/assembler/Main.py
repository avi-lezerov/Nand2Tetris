import sys
import os
from HackAssembler import HackAssembler

      
def main():
    """
    Main function that runs the HackAssembler.
    """
    if len(sys.argv) != 2  or not os.path.exists(sys.argv[1]): 
        raise ValueError("Usage: python main.py <file.asm>")
    
    path = sys.argv[1]
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.endswith(".asm"):
                single_file(os.path.join(path, file))

    elif os.path.isfile(path) and path.endswith(".asm"):
        single_file(path)

    
def single_file(path):
    """
    Assembles a single file.
    """
    file_name = os.path.basename(path)
    file_path = os.path.abspath(path)  # Normalize the path to absolute
    # Create an assembler object and run it
    assembler = HackAssembler(file_path)
    # Assemble the file
    assembler.run()
                            
if __name__ == "__main__":
    main()
