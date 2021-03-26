def trasformaIpInBit(ipDec):
    ipBin = ""
    for gruppo in ipDec.split("."):
        byte =  bin(int(gruppo)).replace("0b", "")
        print(len(byte))
        
        for c in range(8-len(byte)):
            ipBin+="0"
        
        ipBin += byte #+ "."

    return ipBin

def broadcast(ipBin, nBitHost):
    #ipBoad = 
    pass


def main():
    ipDec = "192.168.100.0" #input("inserisci l'ip della rete")
    nBitHost = 24 #int(input("numero di bit per la sottorete"))
    broadcast(trasformaIpInBit(ipDec), nBitHost)

if __name__ == "__main__":
    main()