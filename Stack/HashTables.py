def repeatingChar(s):
    hash_dict={}
    for char in s:
        hash_dict[char]=hash_dict.get(char,0)+1
    
    for char in s:
        if hash_dict[char] >1:
            return char
    return None

print(repeatingChar("coding"))  
print(repeatingChar("level"))   
print(repeatingChar("aabbcc"))   
print(repeatingChar("abcabc"))   

        