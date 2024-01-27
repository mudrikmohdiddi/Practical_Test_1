def grade(score):
    if(score<0 or score>100):
        return "You enter wrong input"
    elif(score>=80):
        return "A"
    elif(score>=60):
        return "B"
    elif(score>=40):
        return "C"
    elif(score>=30):
        return "D"
    else:
        return "F"
def average(total_score,no_student):
    return total_score/no_student
def main():
    no_student=int(input("Please enter number of student:"))
    while(no_student<0):
        print("You enter wrong input, please try again")
        no_student=int(input("\nPlease enter number of student:"))
    sum=0
    for i in range(1,no_student+1):
        name=input(f"Please enter name of student.{i} :")
        score=int(input(f"Please enter score of student number.{i} name {name}:"))
        print(f"Student number.{i} name {name} his\her score:{score}  grade:{grade(score)}")
        sum=sum+score
    print("The overall average score is:", average(sum,no_student))
main()
