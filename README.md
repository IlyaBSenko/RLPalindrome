# RLPalindrome
### Ever wondered how many palindromes exist in the rocket league scoreboard / timer?
#### Well we can write code to find out

#### This is a fun problem because this number is most often an odd number
#### The number takes the form of team1 + minute + seconds(2 digits) + team2
#### where team1, team2 are 0-9 and the timer counts m:ss with seconds 0-59.


#### Since we know that the 1st and last number will be 0 - 9
#### We can write a nested for loop for both numbers
```python
for team1 in range(10):               
    for team2 in range(10): 
```

#### The middle number is a little tricky but uses the same logic
#### We write a nested for loop inside the first, but with minutes for the first number 
#### and seconds as the second and third number

```python
for minutes in range(10):     
            for seconds in range(60):  
```

#### Now we need to format the number into a string and then check if that number is a palindrome

```python
s = f"{team1}{minutes}{seconds:02d}{team2}"

                if s == s[::-1]:
                    palindromes.append(s)
```

#### So the final product ends up being:
```python
import time

palindromes = []

for team1 in range(10):               
    for team2 in range(10):            
        for minutes in range(10):    
            for seconds in range(60):  
                
                s = f"{team1}{minutes}{seconds:02d}{team2}"

                if s == s[::-1]:
                    palindromes.append(s)

print(f"Found {len(palindromes)} palindromes")
```

#### This is fun to figure out as if you consistently play rocket league enough
#### you will notice that the scoreboard / timer is often a palindrome
#### more then you would think
