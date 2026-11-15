
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["qwe"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as e:
#     print(f"The key {e} does not exist.")
# else: # if try succeeds
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise TypeError("This is an error")

