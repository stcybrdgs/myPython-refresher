# copying binary data to external file

def main():
    infile = open('jazzNlady.jpg', 'rb') # read binary
    outfile = open('jazzNlady-copy.jpg', 'wb') # write binary
    while True:
        # choose 10240 (ie, 10kb) as amount to read at a time
        # rem you don't know how big the file is, ans you want
        #     to choose a reasonable size of info to read at a time
        buf = infile.read(10240) 
        if buf: # write if there is something in the buffer
            outfile.write(buf) # write what is in buffer to ext file
            print('.', end='', flush=True)
        else: break # break if the buffer is empty
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
