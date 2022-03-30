class Doc:
    def __init__(self, data, location):
        self.data = data
        self.location = location
        self.next = None
    
class Printer:
    def __init__(self, docList):
        self.count = 0
        self.head = None
        if len(docList) > 0:
            for location in range(len(docList)):
                priority = docList[location]
                self.append(Doc(priority, location))
        
    def append(self, doc):
        if self.head == None:
            self.head = doc
        else:
            now = self.head
            while now.next != None:
                now = now.next
            now.next = doc
        self.count += 1
    
    def popHead(self):
        poppedDoc = self.head
        self.head = self.head.next
        self.count -= 1
        poppedDoc.next = None
        return poppedDoc
    
    def isEmpty(self):
        if self.count == 0:
            return True;
        return False;
        
def solution(priorities, location):
    printer = Printer(priorities)
    
    priorities.sort(reverse=True)

    count = 0
    while printer.isEmpty:
        candid = printer.popHead()
        if candid.data != priorities[0]:
            printer.append(candid)
        else:
            count += 1
            del priorities[0]
            if candid.location == location:
                return count
        # print(candid.data, candid.location, candid.next, printer.count)
    return -1
  
#  정확성  테스트
# 테스트 1 〉	통과 (0.37ms, 10.2MB)
# 테스트 2 〉	통과 (2.26ms, 10.3MB)
# 테스트 3 〉	통과 (0.77ms, 10.1MB)
# 테스트 4 〉	통과 (0.12ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.23ms, 10.2MB)
# 테스트 7 〉	통과 (0.31ms, 10.1MB)
# 테스트 8 〉	통과 (2.13ms, 10.2MB)
# 테스트 9 〉	통과 (0.06ms, 10.2MB)
# 테스트 10 〉	통과 (0.25ms, 10.1MB)
# 테스트 11 〉	통과 (1.12ms, 10.3MB)
# 테스트 12 〉	통과 (0.11ms, 10.2MB)
# 테스트 13 〉	통과 (1.73ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.4MB)
# 테스트 15 〉	통과 (0.05ms, 10.2MB)
# 테스트 16 〉	통과 (0.10ms, 10.3MB)
# 테스트 17 〉	통과 (2.02ms, 10.3MB)
# 테스트 18 〉	통과 (0.03ms, 10.2MB)
# 테스트 19 〉	통과 (1.47ms, 10.3MB)
# 테스트 20 〉	통과 (0.33ms, 10.1MB)
