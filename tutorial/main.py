
class Object:
    '''
    Class which holds two numbers, but lacks any operatios for them


    Attributes
    ----------
    a : int/float
        first number
    b : int/float
        second number

    Methods
    ----------
    summer()
        sums the two numbers
    '''


    def __init__(self, a, b):
        '''
        Init method for Object; defines the two numbers we are implementing operations for

        Parameters        
        ----------
        a : int/float
            first number
        b : int/float
            second number

        Returns
        ----------
        -
        '''

        self.a = a
        self.b = b

    
    def summer(self):
        '''
        Should return sum of self.a and self.b
        '''
        raise NotImplementedError('implement me')


def main():
    
    num1 = 5
    num2 = 7

    obj = Object(num1, num2)

    print(f'We have summed numbers {obj.summer()}')



if __name__ == '__main__':
    main()
