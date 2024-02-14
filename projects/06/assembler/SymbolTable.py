
class SymbolTable:

    
    def __init__(self):
        """
        Initializes the SymbolTable object and adds the predefined symbols to the table.
        """
        self.__table = {}
        for i in range(16):
            self.__table["R" + str(i)] = i
        self.__table["SCREEN"] = 16384
        self.__table["KBD"] = 24576
        self.__table["SP"] = 0
        self.__table["LCL"] = 1
        self.__table["ARG"] = 2
        self.__table["THIS"] = 3
        self.__table["THAT"] = 4
       
            



    def add_entry(self, symbol : str, address : int):
        """
        Adds the pair (symbol, address) to the table.

        Args:
            symbol (str): The symbol.
            address (int): The address.
        """
        pass

    def contains(self, symbol : str) -> bool:
        """
        Determines if the symbol table contains the given symbol.

        Args:
            symbol (str): The symbol.

        Returns:
            bool: True if the symbol is in the table, False otherwise.
        """
        return symbol in self.__table


    def get_address(self, symbol : str) :
        """
        Returns the address associated with the symbol.

        Args:
            symbol (str): The symbol.

        Returns:
            int: The address associated with the symbol.
        """
        if  self.contains(symbol):
            return self.__table.get(symbol)

    def get(self):
        return self.__table