from datetime import *


class Transaction:

    """ Constructeur de transactions
    
    :param sender: l'émetteur du paiement
    :param receiver: le receveur du paiment 
    :param amount: le montant de la transaction
    """
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

        # la date du moment de la création de la transaction au format UNIX datetime
        self.timestamp = str(datetime.timestamp(datetime.now())) 


    """ Renvoie l'émetteur du paiment

    :return: l'émetteur du paiment
    """
    def getSender(self):
        return self.sender


    """ Renvoie le receveur du paiment

    :return: le receveur du paiment
    """
    def getReceiver(self):
        return self.receiver


    """ Renvoie le montant de la transaction

    :return: le montant de la transaction
    """
    def getAmount(self):
        return self.amount


    """ Renvoie la date de la transaction au format UNIX datetime

    :return: la date de la transaction au format UNIX datetime
    """
    def getDatetime(self):
        return self.timestamp