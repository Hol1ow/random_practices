def longest_substring(input_str):
    if input_str.isdigit():
        res = []
        reminder = -1
        substring = ""
        for c in input_str:
            if int(c) % 2 != reminder:
                substring += c
            else:
                res.append(substring)
                substring = c
            reminder = int(c) % 2
    else:
        return
    
    return max(res, key=len)
    
print(longest_substring("225424272163254474441338664823"))
#"272163254"

print(longest_substring("594127169973391692147228678476"))
#"16921472"

print(longest_substring("721449827599186159274227324466"))
#"7214"