s = 'zyxwvutsrqponmlkjihgfedcba'
##count = 0
##for char in range(len(s) - len('bob') + 1):
##        if s[char:char+len('bob')] == 'bob':
##                count += 1
##print(count)


alphabet = ''
for i in range(len(s)): #begin start of substring
    for j in range(i, len(s)): #for each start of substring set the end of substring
        s1 = s[i:j+1] #create a substring with between i and j+1
        print(s1)
        if ''.join(sorted(s1)) == s1: #sort the substring to see if the substring is already sorted
            print(alphabet)
            print(s1)
            alphabet = max(alphabet, s1, key=len) #if in order compare to prior substrings and find the max length
        else:
            break
print(alphabet)
