def findMultiples(n):
        a = 3
        b = 5
        for i in range(1,n+1):
                s = ""
                # print  multiple of 3
                if (i == a):
                        a = a + 3
                        s = s + "AVA"

                # print multiple of 5
                if (i == b):
                        b = b + 5
                        s = s + "AMO"
                if (s == ""):
                        print(i)
                else:
                        print(s)

# Driver Code
if __name__ == '__main__':
        findMultiples(100)
