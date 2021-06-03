s
import requests
from requests_toolbelt.adapters import host_header_ssl

# Create a new requests session
#s = requests.Session()

# Mount the adapter for https URLs
#s.mount('https://', host_header_ssl.HostHeaderSSLAdapter())

#def main():

        #print(res.text)
    #subprocess.call(["curl", "192.168.68.121:5000"])
    #os.system("curl 192.168.68.121:5000")
    #stream = os.popen("curl 192.168.68.121:5000")
    

import pycurl
from io import BytesIO 

def main():
    stream = os.popen("curl -s 192.168.68.121:5000", 'r', 1)
    while True:
        line = stream.readline()
        parseData(line)
        

def parseData(line):
    #$GPGGA,  061456,3726.866520,N, 12154.805533,W,    1,    12,     ,     4.8,M,   -31.8,M,     ,          *52
    # ID,    TIME,   LATITUDE,     LONGITUDE      ,  FIX,     #, HDOP,         alt,   height, time, dgps id, checksum
    if "$GPGGA" in line:
        tokens = []
        token = ""
        for letter in range(len(line)):
            if line[letter] == ',':
                tokens.append(token)
                token = ""
            elif letter == len(line) - 1:
                token += line[letter]
                tokens.append(token)
            else:
                token += line[letter]
        print(line)
        print("ID: " + tokens[0])
        print("TIME: " + tokens[1])
        print("LATITUDE: " + tokens[2] + tokens[3])
        print("LONGITUDE: " + tokens[4] + tokens[5])
        print("FIX: "+ tokens[6])
        print()
    
    #b_obj = BytesIO() 
    #crl = pycurl.Curl() 
    #crl.setopt(crl.VERBOSE, True)

    # Set URL value
    #crl.setopt(crl.URL, '192.168.68.121:5000')
    #crl.setopt(pycurl.USERAGENT, 'curl/7.55.1')

    #while True:
    #    # Write bytes that are utf-8 encoded
        #crl.setopt(crl.WRITEDATA, b_obj)

        # Perform a file transfer 
        #crl.perform() 

        # End curl session
        #crl.close

        # Get the content stored in the BytesIO object (in byte characters) 
        #get_body = b_obj.getvalue()

        # Decode the bytes stored in get_body to HTML and print the result 
        #print('Output of GET request:\n%s' % get_body.decode('utf8')) 


if __name__ == '__main__':
    main()