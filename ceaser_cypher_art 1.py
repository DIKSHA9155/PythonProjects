def encrypt(word,shift_count,new_word_list):   
    for i in word:
        new_word_list.append(chr(ord(i) + shift_count))
    for j in new_word_list:
        print(str(j),end="")

def decrypt(word,shift_count,new_word_list):
    for i in word:
        new_word_list.append(chr(ord(i) - shift_count))
    for j in new_word_list:
        print(str(j),end="")

word = input("Enter a word : ")
new_word_list = []
print("1: Encrypt\n2: Decrypt\n")
choice = input("Enter your choice : ")
shift_count = int(input("Enter the shift count : "))
if choice == "Encrypt":
    encrypt(word,shift_count,new_word_list)
elif choice == "Decrypt":
    decrypt(word,shift_count,new_word_list)
