#while loop
print("Enter a number:")
no = int(input())
while(no>4):
    print("hareem")
    no = int(input())
    if (no == 1):
        break
    if (no==3):
        continue
    print("Loop ended")