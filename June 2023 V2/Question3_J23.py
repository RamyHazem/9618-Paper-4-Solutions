class Employee(object):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        """
        init the employee class
        :param HourlyPay: REAL
        :param EmployeeNumber: STRING
        :param JobTitle: STRING
        """
        self.HourlyPay = HourlyPay
        self.EmployeeNumber = EmployeeNumber
        self.JobTitle = JobTitle
        self.PayYear2022 = [0.0 for i in range(52)]

    def GetEmployeeNumber(self):
        return self.EmployeeNumber

    def SetPay(self, week_no, no_of_hours):
        pay = self.HourlyPay * int(no_of_hours)
        self.PayYear2022[week_no - 1] = pay

    def GetTotalPay(self):
        return sum(self.PayYear2022)


class Manager(Employee):
    def __init__(self, BonusValue, HourlyPay, EmployeeNumber, JobTitle):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.BonusValue = int(BonusValue)

    def SetPay(self, week_no, no_of_hours):
        no_of_hours = no_of_hours * (1 + (self.BonusValue / 100))
        super().SetPay(week_no, no_of_hours)


EmployeeArray = []

with open("./Employees.txt", "r") as employee_file:
    try:
        while True:
            hourly_pay = float(employee_file.readline().strip())
            if not hourly_pay:
                break
            employee_no = int(employee_file.readline().strip())
            bonus_or_title = employee_file.readline().strip()

            try:
                bonus_val = float(bonus_or_title)
                job_title = employee_file.readline().strip()
                new_manager = Manager(HourlyPay=hourly_pay, EmployeeNumber=employee_no, JobTitle=job_title,
                                      BonusValue=bonus_val)
                EmployeeArray.append(new_manager)
            except ValueError:
                job_title = bonus_or_title
                new_employee = Employee(HourlyPay=hourly_pay, EmployeeNumber=employee_no, JobTitle=job_title)
                EmployeeArray.append(new_employee)

    except Exception as Error:
        print(f"Error: {Error}")

    finally:
        employee_file.close()


def EnterHours():
    with open("./HoursWeek1.txt", "r") as file:
        for i in range(8):
            employee_number = int(file.readline().strip())
            no_of_hours = float(file.readline().strip())
            for emp in EmployeeArray:
                if employee_number == int(emp.GetEmployeeNumber()):
                    emp.SetPay(1, no_of_hours=no_of_hours)


EnterHours()


for employee in EmployeeArray:
    print(f"Employee Number: {employee.GetEmployeeNumber()}, Total Pay: {employee.GetTotalPay()}")
