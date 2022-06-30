class Solution:
    def trap(self, height: List[int]) -> int:
        ''' 처음 시도 
        max_num = 0
        fill = 0 
        max_index = 0
        for i in range(len(height)):
            if height[i] >= max_num :
                past_max = max_num
                max_num = height[i]
                if i != 0 and i!=1 and max_num >= past_max : 
                    if max_num == past_max : 
                        fill += ((i-max_index-1)*(max_num)-sum(height[max_index+1:i]))
                    else:
                        fill += ((i-max_index-1)*(max_num-1)-sum(height[max_index+1:i]))
                max_index = i 

        if max_index < (len(height)-1) and height[len(height)-1]!=0: 
            if max_index == 0 : 
                fill+= ((len(height))-2-(max_index))*(max_num-1)-sum(height[max_index+1:len(height)-1]) 
            else :
                fill += ((len(height))-2-(max_index)-1)*(max_num-1)-sum(height[max_index+1:len(height)-2]) 
        
        return fill 
        '''
        
        ''' 시간 초과 
        answer = [0]*len(height)
        for i in range(1, len(height)-1):
            h_diff = min(max(height[:i]),max(height[i:]))
            if h_diff-height[i] > 0:
                answer[i]=h_diff-height[i]
        return sum(answer)
        '''
        
        # 투 포인터를 최대로 이동
        if not height:
            return 0

        volume = 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume
        