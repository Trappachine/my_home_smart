class poli:
    def __init__(self,stri):
        self.stri=stri
    def pl(self):
        revers_str=''.join(reversed(self.stri))
        if revers_str == self.stri:
            print(f'{self.stri} is polindrome')
        else:
            print(f'{self.stri} is not a polindrome')
a=poli('rar')
a.pl()
