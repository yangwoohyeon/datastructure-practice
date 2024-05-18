def selection_sort(a):
  for i in range(0,len(a)-1):
    minimum=i
    for j in range(i,len(a)):
      if a[minimum]> a[j]:
        minimum=j
      a[i],a[minimum]=a[minimum],a[i]
a=[4,2,9,49,29,30,19,39,65,60,72]
print(a)
selection_sort(a)
print(a)