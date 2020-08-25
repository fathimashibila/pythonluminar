s={4,6,6,7,8,1,2,2,5,3,"car"}
print(s)

st={4,6,6,7,8,1,2,2,5,3,"car"}
a=st.copy()
print(a)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st.add(9)
print(st)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st.clear()
print(st)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st2={1,2,4,10}
st3=st.difference(st2)
print(st3)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st2={1,2,4,10}
st.difference_update(st2)
print(st)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st.discard(1)
print(st)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st2={1,2,4,10}
st3=st.intersection(st2)
print(st3)

set1={4,6,6,7,8,1,2,2,5,3,"car"}
set2={1,2,4,10}
set1.intersection_update(set2)
print(set1)

set1={4,6,6,7,8,1,2,2,5,3,"car"}
set2={1,2,4,10}
set3={4,6,7}
set1.intersection_update(set2,set3)
print(set1)

set1={4,6,6,7,8,1,2,2,5,3,"car"}
set2={1,2,4,10}
z=set1.isdisjoint(set2)
print(z)

set1={4,6,6,7,8,1,2,2,5,3,"car"}
set2={1,2,4,10}
z=set1.issubset(set2)
print(z)

set1={4,6,6,7,8,1,2,2,5,3,"car"}
set2={1,2}
z=set1.issuperset(set2)
print(z)

set1={4,6,6,7,8,1,2,2,5,3,"car"}
set1.pop()#removes random element
print(set1)

set1={4,6,6,7,8,1,2,2,5,3,"car"}
set1.remove(2)#removes speciped element
print(set1)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st2={1,2,4,10}
st3=st.symmetric_difference(st2) #randilum common  aayitt ullth ozhich
print(st3)


st={4,6,6,7,8,1,2,2,5,3,"car"}
st2={1,2,4,10}
st.symmetric_difference_update(st2) #randilum common  aayitt ullth ozhich
print(st)

st1={4,6,6,7,8,1,2,2,5,3,"car"}
st2={1,2,4,10}
st3=st1.union(st2) #randilum common  aayitt ullth ozhich
print(st3)

st={4,6,6,7,8,1,2,2,5,3,"car"}
st2={1,2,4,10}
st.update(st2) #randilum common  aayitt ullth ozhich
print(st)













