


class Employee:
    def __init__(self, name, admission_date, wage) -> None:
        self.name = name
        self.admission_date = admission_date
        self. wage = wage
        
    def __str__(self) -> str:
        return f"Name: {self.name}, Admission Date: {self.admission_date}, Wage: {self.wage}"
    
class Manager(Employee):
    def __init__(self, name, admission_date, wage, bonus) -> None:
        super().__init__(name, admission_date, wage)
        self.bonus = bonus
    
    def calculate_salary_with_bonus(self):
        return self.wage + (self.wage * (self.bonus / 100))
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Admission Date: {self.admission_date}, Wage: {self.wage}, Bonus: {self.bonus}%"
        
    
person1 = Employee('Guilherme', '22/04/2024', 2000)
person2 = Manager('Tiago', '22/04/2000', 5000, 10)

print(person1)
print(person2)
print("Manager's salary with bonus:", person2.calculate_salary_with_bonus())