#Tuition Increase Application 
#Jeremy Bargy
#Jan. 7, 2020

#Initialize variables
schoolName= '' #string
increaseLength = 0 #int
tuitionCost = 8000.00 #float
INCREASERATE = 0.03 #float
increaseAmount = 0 #float

# Create a variable to control the loop.
keep_going = 'y'
while keep_going == 'y':
    #Get user data input and validate.
    #Get school name data
    schoolName= input('Please enter the school name: \n')
    while (schoolName.isdigit()):
        print('Error: incorrect input: \n')
        schoolName= input('Please enter the school name: \n')

    #Get time length in years data
    increaseLength = (input('Please enter the length of time the tuition increases in years. i.e. 1 year will be entered as 1: \n'))
    while not(increaseLength.isdigit()) or int(increaseLength) < 1:
        print('Error: incorrect input: \n')
        increaseLength = input('Please enter the length of time the tuition increases in years. i.e. 1 year will be entered as 1: \n')
    increaseLength = int(increaseLength)

    #Calc tuition increase with a loop to occur increaseLength times.
    for count in range(1, increaseLength + 1):
        increaseAmount = tuitionCost * INCREASERATE #calc the increase amount of tuition.
        tuitionCost = tuitionCost + increaseAmount  #calc the new amount of tuition cost.
        #display school name, increase rate, count of loop, and the new tuition cost per semester.
        print(schoolName, ' with a ', format(0.03, '.0%'), ' tuition increase in year ', count, ' will experience a tuition cost per semester of $', format(tuitionCost, ',.2f'), sep='')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' + \
                       'commission (Enter y for yes): ')