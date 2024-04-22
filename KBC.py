Questions=[
    ["Which language is used for app development?","python","java","javaScript","c++"],
    ["Which language is most famous?","python","HTML","java","javascript"],
    ["Which language is used for web development?","css","HTML","javascript","all of them"],
    ["Which subject is most important for graping placements?","critical thinking","discrete structure","pakistan studies","DSA"],
    ["Which subject is most important with python for data science","critical thinking","discrete structures","statistics","state,society and civic engagement"]
]
levels=["1","2","3","4","5"]
money=0
for a in range(0,len(Questions)):
    Question=Questions[a]
    print(f"Your present level is {levels[a]},the question is:")
    print(f"{Question[0]}")
    print(f"a){Question[1]}")
    print(f"b){Question[2]}")
    print(f"c){Question[3]}")
    print(f"d){Question[4]}")
    Answer=str(input("please enter your correct answer \nOtherwise press 0 for exit;\n"))
    if Answer=="0":
        break
    elif Answer==Question[2] in Questions[0] or Answer==Question[1] in Questions[1] or Answer==Question[4] in Questions[2] or Answer==Question[4] in Questions[3] or Answer==Question[3] in Questions[4] :
        print(f"correct answer,you paased {levels[0]}")
        if (a==0):
            money=500
        elif (a==1):
            money=1000
        elif a==2:
            monet=1500
        elif a==3:
            money=2000
        elif a==4:
            money=2500
        else:
            money=0
    else:
        print("yor entered answer is wromg!,better luck for next time")
        break
print(f"you are taking {money} to your home")
    
