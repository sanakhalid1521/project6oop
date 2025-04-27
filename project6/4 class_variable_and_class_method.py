class Bank:
    bank_name = "HBL Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder  

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name 

bank1 = Bank("sana")

print(f"Initial Bank Name: {bank1.bank_name}")

# Bank name change 
Bank.change_bank_name("UBL Bank")
print(f"Updated Bank Name: {bank1.bank_name}")
