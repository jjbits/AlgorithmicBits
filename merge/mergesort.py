#
# mergesort.py - merge sort
#
# Copyright (C) 2017 by Joon Jung
#
# This code is licensed under the MIT license (MIT) (http://opensource.org/licenses/MIT)
#


# input: unordered list of integers
# output: increasing ordered list of input integers
#
# Pseudocode
# mergesort(in_list)
#
#  base check: if len(in_list) == 1 return
#
#  recursive call: call two mergesort with in_list[0: len(inlist/2)] 
#                  and in_list[(len(inlist/2): ]
#  get out_list1 and out_list2 from those two recursive calls
#  do merge:
#  out_list[]
#  for i in range(: len(inlist/2))
#    if out_list1[j] <= out_list2[k]:
#       out_list[i] = out_list1[j]
#     else
#       out_list[i] = out_list2[k]
#  return out_list
#
# Big O upper bound
# for a given input number n
# each level is log(2, n) the root node being 0
# there are log(2, n) + 1 total levels in the recursion tree
# Each level has pwr(2, j) works * alpha*n/pwr(2, j) for j level
# This gives alpha*n work, therfore the totla work is
# alpha*n*(log(2, n) + 1) = alph*n*log(2, n) + alpha*n

def merge(in_list, out_list1, out_list2):
  out_list = []
  j = 0
  k = 0
  for i in range(0, len(in_list)):
    # both j and k index reached the end, return
    if j == len(out_list1) and k == len(out_list2):
      return out_list
    # We can return immediately for the followin two
    # cases as diff(out_lis1, out_list2) =< 1
    elif j == len(out_list1) and k < len(out_list2):
      out_list.append(out_list2[k])
      return out_list
    elif j < len(out_list1) and k == len(out_list2):
      out_list.append(out_list1[j])
      return out_list
    else:
      if out_list1[j] <= out_list2[k]:
        out_list.append(out_list1[j])
        j += 1
      else:
        out_list.append(out_list2[k])
        k += 1

  # This should not be reached.
  return out_list



def mergesort(in_list):
  if len(in_list) <= 1:
    return in_list

  in_list1 = in_list[0 : int(len(in_list)/2)]
  in_list2 = in_list[int(len(in_list)/2) : len(in_list)]
  out_list1 = mergesort(in_list1)
  out_list2 = mergesort(in_list2)

  #print("out_list1")
  #print(out_list1)
  #print("out_list2")
  #print(out_list2)

  return merge(in_list, out_list1, out_list2)

test_list = [7, 3, 5, 1, 1, 9, 5]
#test_list = []
#test_list = [7]
#test_list = [7, 3]
sorted_list = mergesort(test_list)
print(sorted_list)
