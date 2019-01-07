class Duck():
    def __inti__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the pertter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = Duck('Howard')
fowl.name
fowl.name = 'Dounald'
fowl.name
fowl.__name
fowl._Duck__name
