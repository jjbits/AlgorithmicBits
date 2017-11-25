#
# findinversion.py
#
# Copyright (C) 2017 by Joon Jung
#
# This code is licensed under the MIT license (MIT) (http://opensource.org/licenses/MIT)
#

# Input: An integer list, all uniquie
# Ouput: Number of inversions

# Pseudocode
#
# count(A, n):
#
#  if n == 1 retrurn 0
#
#  x = count(left half of A, n/2)
#  y = count(right half of A, n/2)
#  z = count_split_inv(A, n)
#
#  return x+y+z

# This implementation uses merging just like
# the mergesort different than the pseudocodes

# Big O upper bound
# for a given input list length n
# each level is log(2, n) the root node being 0
# there are log(2, n) + 1 total levels in the recursion tree
# Each level has pwr(2, j) works * alpha*n/pwr(2, j) for j level
# This gives alpha*n work, therfore the totla work is
# alpha*n*(log(2, n) + 1) = alph*n*log(2, n) + alpha*n


def count_split_inv(a):
  n = len(a)
  left_a = a[0:n//2]
  right_a = a[n//2:]
  n_left = len(left_a)
  n_right = len(right_a)
  
  out_list = []
  i = 0
  j = 0
  k = 0
  count = 0
  for i in range(n):
    if j == n_left and k < n_right:
      while(k < n_right):
        out_list.append(right_a[k])
        k += 1
      return count, out_list
    elif j < n_left and k == n_right:
      while(j < n_left):
        out_list.append(left_a[j])
        j += 1
      return count, out_list
    else:
      if left_a[j] < right_a[k]:
        out_list.append(left_a[j])
        j += 1
      else:
        out_list.append(right_a[k])
        count += (n//2 - j)
        k += 1

  return count, out_list

def count_inv(a):
  n = len(a)

  if n <= 1: return 0, a
  a_left = a[0 : n//2]
  a_right = a[n//2:]

  x, a_left = count_inv(a_left)
  y, a_right = count_inv(a_right)
  z, a = count_split_inv(a_left+a_right)

  return (x + y + z), a

test_list = [7, 3, 5, 1, 9, 2]
#test_list = []
#test_list = [1]
#test_list = [1, 2]
#test_list = [2, 1]
#test_list = [3, 2, 1]
#test_list = [6, 7, 5]
count, a = count_inv(test_list)

print("count", count)
print("a", a)
