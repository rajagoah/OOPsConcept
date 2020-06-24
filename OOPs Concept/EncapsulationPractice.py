class name:

    #initializing a constructor
    def __init__(self):
        self.first_name = 'Aakarsh'
        self.__last_name = 'Rajagopalan'

    #creating a private function
    def __CombiningFNLN(self):
        FN_LN = self.first_name + ' ' + self.__last_name
        return FN_LN

    #defining a function to print first and last name
    def PrintName(self):
        return '{} {} is the name of the person'.format(self.first_name, self.__last_name)


if __name__ == "__main__":
    #declaring and intializing a variable of type name
    candidate1 = name()

    try:
        #printing name
        print(candidate1.PrintName())
    except AttributeError:
        print('the function PrintName threw an error')

    try:
        #priting first name only
        print(candidate1.first_name)
    except AttributeError:
        print('the attribute first_name doesnt exist')

    try:
        #printing last name only
        print(candidate1.__last_name)
    except AttributeError:
        print('the attribute __last_name doesnt exist')

    try:
        print(candidate1.__CombiningFNLN())
    except AttributeError:
        print('the attribute __CombiningFNLN doesnt exist')
