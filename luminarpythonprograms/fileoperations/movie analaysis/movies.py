f=open("moviesdata","r")
dict={}
dictt={}
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[1]
    year=data[2]
    rate=data[3]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
    if(rate not in dictt):
        dictt[rate]=1
    else:
        dictt[rate]=dictt[rate]+1

print(" YEAR:NO OF MOVIES RELEASED")
for year,movies in dict.items():
    print(year,":",movies)

print("RATING:NO OF MOVIES")
for rate,movies in dictt.items():
    print(rate,":",movies)

print("MAXIMUM NO OF MOVIES RELEASED IN THE YEAR")
maximum=max(dict,key=dict.get)
print("Year:",maximum,",","no of movies releasd:",dict[maximum])