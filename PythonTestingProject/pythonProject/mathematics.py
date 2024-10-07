

class Mathematics:

    def multiply_them(self,*args, total=1):
         for arg in args:
             total *= arg
         return total

    def sum_them(self ,*args, total=0):
        for arg in args:
            total += arg
        return total