def count(s):
    c = 0
    for i in s:
        if i.lower() in "aeiou":
            c = c+1
        else:
            continue
    print(c)

def rev(s):
    temp = s[::-1]
    print(temp)