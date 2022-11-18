import secrets
class Password:
    def __init__(self, tuple_of_strs, length):
        self.length = length
        self.tuple_of_strs = tuple_of_strs
        self.signs_list = ''
        for i in tuple_of_strs:
            self.signs_list += ''.join(i)
        self.signs_list = list(self.signs_list)
    
    def generate(self):
        password = ''
        for stroka in self.tuple_of_strs:
            password += ''.join(secrets.choice(stroka))
        for i in range(self.length - len(self.tuple_of_strs)):
            password += ''.join(secrets.choice(self.signs_list))
        return password
            

abc = 'abcdefghijklmnopqrstuvwxyz'
abc_upper = abc.upper()
numbers = '0123456789'
tpl = (abc_upper, abc, numbers)
parol = Password(tuple_of_strs=tpl, length=7)
print(parol.generate())