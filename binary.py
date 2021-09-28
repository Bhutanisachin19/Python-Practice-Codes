#using binary search to return the element

def binary_search(arr,num):
	size = len(arr)
	start = 0
	end = size-1
	
	if(num < arr[0]):
		return 0 #as the index should be 0\
	elif(num > arr[size-1]):
		return size-1
	else:
		#binary search
		while(start < end):
			mid =(start + end)/2
			mid = int(mid)
			if (arr[mid] == num):
				return mid
				
			if (arr[mid] > num):
				end = mid-1
			else:
				start = mid+1
		
		if(num > arr[mid]):
			return mid+1
		else:
			return mid-1
		
		return -1
	
		
		
val = binary_search([1,3,4,9,10,16,19,22,24],23)
print(val)