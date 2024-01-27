def convert_KB(KB):
    bytes=1024*KB
    bits=bytes/8
    megabyte=1024*KB
    gigabyte=1024*megabyte
    print("KB\t\tbits\t\tbytes\t\tmegabytes\tgigabytes")
    print(f"{KB}\t\t{bits}\t\t{bytes}\t\t{megabyte}\t\t{gigabyte}")
def main():
    no=1
    while(no<=10):
        kb=float(input("Please enter a file size in kilobytes (KB):"))
        if(kb>=0):
            convert_KB(kb)
        else:
            print("Invalid Input")
        no=no+1
main()
            
        
    
