def f(student1, student2):
    student1_avg = avg(student1.split(','))
    student2_avg = avg(student2.split(','))

    if (student1_avg > student2_avg):
        return 1
    
    if (student2_avg > student1_avg):
        return 2
    
    return 0

def avg(grades):
    sum = 0

    for grade in grades:
        sum += int(grade)
    return sum / len(grades)

if __name__ == "__main__":
    print(f("3,4,5", "4,3"))
    print(f("3,4,5", "5,5,4,5"))
    print(f("3,4,5,4", "4,4"))