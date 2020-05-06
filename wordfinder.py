import json
from difflib import get_close_matches


data=json.load(open("data.json"))

def map(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
       yn=input(f"Did u mean  {get_close_matches(w,data.keys())[0]} instead?? Y/N:  ")
       if yn=="Y":
           return data[get_close_matches(w,data.keys())[0]]
       elif yn=="N":
            return "The word does not Exist"
       else:
            return "We didn't understand your query!"
    else:
        return "Word not found!!"



    

    # word=w.lower()
    # print(word)
    
    # try:
    #      return (data[word])
    # except KeyError:
    #     print("Word not found!")
    # word=w.split(' ')
    # output=[]

    # for i in word:
    #     output.append(data.get(i,"oops!! Not found "))
    
    # print(output)
  


a=input("Enter a word: ")
output=map(a)
if type(output)== list:
    for item in output:
        print(item)
else:
        print(output)