class Difference:
    def __init__(self, a):
        self.__elements = a
        self.hold = []
        self.maximumDifference = 0
    def computeDifference(self):
        i = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                x = abs(self.__elements[i] - self.__elements[j])
                if x not in self.hold:
                    self.hold.append(x)
        
        self.maximumDifference = max(self.hold)




	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)