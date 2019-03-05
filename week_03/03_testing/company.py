class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, more_money=5000):
        if isinstance(more_money, int) is False:
            return "You need to enter a positive integer!"
        elif more_money < 0:
            return f"{more_money} is NOT a raise!"
        else:
            self.salary += more_money
            return f"After a raise of {more_money}, you have {self.salary}."
