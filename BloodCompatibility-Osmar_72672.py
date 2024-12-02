# Osmar Principe - 72672
# osmarprincipe98@gmail.com

# List with blood receives possibilities data's to check the input and give the answer.

blood_receives = {
    'A+': ['A+', 'A-', 'O+', 'O-'],
    'A-': ['A-', 'O-'],
    'B+': ['B+', 'B-', 'O+', 'O-'],
    'B-': ['B-', 'O-'],
    'AB+': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
    'AB-': ['A-', 'B-', 'AB-', 'O-'],
    'O+': ['O+', 'O-'],
    'O-': ['O-']
}

# List with blood gives possibilities data's to check the input and give the answer.


blood_gives = {
    'A+': ['A+', 'AB+'],
    'A-': ['A+', 'A-', 'AB+', 'AB-'],
    'B+': ['B+', 'AB+'],
    'B-': ['B+', 'B-', 'AB+', 'AB-'],
    'AB+': ['AB+'],
    'AB-': ['AB+', 'AB-'],
    'O+': ['A+', 'B+', 'AB+', 'O+'],
    'O-': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
}

# List with the blood possibilities to input.

X = [ 'A+' , 'A-' , 'B+' , 'B-' , 'AB+' , 'AB-' , 'O' , 'O-' ]

# Function for blood receives , with condition to check if user typed the right input.

def blood_type_receives (answer):
    if answer not in X:
        print ('Invalid blood type:' , answer + '.' , 'please try again.')
    else:
        print ('Blood type' , answer , 'can receive donations from:' , blood_receives.get(answer,[]))

# Function for blood donators , with condition to check if user typed the right input.

def blood_types_gives (answer):
    if answer not in X :
        print ('Invalid blood type:' , answer + '.', 'please try again.')
    else:
        print ('Blood type' , answer , 'can donate to:', blood_gives.get(answer ,[]))

# Main program code.

# Frist messages when starting the program.

print ('Welcome to the Blood Type Compatibility checker!')
print ('--------------------------------------------------------')

# Loop begnning to ask what what the users would like to do.

choice = 0
while choice != 'end' :
    print (' ')
    print ('choose an option:')
    print ('1. Check who can donate to your blood type.')
    print ('2. Check who you can donate blood to.')
    print ('3. Exit the program.')
    print ('')
    choice = int(input('Enter your choice (1,2,3):'))
    if choice == 1:
        blood_type_receives (answer = input('Enter your blood type(e.g. , A+, O-, AB+):'))
    elif choice == 2:
        blood_types_gives (answer = input('Enter your blood type(e.g. , A+, O-, AB+):'))
    elif choice == 3:
        choice = 'end' 
    else :
        print ('Invalid choice! Please enter 1, 2, or 3.')

# final message
print ('Thank You for using the Blood Type Compatibility Checker. Goodbye!')

