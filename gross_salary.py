Gross_Salary=float(input("Enter Gross Salary:"))
Federal_Deductions=float(input("Enter FD:"))
Static_Deductions=float(input("Enter SD:"))
CPP_Deductions=float(input("Enter CPP:"))
Number_of_Weeks=int(input("Enter number of Weeks:"))
Total_Deductions=Federal_Deductions + Static_Deductions + CPP_Deductions
Net_Salary = Gross_Salary - (Gross_Salary * (Total_Deductions/100))
print("Net Salary:" ,Net_Salary * Number_of_Weeks)
