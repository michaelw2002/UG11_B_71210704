def check_data_type(data1,data2):
    data2 = data2.lower()
    if (type(data1) == str and (data2) == "str"):
        print("Jawaban Anda benar")
        return True
    elif (type(data1) == int and (data2) == "int"):
        print("Jawaban Anda benar")
        return True
    elif (type(data1) == int and (data2) == "str"):
        print("Jawaban Anda salah, seharusnya adalah: int")
        return False
    else:
        print("Jawaban Anda salah, seharusnya adalah: str")
        return False
print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))
