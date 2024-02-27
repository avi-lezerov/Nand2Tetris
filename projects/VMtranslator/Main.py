import sys
import os
from VMtranslator_writer import VMtranslator

   
def main():
    
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        raise ValueError("Usage: python main.py <path_to_vm_file_or_folder>")
   
    input_path = os.path.abspath(sys.argv[1])
    
    if os.path.isfile(input_path) and input_path.endswith(".vm"):
        process_single_file(input_path)
    elif os.path.isdir(input_path):
        process_directory(input_path)
    else:
        # Invalid input
        raise ValueError("Invalid input path.")


def process_directory(directory):
    directory_name = os.path.basename(directory)
    VMtr = VMtranslator(directory + "\\" + directory_name + ".asm")
    files = os.listdir(directory)
    vm_files = [f for f in files if f.endswith(".vm")]
    for file in vm_files:
        VMtr.prosses_file(os.path.join(directory, file))
        

def process_single_file(path):
    file_path = os.path.abspath(path)  # Normalize the path to absolute
    VMtr = VMtranslator(file_path)
    VMtr.prosses_file(file_path)


if __name__ == "__main__":
    main()