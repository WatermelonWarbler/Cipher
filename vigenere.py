def main():
    word=input("Enter Word\n")
    key=input("Enter Key\n")
    word=word.upper()
    key=key.upper()
    if len(key) >= len(word):
        raise ValueError("Key can't be longer than Word")
    lk= len (key)
    for i in range(lk, len(word)):
        key+=key[i%lk]
    print("New key is {}".format(key))
    out=[]
    for i,l in enumerate(word):
        o=ord(l)+(ord(key[i])%65)
        if o>90:
            o-=26
        out.append(chr(o))
    print (''.join(out))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye!")
    except ValueError as e:
        print(e)
