class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]: #create fuction
        Hashtable = {}  #create a hashtable to store and fastly find the phan con lai
        for index, num in enumerate(nums):  # loop từng số trong list để tìm phần còn lại của số đó rồi xem có trong hash table chưa/
                                            # có rồi thì return 
            phan_con_lai = target - num  #tinh phan con lai
            if phan_con_lai in Hashtable: #xem có trong hashtable chx? condition này là O(1) vì nó tình key để ra index lưu trữ trong hashtable
                return [Hashtable[phan_con_lai], index]
            
            Hashtable[num]= index  # key của hashtable là num và lữu trữ inde. Nếu có 2 số giống nhau thì sẽ lưu trữ index của số mới
        return []


'''
trong hashtable/dictionary các data sẽ được lưu trữ dưới dạng key:value vả mỗi cặp này sẽ có index trong dic riêng
nhưng index sẽ không được tạo theo thứ tự mà bán ngẫu nhiên dựa trên một các tính toán sao cho từ 1 key ra được 1 index rồi lưu trữ thẳng vào
index đó. Vì mỗi khi tìm chỉ (line4) cần tính toán ra cái index đó dựa trên key đã cho, nên nó luôn là O(1)

        
