class Primer:

    # constructor
    def __init__(self,seq):
        self.sequence = seq
        self.length = len(seq)
        self.gc = 0
        self.tm = 0
	self.returnInfo()

    def __str__(self):
        return 'Information for primer {}'.format(self.sequence)

    # return information about the primer
    def returnInfo(self):
        print("===================")
        print("Information about primer " + self.getSequence())
        print("GC Content: " + str(self.getGC()))
        print("Primer Length: " + str(self.getLength()))
        print("Melting Temp: " + str(self.getTm()))
        print("====================")

    # return length of the primer
    def getLength(self):
        return self.length

    # return GC content of the primer
    def getGC(self):
        return self.gc

    # return the sequence of the primer
    def getSequence(self):
        return self.sequence

    # return the melting temperature of the primer
    def getTm(self):
        return self.tm

p1 = Primer("ATTGCCC")
print(p1)

