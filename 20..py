text=input("one","two", "three", "four", "five", "six")
for i in text:
    if (len(i)>longest):
       longest =len(i)
       logest_word = i
print(" the longest word is", longest_word,"with length", len(longest_word))
