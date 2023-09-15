map = {"a+":4, "a":3, "a-":3.7, "b+":3.3, "b":3, "b-":2.7, "c+":2, "d":1}
cnt = 0
grade = 0
inp = input("Grade:")
while inp != "end":
    while inp not in map.keys():
        inp = input("Grade:")
    grade += map[inp]
    cnt += 1
    inp = input("Grade:")

print("GPA:", grade/cnt)