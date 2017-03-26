def main():
    word=input("enter word\n")
    out=[]
    for c in word:
        o=chr(ord(c)+1)
        out.append(o)
    print(''.join(out))

if __name__ == "__main__":
    main()
