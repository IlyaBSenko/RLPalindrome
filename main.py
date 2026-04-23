import time

palindromes = []

# Huuuuuge nested loop, but its chill because it's only 10*10*10*60 = 60,000 iterations
for team1 in range(10):                # 0-9
    for team2 in range(10):            # 0-9
        for minutes in range(10):      # 0-9
            for seconds in range(60):  # 0-59
                
                s = f"{team1}{minutes}{seconds:02d}{team2}"

                if s == s[::-1]:
                    palindromes.append(s)

print(f"Found {len(palindromes)} palindromes")

# if you want to see the specific palindromes
for p in palindromes:
    print(p)
    time.sleep(.005)
    # then just import time at the top

