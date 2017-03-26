def main():
    word=input("enter word\n")
    out=[]
    shift=input("enter number\n")
    for c in word:
        try:
            o=chr(ord(c)+int(shift))
        except ValueError:
            print ("Invalid Input")
            exit(1)
        out.append(o)
    print(''.join(out))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye!")
