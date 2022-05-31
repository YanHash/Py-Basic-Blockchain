from datetime import *
from Block import *
from Transaction import *

class Blockchain:

    def __init__(self):
        self.blockchain = []
        self.waitingTransactions = []
        self.miningReward = 0.5     # valeur choisie, le montant reçu après minage d'un bloc 
        self.miningDifficulty = 1   # valeur choisie, la difficulté de minage d'un bloc
        self.blockchain.append(self.genesisBlock())


    def genesisBlock(self) :
        print("creation bloc de genese")
        transactions = []
        date = str(datetime.timestamp(datetime.now()))
        firstBlock = Block(date, transactions)
        print("debut minage")
        firstBlock.mineBlock(self.miningDifficulty)
        return firstBlock


    def addTransaction(self, transaction):
        self.waitingTransactions.append(transaction)

    
    def getMiningDifficulty(self):
        return self.miningDifficulty
    
    
    def getMiningReward(self):
        return self.miningReward
    
    
    def getLastBlock(self):
        lastBlock = self.blockchain[-1]
        return lastBlock


    def getTransactions(self):
        transactions = []
        for transaction in self.waitingTransactions:
            transactions.append(transaction.__dict__)
        return transactions


    def mineWaitingTransactions(self, minerAddress):
        date = str(datetime.timestamp(datetime.now()))
        newBlock = Block(date, self.waitingTransactions)
        newBlock.mineBlock(self.miningDifficulty)
        self.blockchain.append(newBlock)
        self.waitingTransactions = [Transaction("[BlockChain] Mining Reward", minerAddress, self.miningReward)]


    def isValid(self):
        for i in range(1, len(self.blockchain)):
            previousBlock = self.blockchain[i-1]
            currentBlock = self.blockchain[i]
            print(previousBlock.currentBlockHash)
            print(currentBlock.previousBlockHash)

            if (currentBlock.currentBlockHash != currentBlock.hashBlock()) or (currentBlock.previousBlockHash != previousBlock.currentBlockHash):
                return False
            else:
                return True


    def getBalance(self, minerAddress):
        total = 0
        for block in self.blockchain:
            for trans in block.transactions:
                if trans.getSender() == minerAddress:
                    total -= trans.amount
                if trans.getReceiver() == minerAddress:
                    total += trans.amount
        return total


    def ViewBlockchain(self):
        n = 0
        chainLength = len(self.blockchain)
        for i in range(chainLength):
            print("datetime: ", self.blockchain[i].timestamp)

            for transaction in self.blockchain[i].transactions:
                print("***** Transaction N°", n, "*****")
                print("Sender: ", transaction.getSender())
                print("Receiver: ", transaction.getReceiver())
                print("Amount: ", transaction.getAmount())
                print("****************************\n")
                n += 1

            print("Hash: ", self.blockchain[i].currentBlockHash, "\n")