def sorter(x,y):
  result = []
  len1,len2 = len(x),len(y)
  i,j =0,0
  while i<len1 and j<len2:
    if x[i] < y[j]:
      result.append(x[i])
      i += 1
    else:
      result.append(y[j])
      j += 1
  result += x[i:]
  result += y[j:]
  return result

print(sorter([2, 4, 8, 11, 13, 14, 15, 19], [3, 4, 9]))
print(sorter([2, 4, 12], [3, 4, 9, 11, 12, 13, 14, 15]))


# if __name__ == "__main__":
#     print(sorter([2, 4, 8, 11, 13, 14, 15, 19], [3, 4, 9]))
#     print(sorter([2, 4, 12], [3, 4, 9, 11, 12, 13, 14, 15]))