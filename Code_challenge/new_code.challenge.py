# Given a hashmap where the keys are integers, print out all of the values of the 
# hashmap in reverse order, ordered by the keys.
# 
# For example, given the following hashmap:{
#   14: "vs code",
#   3: "window",
#   9: "alloc",
#   26: "views",
#   4: "bottle",
#   15: "inbox",
#   79: "widescreen",
#   16: "coffee",
#   19: "tissue",
# }
# The expected output is:widescreen
# views
# tissue
# coffee
# inbox
# vs code
# alloc
# bottle
# window
# since "widescreen" has the largest integer key, "views" has the second largest, 
# etc.You may use whatever programming language you'd like.

hashmap = {
  14: "vs code",
  3: "window",
  9: "alloc",
  26: "views",
  4: "bottle",
  15: "inbox",
  79: "widescreen",
  16: "coffee",
  19: "tissue",
}

# list_rev = []
# for k in hashmap.keys():
#     list_rev.append(k)

# list_rev = sorted(list_rev, reverse = True )    
# print(list_rev)    

# for item in list_rev:
#     print(f' {item}: {hashmap[item]}')

# list_val = sorted(hashmap.keys(), reverse = True)
# print(list_val)
# print(hashmap[(sorted(hashmap.items(), reverse = True))])

# for item in list_val:
#     print(f'{hashmap[item]}')

for item in sorted(hashmap.keys(), reverse = True):
  print(f'{hashmap[item]}')    

