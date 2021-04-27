def decider(w):
    first = w[0:len(w)//2] 
    second = w[len(w)//2 if len(w)%2 == 0 else len(w)%2 != 0:]
    print(w)
    print(first)
    print(second)
    str_first = [first]
    str_second = second
    for strings in str_first:
        print ("does %s match %s? %s" % (strings, str_second, strings == str_second))

w = "abab"
decider(w)
w = "aaaaaa"
decider(w)
w = "ababa"
decider(w)
w = "aaaabb"
decider(w)