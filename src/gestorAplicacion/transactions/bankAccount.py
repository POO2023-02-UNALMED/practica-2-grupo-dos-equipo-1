class BankAccount(Serializable):
    instances = []

    def __init__(self, cvv):
        self.balance = 0.0
        self.cvv = cvv
        BankAccount.instances.append(self)
