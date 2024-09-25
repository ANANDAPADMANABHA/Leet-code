class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights),sum(weights)
        
        def can_ship_in_days(capacity):
            total,num_of_days = 0,1
            for weight in weights:
                if total+weight > capacity:
                    num_of_days+=1
                    total = 0
                total += weight
                
                if num_of_days > days:
                    return False
                
            return True
                    
        
        while low<= high:
            mid = (low+high)//2
            if can_ship_in_days(mid):
                high = mid-1
            else:
                low = mid+1
                
        return low
                