# Bad Python code

def myfunc(x):
    # This function prints square of number if it's positive, 
    # but returns a string if it's negative.
    if x >= 0:
        print("The square of", x, "is", x*x)
    else:
        return "Negative numbers are not allowed."

numbers = [1, 2, -3, 4, 'five', 6, 7.0, 8]

result = []
for i in range(len(numbers)):
    result.append(myfunc(numbers[i]))

print(result)