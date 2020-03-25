# Strings and bytes are not directly interchangeable
# Strings contain unicode and bytes are raw 8-bit values

def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # Trying to combine them
    # print(s+b) this gives error
    print(s+str(b)) # Not a good solution

    s2 = b.decode('utf-8')
    print(s+s2) # now is better

    b2 = s.encode('utf-8')
    print(b+b2) # you can also do this to Bytes
    
    b3 = s.encode('utf-32')
    print(b3)


if __name__ == "__main__":
    main()