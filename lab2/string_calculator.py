class StringCalculator:
    def add(self, input_str):
        if input_str:
            
            if input_str[0:2] == '//':
                delimiter = input_str.split()[0][2:] 
                input_str = input_str[2:].replace(delimiter, ',')

            input_str = input_str.replace('\n', ',').lstrip(',')

            numbers = input_str.split(',')

            negative_numbers = [num for num in numbers if int(num) < 0]

            if negative_numbers:
                return "отрицательные числа запрещены: %s" % ','.join(negative_numbers)

            return sum([int(num) for num in numbers if int(num) <= 1000]) 
        
        return 0