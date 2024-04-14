Ne = int(input("event: "))
#number events

events = []
result = [] #Person and time

def register():
    for e in range(0, Ne):
        event = input("Event: ")
        events.append(event)
        person = int(input("person: "))
        events.append(person)    
    return events
def readevent(Ev):
    for i in range(0, len(Ev), 2):
        En = Ev[i] #current event
        Pn = Ev[i + 1] #person of event
        time = 0
        if(En == "R"): #excludes other events that do not start with Receiver
            
            for c in range(i + 2, len(Ev), 2): #star after current event
                if(Ev[c] == "T"):
                    time += Ev[c + 1] #time
                elif(Ev[c] == "R" and Ev[c - 2] != "T"):
                    time += 1
                elif(Ev[c] == "E" and Ev[c + 1] == Pn): #Send mensage
                    if (Ev[c - 2] != "T"):
                        time += 1
                    break
            result.append(Pn) #person
            result.append(time) #time
            for n in range(0, len(result), 2):
                if(result[n] == Pn):
                    time += result[n + 1]
                    result.insert(n + 1, time) #Time for the person to have been responded to
                    result.pop(n + 2)#remove old time
                    result.pop() #remove last time repeted
                    result.pop() #remove last person repeted
                
    return result
def printResut(r):
    for g in range(0, len(r), 2):
        print(f"{r[g]} {r[g+1]}")
        
events = register()
result = readevent(events)
printResut(result) #Print Result