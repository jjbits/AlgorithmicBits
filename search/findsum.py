# INPUT: An integer list and an integer s
# OUTPUT: A tuple of (x, y) which is s = x + y


# Simple Way
# Loop through the input list
# and for each num, loop again starting from
# the next item
# to find the sum is equal to s.
# If found, return them as a pair.
# O(pwr(n, 2))
def findsum(num_list, s):
  for each_num in num_list:
    for another_each_num in num_list:
      if each_num != another_each_num:
        if each_num+another_each_num == s:
          print("Found a pair: (", str(each_num), " ", str(another_each_num), ")")
          return

  print("None found")

# Faster way
# num1 is the first the smallest number
# num2 is the end the largest number
# indx1 first points to 0
# indx2 first point to len(num_list)
# if num1 + num2 == s, we found our guy
# if not
#   while idx1 < idx2
#     if num1 + num2 < s, we set idx2-= 1 amd  num2 = num_list[indx2]
#     else idx1+=1 and num1 = num_list[idx1]
#     if num1+num2 == s
#         return(num1, num2)
# return not found	
# O(n)

def findsum_fast(num_list, s):
  idx1 = 0
  idx2 = len(num_list) - 1
  num1 = num_list[idx1]
  num2 = num_list[idx2]

  while idx1 < idx2:
    if num1+num2 == s:
      print("Found a pair: (", str(num1), ",", str(num2), ")")
      return

    if num1+num2 > s:
      idx2 -= 1
      num2 = num_list[idx2]
    else:
      idx1 += 1
      num1 = num_list[idx1]


num_list = [1, 2, 3, 4, 5]
s = 7
findsum_fast(num_list,s)
