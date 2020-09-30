import time


print("hey, ik ben Leon"'\n')
time.sleep(1.5)
print("en wie ben jij?"'\n')
naam = input("type je naam hier : ")
time.sleep(0.5)
print('\n'"hey",naam,"aangenaam kennis te maken")
time.sleep(1)
print("ik ben 17 jaar jong en jij?"'\n')
leeftijd = input("type hier je leeftijd : ")
time.sleep(0.5)
print(leeftijd," nice"'\n')
print("doe je ook nog aan sport?")
sport = input("type ja of nee : ").upper()


if sport == "NEE":
    x = 'N'
    
 
elif sport == "JA":
    x = 'Y'

    
else:
    print("sorry maar dat is geen ja of nee :(")
    print('\n'"exiting script")
    time.sleep(0.5)
    exit()
    
while x == 'Y':
    print("cool welke sport doe je?")
    sport1 = input("type hier je sport : ")
    print('\n''\n',sport1,"is een gave sport")
    print("voor hoelang doe je deze sport al?")
    sporttijd = input("")
    
while x == 'N':
        print("ik doe ook geen sport")