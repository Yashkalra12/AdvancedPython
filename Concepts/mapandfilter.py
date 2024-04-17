marks=[80,45,67,75,95,84]
def grades(marks):
    if marks>=90:
        return 'A'
    elif marks>=80:
        return 'B'
    elif marks>=70:
        return 'C'
    else:
        return 'F'
    
grades=list(map(grades,marks))
print(grades)    

def check(marks):
    if marks>70:
        return marks

checking=list(filter(check,marks))
print(checking)    

evens=list(filter(lambda a:a%2==0,marks))
print(evens)