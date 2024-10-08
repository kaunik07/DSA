# KAUNIK
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        np = len(processorTime)
        nt = len(tasks)

        processorTime.sort(key=lambda x:x , reverse=True)
        
        #same sort as task.sort()
        tasks.sort(key=lambda x:x) 
        

        res = 0
        j = 3
        for i in range(np):
            # print(j)
            res = max(res, tasks[j]+processorTime[i])
            j+=4

        return res
            
            


