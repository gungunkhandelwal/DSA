def reverse_int(x):
        reverse_int=0
        while x >0:
            last_digit=x%10
            reverse_int= (reverse_int*10)+last_digit
            x//=10
        return reverse_int

n=123

# Can't handle for negative number

        