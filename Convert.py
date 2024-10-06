class Convert:
    
    def to_decimal_conv(number: str, base: str) -> tuple[str, bool]:
        
        def int_conv(numbers: list, base: int):
            
            output = 0
            
            for i in range(len(numbers)):
                addon = (int(numbers[-(i+1)])) * (base**i)
                output += addon
            
            return output

        def float_conv(numbers: list, base: int):
            
            output = 0
            
            for i in range(len(numbers)):
                addon = (int(numbers[i])) * (1 / (base ** (i + 1)))
                output += addon
            
            return output

        def validate_input_number(number: str) -> bool:
            valid_chars = ('A', 'a', 'B', 'b','C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 
                            'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 
                            'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q',
                            'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W',
                            'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '.', '1', '2', '3', 
                            '4', '5', '6' , '7', '8', '9'
                            )  
            
            if list(number).count('.') not in (0, 1):
                return False
            else:
                if number[-1] == '.' or number[0] == '.':
                    return False 
                for char in list(number):
                    if char not in valid_chars:
                        return False            
            return True
        
        def validate_base(base: str) -> bool:
            try: 
                int(base)
            except ValueError:
                return False
            return True
        
        
        def range_check(number: str, base: int) -> bool:
            number = list(number)
            if base > 10:
                try:
                    number = assign_values(number, base)
                except IndexError:
                    return False
            for n in number:
                if n != '.':
                    if int(n) >= base:
                        return False
            return True

        def assign_values(number: list, base: int) -> list: 
            letters = (('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ('F', 'f'), 
                                ('G', 'g'), ('H', 'h'), ('I', 'i'), ('J', 'j'), ('K', 'k'), ('L', 'l'), 
                                ('M', 'm'), ('N', 'n'), ('O', 'o'), ('P', 'p'), ('Q', 'q'), ('R', 'r'), 
                                ('S', 's'), ('T', 't'), ('U', 'u'), ('V', 'v'), ('W', 'w'), ('X', 'x'), 
                                ('Y', 'y'), ('Z', 'z'))     
            values = [x for x in range(10, base)]
            for char in list(number):
                if char != '.':
                    for letter in letters:
                       if char in letter:
                        if values[letters.index(letter)] >= base:
                            raise IndexError  
                        number[number.index(char)] = values[letters.index(letter)]
                                                
            return number
                        
        
        output_str = ''
        int_out: int = 0
        float_out = '.00'
        is_float = False
        
        if not validate_input_number(number):
            output_str = " Error! invalid input for ' Number ' "
        else:
            if not validate_base(base):
                output_str = " Error! invalid input for ' Base ' "
            else:
                if '.' in list(number):
                    is_float = True
                    float_point_index = number.index('.')
                    
                base = int(base)
                
                if not range_check(number, base):
                    output_str = " \tError! invalid input for ' Base '\nBase must be greater than any index of the number "
                else:
                    number = assign_values(list(number), base)
                    if not is_float: 
                        number = [int(i) for i in number]   
                        int_out = int_conv(number, base)
                        output_str = f"Base 10 Number :  {int_out}" + float_out     
                    else:
                        number = [int(i) if number.index(i) != float_point_index else '.' for i in number]
                        int_part, float_part = number[:number.index('.')], number[number.index('.')+1:]
                        int_out = int_conv(int_part, base)
                        float_out = float_conv(float_part, base)
                        output_str = f"Base 10 Number :  {int_out+float_out}"
                                                                                
        return output_str
            
    

    def decimal_conv(number, base):
        
        def validate_number(number: str) -> bool:
            valid_chars = ('.', '1', '2', '3','4', '5', '6' , '7', '8', '9', '0')  
            if number.count('.') in (0, 1):
                for char in list(number):
                    if char not in valid_chars:
                        return False
            else:
                return False
            return True
        
        def validate_base(base: str) -> bool:
            try: 
                if base == '1':
                    return False
                int(base)
            except ValueError:
                return False
            return True
    
        def letters_assign(num: int, base: int) -> str:
            letters = ("A", "B", "C", "d", "E", "F", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
            values = list((i for i in range(10, base)))
            for value in values:
                if num == value:
                    try:
                        letter = letters[values.index(value)]
                        break
                    except IndexError:
                        print("\n\n\tERROR :: EXCEEDED THE LIMIT OF CHARACTERS!\n\n")
                        exit()
            return letter


        def int_conv(number: int, base: int) -> str:
            output = []
            while number > 0:
                mode = number % base
                if base > 9 and mode in range(10,base):
                    mode = letters_assign(mode, base)
                output.insert(0, str(mode))
                number //= base
            output = ''.join(output)
            return output
        

        def float_conv(float_part: int, base: int) -> str:
            float_value = []
            fp = 0
            while fp < 10:
                val = float_part * base
                float_part_len = len(str(float_part))
                if float_part_len < len(str(val)):
                    float_part = list(str(val))[-float_part_len:]
                    float_part = int(''.join(float_part))
                    rest = list(str(val))[:-float_part_len]
                    rest = int(''.join(rest))
                elif float_part_len == len(str(val)):
                    float_part = val
                    rest = 0
                else:
                    rest = 0
                float_value.append(rest)
                if float_part == 0:
                    break
                fp+=1
            for i in float_value:
                if i > 9 :
                    float_value[float_value.index(i)] = letters_assign(i, base)
            float_value = ''.join([str(x) for x in float_value])
            return float_value


        output_str = ''
        float_part = '.00'
        float_number = False
        
        
        if not validate_number(number):
            output_str = " Error! invalid input for ' Number ' "
        else:
            if not validate_base(base):
                output_str = " Error! invalid input for ' Base ' "
            else:
                if not number.count('.')  == 0:
                    float_number = True
        
                base = int(base)
                
                if not float_number:
                    int_part = int_conv(int(number), base)
                    output_str = f"Base {base} number : " + int_part + float_part
                else:
                    int_part, float_part = number.split('.')
                    int_out = int_conv(int(int_part), base)
                    float_out = float_conv(int(float_part), base)
                    float_out = ''.join(float_out)
                    output_str = f"Base {base} number : " + int_out + '.' + float_out
                    
        return output_str
    