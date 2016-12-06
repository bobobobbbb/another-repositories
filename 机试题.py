prompt = input("输入样例：")
while not(len(prompt) <= 10000 and prompt.isalpha()):
    prompt = input("你的输入有误请重新输入：")

list1 = list(prompt)
print("输出样例:",end = "")
while ("P" in list1) or ("y" in list1) or ("t" in list1) or ("h" in list1) or ("o" in list1) or("n" in list1):
    for P in list1:
        if P == "P":
            print("P",end = "")
            list1.remove("P")
            break
    for y in list1:
        if y == "y":
            print("y",end = "")
            list1.remove("y")
            break
    for t in list1:
        if t == "t":
            print("t",end = "")
            list1.remove("t")
            break
    for h in list1:
        if h == "h":
            print("h",end = "")
            list1.remove("h")
            break
    for o in list1:
        if o == "o":
            print("o",end = "")
            list1.remove("o")
            break
    for n in list1:
        if n == "n":
            print("n",end = "")
            list1.remove("n")
            break
