class FileReader:

    def __init__(self, path):
        try:
            file = open(path, "r")  
        except:
            raise ValueError("Error: File not found.")
    
        self.file = file.readlines()
        file.close()
       

    def get_file_content(self) :
        list = []
        for line in self.file:
            if line != '' and line != '\n' and line[0] != '/' :
                list.append(line)
        return list