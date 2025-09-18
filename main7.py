def main():

	arr = [1,2,5,8,4,6]
	index = 0
	for i in range(len(arr)):
		if index < arr[i]:
			index = arr[i]

	print(index)



if __name__ == '__main__':
	main()