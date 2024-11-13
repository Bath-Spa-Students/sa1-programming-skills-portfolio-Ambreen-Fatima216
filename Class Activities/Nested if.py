Salary = int(input("Enter your salary "))# salary variable for user input
if Salary >= 30000:
        years_on_job = float(input("Enter the years of job:"))#Years of job variable
        if years_on_job >= 2:
                print("You qualify for your job")
        else :
                print("experience is less than 2 years")
else :
        print("you must be earning atleast 30000 to qualify ")