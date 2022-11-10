#Name: Kevin Loi
#Date: 11/4/2022
#Program: Lexical Scanner
#Course: CPSC 323 Compilers
file = open("input_scode.txt", "r")
# There are a lot more keywords/separators/operators/identifiers, but because the file for hw 
# doesn't have all of them, we are just going to keep it minimal to show we understand keywords/separators/operators/identifiers
keyword = ['while', 'for', 'if', 'else', 'elif']
separator = ['(', ')', ';']
operator = ['<', '=']
identifier = ['x', 'upper', 't', 's']

file_contents = file.read()
file_to_arr =  file_contents.split()

print(file_to_arr)
print("token               lexeme")
print("--------------------------")

str1 = ''
count = 0
while count < len(file_to_arr):
    count = count + 1
    for element in file_to_arr[count]:
        try:
            str_to_float = float(file_to_arr[count])
            print("real            ", file_to_arr[count])
            str1 = ''
        except:
            str1 += element
            if str1 in keyword:
                print("keyword            ", str1)
                str1 = ''
            elif str1 in separator:
                print("separator          ", str1)
                str1 = ''
            elif str1 in operator:
                print("operator           ", str1)
                str1 = ''
            elif str1 in identifier:
                print("identifier         ", str1)
                str1 = ''


        # if str1 in keyword:
        #     print("keyword            ", str1)
        #     count = count + 1
        #     str1 = ''
        # elif str1 in separator:
        #     print("separator          ", str1)
        #     count = count + 1
        #     str1 = ''
        # elif str1 in operator:
        #     print("operator           ", str1)
        #     count = count + 1
        #     str1 = ''
        # elif str1 in identifier:
        #     print("identifier         ", str1)
        #     count = count + 1
        #     str1 = ''
        # elif (str1 in file_to_arr[count]).isdigit():
        #     print("real               ", str1)
        #     count = count + 1
        #     str1 = ''
            

        # try:
        #     str_to_float = float(str1)
        #     if str_to_float.isdigit():
        #         print("real            ", file_to_arr[count])
        #         count = count + 1
        #         str1 = ''
        # except:
        #     print(file_to_arr[count])
            

        # elif type(str1) is float:
        #    print("real            ", file_to_arr[count])
        #    count = count + 1
        #    str1 = ''
        
        # if element in keyword:
        #     print("keyword            ", file_to_arr[count])
            
    # if file_to_arr[count] in keyword:
    #     print("keyword            ", file_to_arr[count])
    #     count = count + 9

# token = ['keyword', 'separator', 'identifier', 'operator', 'real']
# lexeme = ['while', '(', "x", "<", "upper", ")", "t", "=", "33.00", ";"] 

# dict = {'keyword':['while', 'for'], 'separator':['(', ')', ';'], 'identifer':['x','upper','t'], 'operator':['<','='], 'real':'33.00'} 