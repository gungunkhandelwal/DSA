def medianArray(nums1,nums2):
        m = len(nums1)
        n = len(nums2)
        t = m + n
        indx2 = t//2
        indx1 = indx2  - 1
        count = 0
        indx1ele , indxele2 = -1 , -1
        l , r = 0, 0

        while l <m and r <n:
            if nums1[l] < nums2[r]:
                if count == indx1:
                    indx1ele = nums1[l]
                if count == indx2:
                    indxele2 = nums1[l]
                count +=1
                l+=1
            else: 
                if count == indx1:
                    indx1ele = nums2[r]
                if count == indx2:
                     indxele2 = nums2[r]
                count +=1
                r+=1

        while l <m:
            if count == indx1:
                indx1ele = nums1[l]
            if count == indx2:
                indxele2 = nums1[l]
            count +=1
            l+=1
        
        while r < n:
            if count == indx1:
                    indx1ele = nums2[r]
            if count == indx2:
                     indxele2 = nums2[r]
            count +=1
            r+=1

        if t % 2 == 1:
             return float(indxele2)
        
        return float(indx1ele + indxele2) / 2.0
                  
        
        '''
        Brute force Approach
        Time complexity - O(m+n)
        space complexity -O(m+n)
        '''
        # def findMergeSortedArray(nums1,nums2):
        #     merged_arr=[]
        #     m=len(nums1)
        #     n=len(nums2)
        #     l,r = 0,0

        #     while l<m and r<n:
        #         if nums1[l] < nums2[r]:
        #             merged_arr.append(nums1[l])
        #             l+=1
        #         else:
        #             merged_arr.append(nums2[r])
        #             r+=1
            
        #     while l<m:
        #         merged_arr.append(nums1[l])
        #         l+=1
        #     while r<n:
        #         merged_arr.append(nums2[r])
        #         r+=1
        #     return merged_arr
        
        # arr=findMergeSortedArray(nums1,nums2)
        # n=len(arr)
        # median=0


        # if n%2 ==0:
        #         median =(arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2  
        # else:
        #         median = arr[len(arr)//2]
        # return median

nums1=[1,3]
nums2=[2]
print(medianArray(nums1,nums2))