# check if email is valid

import sys
for line in sys.stdin:
    try:
        name = line.split('@')[0]
        domain = line.split('@')[1].split('.')[0]
        tld = line.split('@')[1].split('.')[1]
        if len(name) > 0 and len(domain) > 0  and len(tld) != 3:
            valid_tlds = ['com','org','edu']
            for i in range(0,3):
                if tld[i] != valid_tlds[0][i]:
                    if tld[i] != valid_tlds[1][i]:
                        if tld[i] != valid_tlds[2][i]:
                            print("false")
                break
            print("true")
        else:
            print("false")
    except:
        print("false")
