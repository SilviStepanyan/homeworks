#capitalize
 def capitalize(string):
     return chr(ord(string[0]) - 32) + string[1:]


#count
 def count(string, substring):
     cnt = 0
     word_list = string.split()
     for i in word_list:
         if(i == substring):
             cnt += 1
     return cnt;


#endswith
 def endswith(substr1, str1):
     if substr1 == str1[-len(substr1):]:
         return True
     else:
         return False


#find  non
def find(string, el):
    for i in range(0, len(string)):
        if string[i] == el:
            return i


#join
 def join(separator, iterable):
     str1 = ""
     for el in iterable:
         str1 += el + separator
     return str1[:len(str1) - 1]


#startswith
 def startswith(substr5, str5):
     if substr5 == str5[:len(substr5)]:
         return True
     else:
         return False


#strip
 def strip(str):
     return " ".join(str.split())


#lower
def lower(string):
    for i in string:
        if ord(i) in range(65, 91):
         modStr =  string.replace(i, chr(ord(i) + 32))
    return modStr

