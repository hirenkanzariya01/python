amount = 5000
class online_payment:
    def dabit_money():
        return "Dabit money from Online Payment"

    def cradit_money():
        a = int(input("Enter Amount :- "))
        return amount + a


class Cheack_payment:
    def dabit_money():
        return "Dabit money from Cheack Payment"



class Card_payment:
    def dabit_money():
        return "Dabit Money from Card Payment"


def money_transition(a):
    print(a.dabit_money())

def money_deposite(a):
    print(a.cradit_money())


money_deposite(online_payment)

# money_transition(online_payment)

# o_p = online_payment
# print(o_p.dabit_money())

# c_p = Cheack_payment
# print(c_p.dabit_money())
