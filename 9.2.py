name = input("Enter file:")
largest=None
num=dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line.rstrip
    if not line.startswith("From "):
        continue
    else:
        words=line.split()
        hold=words[2]
        if hold not in num:
            num[hold]=1
        else:
            num[hold]=num[hold]+1
print(num)