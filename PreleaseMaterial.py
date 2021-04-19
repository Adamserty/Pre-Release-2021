TutorGroup = input("Type the tutor group to set up votes for Eg. 7A")

while len(TutorGroup) < 2:
    TutorGroup = input("Error. Type the tutor group to set up votes for Eg. 7A: ")

NumStudents = int(input("Please input the number of students in this tutor group: "))

while NumStudents < 28 or NumStudents > 35:
    NumStudents = int(input("Error. Please input the number of students in the tutor group: "))

NumCandidates = int(input("How many candidates are in this tutor group?"))

while NumCandidates < 1 or NumCandidates > 4:
    NumCandidates = int(input("Error. How many candidates are in this tutor group? 1-4 max "))

NamesCandidates = [""] * NumCandidates
Votes = [0] * NumCandidates
Abstain = 0

for count in range(0, NumCandidates):
    NamesCandidates[count] = input("Type the name of the candidate: ")

for count in range(0, NumStudents):
    print("Here are the names of the candidates so you can vote: ", NamesCandidates)

    for i in range(0, NumCandidates):
        print("Type ", i + 1, "to vote for: ", NamesCandidates[i])

    print("To abstain from voting press 0")

    VoteInput = int(input())
    while VoteInput < 0 or VoteInput > NumCandidates:
        VoteInput = int(input("Error, type the candidate number or type 0 to abstain."))

    if VoteInput == 0:
        Abstain = Abstain + 1
    elif VoteInput == 1:
        Votes[0] = Votes[0] + 1
    elif VoteInput == 2:
        Votes[1] = Votes[1] + 1
    elif VoteInput == 3:
        Votes[2] = Votes[2] + 1
    else:
        Votes[3] = Votes[3] + 1

print ("TutorGroup: ", TutorGroup)
for count in range(0, NumCandidates):
    print("Candidate Name: ", NamesCandidates[count])
    print("Number of Votes: ", Votes[count])
print("Number of Abstained: ", Abstain)

winners = ""
most = Votes[0]
for count in range(0, NumCandidates):
    if Votes[count] > most:
        most = Votes[count]

for count in range(0, NumCandidates):
    if Votes[count] == most:
        winner = NamesCandidates[count]
        print("This candidate is a winner ", winner)