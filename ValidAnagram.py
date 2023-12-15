def Val_angrm(s,t):
    counter = {}

    if len(s) != len(t):
        return False
    else:
        for i in s:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1

        for i in t:
            if i in counter:
                counter[i]-=1
            else:
                counter[i]=1

        for k in counter.keys():
            if counter[k] !=0:
                return False
        return True


    #return counter
    
x= Val_angrm('anagram','nagaram')
#x= Val_angrm('rat','car')
#x= Val_angrm('aa','bb')
print(x)
                
            
