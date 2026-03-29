class Solution(object):
    def defangIPaddr(self, address):
        f=0
        defa=""
        for i in range(len(address)):
            if address[i]==".":
                de=address[f:i] + "[.]"
                f=i+1
                defa = defa[:] + de[:]
        defa = defa[:] + address[f:]
        return defa
