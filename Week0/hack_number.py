def hack_number(number):
    while True:
        i = int(number) + 1
        binary = str(bin(i))
        cnt_ones = 0
        result = False
        # print(binary[2::1])
        # print(binary[:1:-1])
        if binary[2::1] == binary[:1:-1]:
            # print("palindrome")
            # print(binary)
            for digit in binary:
                if digit == "1":
                    # print("plus 1")
                    cnt_ones += 1
        if cnt_ones % 2 == 1:
            return i
        else:
            number += 1


print(hack_number(10))
print(hack_number(8031))
