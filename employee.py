"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    pay = 0;
    def __init__(self, name, contType, contAmo, hours, commiType, commiAmo, contracts):
        self.name = name
        self.contType = contType
        self.contAmo = contAmo
        self.hours = hours
        self.commiType = commiType
        self.commiAmo = commiAmo
        self.contracts = contracts
        self.pay = Employee.pay

    def contractPay(self, contType, amo, hours):
        if contType == "monthly":
            return amo
        elif contType == "hourly" :
            return amo * hours

    def commissionPay(self, commiType, amo, contracts):
        if commiType == "bonus":
            return amo
        elif commiType == "contract":
            return contracts * amo
        else:
            return 0

    def get_pay(self):
        self.pay += self.contractPay(self.contType, self.contAmo, self.hours)
        self.pay += self.commissionPay(self.commiType, self.commiAmo, self.contracts)
        return self.pay

    def __str__(self):
        if self.contType == "monthly":
            if self.commiType == "bonus":
                return f"{self.name} works on a monthly salary of {self.contAmo} and receives a bonus commission of {self.commiAmo}. Their total pay is {self.pay}."
            elif self.commiType == "contract":
                return f"{self.name} works on a monthly salary of {self.contAmo} and receives a commission for {self.contracts} contract(s) at {self.commiAmo}/contract. Their total pay is {self.pay}."
            else:
                return f"{self.name} works on a monthly salary of {self.contAmo}. Their total pay is {self.pay}."
        elif self.contType == "hourly" :
            if self.commiType == "bonus":
                return f"{self.name} works on a contract of {self.hours} hours at {self.contAmo}/hour and receives a bonus commission of {self.commiAmo}. Their total pay is {self.pay}."
            elif self.commiType == "contract":
                return f"{self.name} works on a contract of {self.hours} hours at {self.contAmo}/hour and receives a commission for {self.contracts} contract(s) at {self.commiAmo}/contract. Their total pay is {self.pay}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.contAmo}/hour. Their total pay is {self.pay}."





# Billie works on a monthly salary of 4000.  Their total pay is 4000.
#                           type       amo   hours type  amo   cont
billie = Employee('Billie', "monthly", 4000, None, None, None, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 25, 100, None, None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", 3000, None, "contract", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 25, 150, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", 2000, None, "bonus", 1500, None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 30, 120, "bonus", 600, None)
