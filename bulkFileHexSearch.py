# Bulk File Hex Search - by Jace Voracek

#Change this to your directory along with the hex sequence you wish to search.
#Examples: 7C58A82B, B401F4E8FF7C5046 
findMe = "00aabbccddeeff"
myDir = "dir/"



import os
import csv
import binascii
import sys

print("Let's do this! Now searching for all instances of: " + findMe + " in " + myDir + "... ");

log = open("BulkFileHexSearchResults.txt", "a")
sys.stdout = log

for file in os.listdir(myDir):
    print("Starting file: " + file)
    with  open(myDir + file, 'rb') as fp:
        isDuplicate = 0
        while True:
            piece = fp.read(1000000)
            if not piece:
                break
            hexContents = str(binascii.hexlify(piece))
            hexContents = hexContents[2:]
            offsetCount = 0
            #Search for the following hex sequence:
            for entry in [hexContents[i:i+40] for i in (range(0, len(hexContents), 32))]:
                
                if str(findMe) in str(entry):
                    #addOffset = str(hex(offsetCount))
                    print(entry + " FOUND")
                    isDuplicate = isDuplicate + 1
                offsetCount = offsetCount + 16
            
        if (isDuplicate > 1):
            print("FOUND DUPLICATE!!")
    
    print("Finished! :-)")
    
    