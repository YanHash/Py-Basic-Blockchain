from hashFunction import *
from Transaction import *

class Block:

    """ Constructeur de blocs 

    :param transactions: la liste des transactions opérées sur la blockchain 
    :param previousBlockHash: le hash (somme de controle) du block précédent 
    """
    def __init__(self, timestamp, transactions, previousBlockHash=""):
        self.count = 0
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousBlockHash = previousBlockHash
        self.currentBlockHash = self.hashBlock()
        



    """ Produit le hash d'un bloc donné 

    :return: le hash produit
    """
    def hashBlock(self):
        allTransactions = ""
        for transaction in self.transactions:
            allTransactions += str(transaction.__dict__)
        hashable = self.timestamp + str(self.count) + self.previousBlockHash + allTransactions
        return hashFunction(hashable)



    """ Mine des blocs jusqu'à atteindre le preuve de travail
        qui est vérifiée si le hash du bloc actuel commence par
        autant de "0" que le niveau de la difficulté de minage prévue
        par la blockchain
    """
    def mineBlock(self, miningDifficulty):
        while (self.currentBlockHash[:miningDifficulty] != miningDifficulty * '0'):
            self.currentHash = self.hashBlock()
            print("minage en cours")
            self.count += 1
        print("fin de minage")

        