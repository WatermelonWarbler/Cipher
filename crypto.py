def main():
    word=input("enter word\n")
    out=[]
    shift=input("enter number\n")
    for c in word:
        o=chr(ord(c)+int(shift))
        out.append(o)
    print(''.join(out))
    
if __name__ == "__main__":
    main()
