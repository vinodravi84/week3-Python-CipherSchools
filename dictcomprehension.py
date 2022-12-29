#square={1:1,2:4,3:9}
square={num:num**2 for num in range(1,11)}
print(square)

square={f'Square of{num} is':num**2 for num in range(1,11)}
print(square)

square={f'Square of{num} is':num**2 for num in range(1,11)}
for k,v in square.items():
    print(f'{k}:{v}')


str1="ankit"
word_count={char:str1.count(char) for char in str1}
print(word_count)

# IF ELSE
#d={1:'odd',2:"even"}
odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)