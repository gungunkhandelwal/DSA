def longestCommonPrefix(strs):
    res='' 
    print(strs[0])
    print(len(strs[0]))
    for i in range(len(strs[0])):
        print(f"i am {i}")
        for s in strs:
            print(f"hoooo {s}")
            print(f"s[i] {s[i]}")
            print(f"strs[0][i]. {strs[0][i]}")
            if i == len(s) or s[i] != strs[0][i]:
                print('❤️')
                return res
            print(f"i am res {res}")
        res+=strs[0][i]
    return res

strs=["flower","flow","flight"]
print(longestCommonPrefix(strs))

# Time complexit O(n). and space complexity O(1)