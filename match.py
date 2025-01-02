# fruit=input("enter the fruit name")
# match fruit:
#     case "banana":
#         print("it's yellow")
#     case "orange":
#         print("it is orange")
'''grade calculator'''
def calculate_grade(score):
    match score:
        case score if 90 <= score <= 100:
            return "A"
        case score if 80 <= score < 90:
            return "B"
        case score if 70 <= score < 80:
            return "C"
        case score if 60 <= score < 70:
            return "D"
        case score if 0 <= score < 60:
            return "F"
        case _:
            return "Invalid score"

# Example usage:
scores = [95, 85, 75, 65, 55, -1, 105]
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score}, Grade: {grade}")
