def getRoadsPoints(sf, shapeval, show=False):    
    fields = sf.fields
    if show:
        print("Fields -> {0}".format(fields))
        
    itype=None
    iint=None
    if shapeval.startswith("Airport"):
        for i,val in enumerate(fields):
            if val[0] == "FAA_AIRPOR":
                itype = i-1
                break
    if shapeval.startswith("RailFeature"):
        for i,val in enumerate(fields):
            if val[0] == "LENGTHKM":
                itype = i-1
                break
    if shapeval.startswith("TrailSegment"):
        for i,val in enumerate(fields):
            if val[0] == "SOURCE_D00":
                itype = i-1
                break
    if shapeval.startswith("RoadSegment"):
        for i,val in enumerate(fields):
            if val[0] == "PERMANENT_":
                itype = i-1
                break
        iint=None
        for i,val in enumerate(fields):
            if val[0] == "INTERSTATE":
                iint = i-1
                break
                
    return itype,iint


def getRoadsData(shapeval, record, itype, iint, cntr):
    if shapeval.startswith("AirportPoint"):
        geoid = record[itype]
        name  = record[itype+1]
        test  = record[itype+2]
        try:
            int(test)
        except:
            return None
        return [geoid, name]
    elif shapeval.startswith("AirportRunway"):
        geoid  = record[itype]
        name   = record[itype+1]
        return [geoid, name]
    elif shapeval.startswith("RailFeature"):
        length = record[itype]
        name   = record[itype+3]
        geoid  = name
        return [geoid, name]
    elif shapeval.startswith("TrailSegment"):
        length = record[itype]
        name   = record[itype+3]
        geoid  = name
        return [geoid, name]
    elif shapeval.startswith("RoadSegment"):
        geoid  = record[itype]
        name   = record[itype+21]
        inter  = "-".join(record[iint:iint+4])
        usrte  = "-".join(record[iint+4:iint+8])
        strte  = "-".join(record[iint+8:iint+12])
        ctrte  = record[iint+12]
        street = record[iint+15]
        cntr[street] += 1
        extra  = [inter, usrte, strte, ctrte, street]

        ## Interstate
        isInterstate = False
        if inter != '---':
            isInterstate = True

        ## USRte
        isUSRte = False
        if usrte != '---':
            isUSRte = True

        ## StateRte
        isStateRte = False
        if strte != '---':
            isStateRte = True

        ## Highway
        isHighway = False
        try:
            if any([street.find(" {0}".format(x)) != -1 for x in ['Hw ', 'Hwy', 'Pkwy', 'Hwy', 'Fwy', 'Tollway', 'Expy']]):
                isHighway = True
        except:
            pass

        ## Major Road
        isMajorRd = False
        try:
            if any([street.find(" {0}".format(x)) != -1 for x in ['Ave', 'Blvd']]):
                isMajorRd = True
        except:
            pass

        ## Connections
        isConnection = False
        try:
            if any([street.find(" {0}".format(x)) != -1 for x in ['Bridge ', ' Bdg']]):
                isConnection = True
        except:
            pass
        
        return [geoid, name, cntr, isInterstate, isUSRte, isStateRte, isHighway, isMajorRd, isConnection]
    else:
        print(record)
        1/0
    
    print("No data is returned!!!")
    return None