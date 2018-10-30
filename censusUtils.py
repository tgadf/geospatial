def getCensusPoints(sf, show=False):    
    fields = sf.fields
    if show:
        print("Fields -> {0}".format(fields))

    ipop=None
    for i,val in enumerate(fields):
        if val[0] == "DP0010001":
            ipop = i-1
            break

    ihouse=None
    for i,val in enumerate(fields):
        if val[0] == "DP0130001":
            ihouse = i-1
            break

    ihouseocc=None
    for i,val in enumerate(fields):
        if val[0] == "DP0180001":
            ihouseocc = i-1
            break

    return ipop,ihouse,ihouseocc

            
def getCensusData(pops,house,occpy):
    pop    = pops[0]
    try:
        young  = round(float(sum(pops[1:5]))/pop,2)
        adult  = round(float(sum(pops[5:12]))/pop,2)
        old    = round(float(sum(pops[12:]))/pop,2)
    except:
        young = 0.0
        adult = 0.0
        old   = 0.0

    nhouse  = house[0]
    try:
        ffamily = round(float(house[1])/nhouse,2)
    except:
        ffamily = 0.0
    nhouseunits = occpy[0]
    try:
        foccpy = round(float(occpy[1])/nhouseunits,2)
    except:
        foccpy = 0.0

    return {"Housing": [nhouse,ffamily], "Occupancy": [nhouseunits, foccpy], "Pop": [pop,young,adult,old]}
            
        

def getCensusName(mtype, name, memi):
    if mtype == "CBSA":
        ptype = None
        if isinstance(name,str):
            if name.find("Metro Area") != -1:
                memi = "Metro"
                name = name.replace("Metro Area", "").strip()
            elif name.find("Micro Area") != -1:
                memi = "Micro"
                name = name.replace("Micro Area", "").strip()
            else:
                print(name)
                1/0

    if mtype == "CSA":
        ptype = None
        if isinstance(name,str):
            if name.find(" CSA") != -1:
                name = name.replace(" CSA", "").strip()
            else:
                print(name)
                1/0

    if mtype == "Place":
        ptype = None
        if isinstance(name,str):
            name = name.replace("(balance)", "").strip()
            if name.endswith(" city"):
                memi = "City"
                name = name[:-5]
            elif name.endswith(" municipality"):
                memi = "Municipality"
                name = name[:-13]
            elif name.endswith(" borough"):
                memi = "Borough"
                name = name[:-8]
            elif name.endswith(" city and borough"):
                memi = "City/Borough"
                name = name[:-17]
            elif name.endswith(" town"):
                memi = "Town"
                name = name[:-5]
            elif name.endswith(" CDP"):
                memi = "CDP"
                name = name[:-4]
            elif name.endswith(" village"):
                memi = "Village"
                name = name[:-8]
            elif name.endswith(" unified government"):
                memi = "Unified Government"
                name = name[:-19]
            elif name.endswith(" consolidated government"):
                memi = "Consolidated Government"
                name = name[:-24]
            elif name.endswith(" metro government"):
                memi = "Metro Government"
                name = name[:-17]
            elif name.endswith(" metropolitan government"):
                memi = "Metropolitan Government"
                name = name[:-24]
            elif name.endswith(" urban county"):
                memi = "Urban County"
                name = name[:-13]
            elif name.endswith(" County"):
                memi = "County"


    if mtype == "MetDiv":
        ptype = None
        if isinstance(name,str):
            if name.find("Metro Area") != -1:
                memi = "Metro"
                name = name.replace("Metro Area", "").strip()
            elif name.find("Micro Area") != -1:
                memi = "Micro"
                name = name.replace("Micro Area", "").strip()
            else:
                print(name)
            
    return name,memi