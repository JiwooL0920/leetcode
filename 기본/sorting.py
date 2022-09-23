# [selection sort]
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 그다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복
# O(n^2)
def selection_sort(array):
	for i in range (len(array)):
		min_index = i
		for j in range (i+1, len(array)):
			if array[min_index] > array[j]:
				min_index = j;
		array[i], array[min_index] = array[min_index], array[i]

# [Insertion Sort]
# 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입
# 두번째 데이터부터 시작 -- 첫번째 데이터는 그 자체로 정렬되어 있다고 판단
# 현재 리스트의 데이터가 거의 정렬되어 있는 쌍태라면 매우 빠르게 동작함.
# 최선: O(N)
# O(N^2)
def insertion_sort(array):
	for i in range(1, len(array)):
		# start from i, until 0, decrement 1
		for j in range (i, 0, -1): #인덱스 i부터 1까지 감소하며 반복
			if array[j] < array[j-1]:
				array[j], array[j-1] = array[j-1], array[j]
			else: #자기보다 작은 데이터를 만나면 그자리에서 멈춤
				break

# [Quick Sort]
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
# 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나눔
# pivot = 교환하기 위한 기준
# pivot을 성정한 뒤에는 왼쪽에서부터 pivot보다 큰 데이터를 찾고 오른쪽에서부터
# 그것보다 작은 데이터를 찾아서 위치를 서로 교환


# [Merge sort]
def merge_sort(array):
	# if only one element return array
	if len(array) <= 1:
		return array
	# middle of the array
	midpoint = int(len(array) / 2)
	# divide into two equal halves
	left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
	# recursive call on each halves
	return merge(left,right)

def merge(left, right):
	result = []
	l = r = 0
	# while there are elements in both array
	while l < len(left) and r < len(right):
		# check which index in the array is lower
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result.extend(left[l:]) #take everything from left array to the end
	result.extend(right[r:]) #take everything from right array to the end
	return result

# Bubble Sort
def bubble_sort(nums):
	for i in range(len(nums)-1):
		for j in range(len(nums)-1-i):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]


if __name__ == '__main__':
	array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
	# selection_sort(array)
	# insertion_sort(array)
	# result = merge_sort(array)
	# print(result)
	bubble_sort(array)
	print(array)