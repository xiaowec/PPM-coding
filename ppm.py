import math
import sys

k = 3
table = [{} for i in range(k+1)]
table[0] = {'': {}}
result = [[]]

def getProb(letter, table, eliminate):
    count = 0
    escapecount = 0
    sumcount = 0

    for key in table.keys():
	if key not in eliminate:
            sumcount += table[key]
            escapecount += 1

    if letter == '<$>':
        count = escapecount
    else:
        count = table[letter]

    sumcount += escapecount
    if sumcount == 0 and count == 0:
        return 1
    return float(count)/sumcount

def updateTable(letter, matchstr):
    for i in range(len(matchstr)+1):
	context = matchstr[i:len(matchstr)]
	length = len(context)

	if context not in table[length]:
	    table[length][context] = {}

	if letter in table[length][context]:
            count = table[length][context][letter]
            count += 1
	else:
	    count = 1

	table[length][context][letter] = count

def match(letter, matchstr):
    eliminate = []
    match = False

    for i in range(len(matchstr)+1):
        context = matchstr[i:len(matchstr)]
	length = len(context)

        #print context
	if context in table[length]:
            if letter in table[length][context]:
    		prob = getProb(letter, table[length][context],eliminate)
		tempresult = [letter, prob]
		result.append(tempresult)
		match = True
		break
            else:
                prob = getProb('<$>', table[length][context],eliminate)
   
                if prob < 1:
                    tempresult = ['<$>',prob]
            	    result.append(tempresult)

                for key in table[length][context].keys():
                    eliminate.append(key)

    if match == False:
     	prob = 1.0/(256 - len(table[0][''].keys()))
     	tempresult = [letter, prob]
     	result.append(tempresult)
    updateTable(letter, matchstr)

def PPM(text):
    for i in range(len(text)):
	if i <= k:
            matchstr = text[0:i]
	else:
	    matchstr = text[i-k:i]

	match(text[i], matchstr)

def getInfoBits():
    bits = 0

    for i in range(1,len(result)):
        bits += (-math.log(result[i][1])/math.log(2))

    return bits        

def main():
    file = open('input-xchu.txt','r')
    text = file.readlines()
    file.close()
    #text = text[0]
    print text    

    newtext = ''
    for i in range(len(text)):
        newtext += text[i]
    print '\n'
    print newtext

    rtext = ''
    for i in range(len(newtext)):
        rtext = newtext[i]+rtext
    print rtext
    PPM(newtext)

    #result_file = open('PPM_Result.txt','w')
    #for i in range(1,len(result)):
    #    result_file.write(str(result[i][0]))
    #    result_file.write(',')
    #    result_file.write(str(result[i][1]))
    #    result_file.write('\n')
    #result_file.close()

    for k in range(1,6):
        PPM(newtext)
        bits = getInfoBits()
        print 'the number of bits encoded when k=%d is %f' %(k,bits)

if __name__ == '__main__':
    main()
