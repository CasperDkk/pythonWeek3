def get_grade (score):
    if score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    elif score >= 60:
        return "Grade D"
    else:
        return "Grade F"
    
def main():
    while True:
        try:
            score = float(input("Enter your score(0-100): "))
            if score < 0 or score > 100:
                print("Please enter a score between 0 and 100.")
            else:
                print(get_grade(score))
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
    
    
