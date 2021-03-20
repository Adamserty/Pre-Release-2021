YearList = [0, 7, 8, 9, 10, 11]
SectionList = ['none', 'A', 'B', 'C', 'D', 'E', 'F']
print ("Enter the number corresponding to the year group")
print ("1. 7")
print ("2. 8")
print ("3. 9")
print ("4. 10")
print ("5. 11")
print ("Enter here:")
Year = int(raw_input())
if Year == 1 or Year == 2 or Year == 3 or Year == 4 or Year == 5:
    print("This is the year chosen: {}".format(YearList[Year]))
else:
    print("Invalid year.")
print("Enter the number corresponding to the section")
print ("1. A")
print ("2. B")
print ("3. C")
print ("4. D")
print ("5. E")
print ("6. F")
print("Enter here:")
Section = int(raw_input())
if Section == 1 or Section == 2 or Section == 3 or Section == 4 or Section == 5 or Section == 6:
    print("This is the section chosen: {}".format(SectionList[Section]))
else:
    print("Invalid Section.")
Group = (str(YearList[Year]) + str(SectionList[Section]))
print("")
print ("This is the group chosen : {}".format(Group))
print(" ")
print("Enter number of students on group :")
StdNum = int(raw_input())
if 28 <= StdNum <= 35:
    print("This is the number of students entered: {}".format(StdNum))
else:
    print("Out of range of students.")
print("Enter number of candidates running for the election :")
Candidates = int(raw_input())
if 1 <= Candidates <= 4:
    print("This is the number of candidates chosen : {}".format(Candidates))
else:
    print("Out of range of candidates allowed.")
CandidatesNames = [""]*Candidates
for count in range(0, Candidates):
    CandidatesNames[count] = raw_input("Enter the name of the candidate: ")
print("The names are: ")
for x in range(len(CandidatesNames)):
    print CandidatesNames[x]



