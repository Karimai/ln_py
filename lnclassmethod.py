class Employee:
    raise_factor = 1.0
    num_employees = 0

    def __init__(self, name: str, last_name: str, base_salary: float):
        self.name = name
        self.last_name = last_name
        self.base_salary = base_salary
        Employee.num_employees += 1

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def get_salary(self):
        current_salary = self.base_salary * Employee.raise_factor
        return current_salary

    @classmethod
    def raise_salary(cls, factor: float):
        cls.raise_factor += factor

    @classmethod
    def from_string(cls, employee_str: str):
        fisrt_name, last_name, salary = employee_str.split(' ')
        return cls(fisrt_name, last_name, int(salary))

    def __str__(self):
        return f"{self.get_full_name()} {self.get_salary()}"


john = Employee('John', 'Smith', 1000)
pieter = Employee('Pieter', 'Debrie', 4000)
print(Employee.num_employees)
print(john)
Employee.raise_salary(0.05)
print(john)
kevin = Employee.from_string("Kevin Sobolov 5000")
print(kevin)
