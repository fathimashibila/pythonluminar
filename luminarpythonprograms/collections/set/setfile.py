#set is unorderd collction of unique elements
#it is possible to store differnt types of data
#duplication not allowed
#insertion order is not preserved
#mutable
#indexing or slicing not supported in set

#methods in set add(),clear(),copy(),difference(),differnce_update(),discard(),intersection(),intersection_update(),isdisjoint()
#issubset(),issuperset(),pop(),remove(),symmetric_differnce(),symmetric_differnce_update(),union(),update()

#union
st={1,2,3,4}
st1={5,4,8,}
st3=st.union(st1)
print(st3)

#intersection
st4=st.intersection(st1)
print(st4)

#difference
str=st.difference(st1)
print(str)