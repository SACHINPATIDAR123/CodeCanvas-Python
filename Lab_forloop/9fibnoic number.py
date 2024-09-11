#Question.9 Python program to get the Fibonacci series between 0 to 55

'''The Fibonacci sequence is a series of numbers where each number is the sum
of the two preceding ones. It typically starts with 0 and 1.The sequence can
be defined by the recurrence relation'''

# here initialize an empty list for the Fibonacci series

fibseries = []

# in Loop we take nummber upto 55
for i in range(55):
# it Add the first two numbers (0 and 1) to the list
    if i <= 1:
        fibseries.append(i)
    else:
# Calculate the next Fibonacci number

        nextfib = fibseries[i-1] + fibseries[i-2]
# Add it to the list if it's 55 or less

        if nextfib <= 55:
            fibseries.append(nextfib)
        else:
# Stop if the number is greater than 55

            break

# Print the Fibonacci series
print(fibseries)
