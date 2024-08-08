def getDirs(i, rootdir):
    if i < 10:
        add = "00" + str(i)
    elif i < 100:
        add = "0" + str(i)
    else:
        add = str(i)
    known_dir = rootdir + add + "known01.txt"
    unknown_dir = rootdir + add + "unknown.txt"
    return known_dir, unknown_dir

def makeSentList(text_dir):
    sentenceList = []
    text = open(text_dir)
    for line in text:
        sentenceList.append(line.strip())
    return sentenceList
    
    
def lenFeatures(known, unknown):
    lenK = len(known)
    lenU = len(unknown)
    # calculate similarity
    if lenK > lenU:
        return float(lenU)/lenK
    else:
        return float(lenK)/lenU

def countNewL(known, unknown):
    countK = 0
    countU = 0
    for sent in known:
        if '' == sent:
            countK += 1
    for sent in unknown:
        if '' == sent:
            countU += 1
    if countK > countU:
        return float(countU)/countK
    else:
        return float(countK)/countU
    
def sentLength(known, unknown):
    knownLen = []
    unknownLen = []
    
    for sent in known:
        tokenCount = len(sent.split())
        if (tokenCount != 0):
            knownLen.append(tokenCount)
            
    for sent in unknown:
        tokenCount = len(sent.split())
        if (tokenCount != 0):
            unknownLen.append(tokenCount)
     
    kLenSum = 0   
    for sentLen in knownLen:
        kLenSum += sentLen
        
    knownMedianLen = float(kLenSum)/len(knownLen)
        
    uLenSum = 0
    for sentLen in unknownLen:
        uLenSum += sentLen
        
    unknownMedianLen = float(uLenSum)/len(unknownLen)
    
    if  unknownMedianLen > knownMedianLen:
        return float(knownMedianLen)/ unknownMedianLen
    else:
        return float(unknownMedianLen)/knownMedianLen
    
def wordLength(known, unknown):
    kSentTokenLen = 0
    kTokenCounter = 0
    for sent in known:
        tokens = sent.split()
        kTokenCounter += len(tokens)
        for token in tokens:
            kSentTokenLen += len(token)
            
    kMedianWordLen = float(kSentTokenLen)/kTokenCounter
    
    uSentTokenLen = 0
    uTokenCounter = 0
    for sent in unknown:
        tokens = sent.split()
        uTokenCounter += len(tokens)
        for token in tokens:
            uSentTokenLen += len(token)
            
    uMedianWordLen = float(uSentTokenLen)/uTokenCounter
    
    if kMedianWordLen > uMedianWordLen:
        return float(uMedianWordLen)/kMedianWordLen
    else:
        return float(kMedianWordLen)/uMedianWordLen         

def makeFeatures(known, unknown):
    return [lenFeatures(known, unknown), countNewL(known, unknown), sentLength(known, unknown), wordLength(known, unknown)]