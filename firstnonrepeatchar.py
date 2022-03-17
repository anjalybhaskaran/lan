from collections import Counter
def nonrepeatchar(string):
   freq=Counter(string)
   for i in string:
      if(freq[i]==1):
         print(i)
         break
string="anjali"
nonrepeatchar(string)