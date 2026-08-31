#!/usr/bin/python3

import sys
from urllib.parse import quote, urlparse
from pymd5 import md5, padding


##########################
# Example URL parsing code:
res = urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

    #################################
    # Your length extension code here
    # Sprinklers success: token=1d81e182d450db1891e94e8d9ececfaf&command=SprinklersPowerOn
    # Turn Clocks off success: token=de9a6e15ab5f78c443bcbdfacf534025&command=ClockPowerOff&command=NoOp&command=ClockPowerOn
    # Unlock Safes blank: https://project1.ecen4133.org/joza7988/lengthextension/api?token=&command=UnlockSafes
    # Secret password will always be 8 bytes long
    # To create the final token, need to create H(secret || command || padding || newCommand)
    # Need to add the padding to the URL as well!

    # Parse the supplied URL to extract the token and command parameters
    res = urlparse(url)
    #print("URL:", res)
    query = res.query
    #print("Query:", query)

    # Collect the token
    token = query.split("token=")[1].split("&")[0]
    #print("Token:", token)

    #Collect the previous commands
    command = query.split(f"token={token}&", 1)[1]
    #print("Command:", command)

    # Get size of the message in bits including the 8byte secret
    commandLength = len(command) + 8
    pads = padding(commandLength * 8)
    bits = (commandLength + len(pads))*8

    # Command we want to extend with
    unlockCommand = "&command=UnlockSafes"

    # Take the token and MD5 length extend unlock command
    newToken = md5(state=bytes.fromhex(token), count=bits)
    newToken.update(unlockCommand)
    #print("New Token:", newToken.hexdigest())

    # Construct the new URL with the extended token and command
    newUrl = f"{res.scheme}://{res.netloc}{res.path}?token={newToken.hexdigest()}&{command}{quote(pads)}{unlockCommand}"
    print(f"{newUrl}")