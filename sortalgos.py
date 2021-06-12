import random, time

class Algorithm:
    def __init__(self,name):
        self.array = random.sample(range(4096),4096)
        self.name = name

    def update_display(self, swap1=None, swap2=None):
        import visualiser

        visualiser.update(self,swap1,swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

class SelectionS(Algorithm):
    def __init__(selF):
        super().__init__("SelectionS")

    def algorithm(self):
        for i in range(len(self.array)):
            min_index = 1
            for j in range(i+1,len(selF.array)):
                if selF.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.update_display(self.array[i], self.array[min_index])

class BubbleS(Algorithm):
    def __init__(self):
        super().__init__("BubbleS")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(selF.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                self.update_display(self.array[j],self.array[j+1])

class InsertionS(Algorithm):
    def __init__(self):
        super().__init__("InsertionS")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            index = i
            while index > 0 and self.array[index-1] > cursor:
                self.array[index] = self.array[index-1]
                index -=1
            self.array[index] = cursor
            self.update_display(self.array[index], self.array[i])

class ShellS(Algorithm):
    def __init__(self):
        super().__init__("ShellS")

    def algorithm(self):
        gap = len(self.array) // 2

        while gap > 0:
            for i in range(gap, len(self.array)):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j-gap] > temp:
                    self.array[j] = self.array[j-gap]
                    j -= gap
                self.array[j] = temp
                self.update_display(self.array[j], self.array[self.array[i]])
            gap //=2

class QuickS(Algorithm):
    def __init__(self):
        super().__init__("QuickS")

    def algorithm(self,array=[],start=0,end=0):
        if array == []:
            array = self.array
            end = len(array)
            if start < end:
                pivot = self.partition(array,start,end)
                self.algorithm(array,start,pivot-1)
                self.algorithm(array,pivot+1,end)

    def partition(self,array,start,end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i +=1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i],array[j])
        return i

class MergeS(Algorithm):
    def __init__(self):
        super().__init__("MergeS")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array)//2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        result = []
        i, j = 0, 0
        while i<len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
            self.update_display(left[i])
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result

class HeapS(Algorithm):
    def __init__(self):
        super().__init__("HeapS")

    def heapify(self,n,i):
        larget = i
        left = 2*i + 1
        right = 2*i +2
        if left <n and self.array[i]<self.array[left]:
            largest = left
        if right <n and self.array[largest] < self.array[right]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.update_display(self.array[i],self.array[largest])
            self.heapify(n,largest)

    def algorithm(self):
        n = len(self.array)
        for i in range(n,-1,-1):
            self.heapify(n,i)
        for i in range(n-1,0,-1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i,0)

class BucketS(Algorithm):
    def __init__(self):
        super().__init__("BucketS")

    def insertion_sort(self,b):
        for i in range(1, len(b)):
            up = b[i]
            j = i-1
            while j >=0 and b[j] > up:
                b[j+1] = b[j]
                j -=1
                b[j+1] = up
        return b

    def algorithm(self):
        bucket_size = 100
        min = self.array[0]
        max = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] < min:
                min = self.array[i]
            elif self.array[i] > max:
                max = self.array[i]
        bucket_count = ((max - min)//bucket_size) + 1
        bucket = []
        for i in range(0,len(self.array)):
            bucket[(self.array[i]-min)//bucket_size].append(self.array[i])
        k = 0
        for i in range(0,len(bucket_count)):
            buckets.append([])
        for i in range(0,len(self.array)):
            buckets[(self.array[i]-min)//bucket_size].append(self.array[i])
        k = 0
        for i in range(0, len(buckets)):
            self.insertion_sort(buckets[i])
            for j in range(0, len(buckets[i])):
                self.array[k] = buckets[i][j]
                self.update_display(self.array[k])
                k += 1

class RadixS(Algorithm):
    def __init__(self):
        super().__init__("RadixS")

    def algorithm(self):

        def counting_sort(self,exp):
            output = [0] * len(self.array)
            count = [0] * (10)
            for i in range(0, len(self.array)):
                idex = (self.array[i]//exp)
                count[int(index)%10] +=1
            for i in range(1,10):
                count[i] +=count[i-1]
            i = len(self.array)-1
            while i>= 0:
                index = (self.array[i]/exp)
                output[count[int(index)%10]-1] = self.array[i]
                count[int((index)%10)] -= 1
                i -= 1
            i = 0
            for i in range(len(self,array)):
                self.array[i] = output[i]
                self.update_display(self.array[i])

        maximum = max(self.array)
        exp = 1
        while maximum // exp > 0:
            counting_sort(self, exp)
            exp *= 10
