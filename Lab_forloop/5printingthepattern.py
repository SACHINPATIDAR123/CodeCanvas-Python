#Question.5 print the pattern   
'''
          *

         ***

        *****

       *******

      *********
 '''


# Number of lines in the pattern is
n = 5

# Loop from 1 to n to print each line
for i in range(1, n + 1):
    
# Print leading spaces to center the stars
    print(' ' * (n - i), end='') 
    
# Print stars, increasing order by 2 in each line
    print('*' * (2 * i - 1))
