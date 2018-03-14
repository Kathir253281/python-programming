print("Enter '0' for exit.");
ch = input("Enter the character: ");
if ch == '0':
    exit();
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print(ch, "is a alphabet.");
    else:
    	print(ch, "is not a alphabet.");
