"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""
from itertools import permutations

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variables
count = 0
boggle_lst = [[], [], [], []]
dic_lst = []
word_dic = {}


def main():
	"""
	TODO:
	"""
	read_dictionary()
	user_input()
	play_boggle()
	print(f"There are {count} words in total.")


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dic_lst
	global word_dic
	with open(FILE, 'r') as f:
		for line in f:
			# dic_lst.append(line.strip())
			word_dic[line.strip()] = None


def user_input():
	"""
	This function ask the user to input 4 rows of letters
	and appends words in each line into a Python list

	# input_user = [['e','e','r','t'],
					['t','h','j','k'],
					['u','s','d','g'],
					['g','k','l','o']]
	"""
	global boggle_lst

	for i in range(4):
		row = input(str(i+1) + ' row of letters: ')
		row = row.lower()  # case insensitive
		if len(row) != 7:
			print('Illegal input')
			break
		else:
			row = row.split()  # ['a', 'b', 'c', 'd']
			blank_s = ''
			for word in row:
				blank_s += word
			if len(blank_s) != 4:
				print('Illegal input')
				break
			else:
				boggle_lst[i] = row


def play_boggle():
	# play_boggle loops through all the 16 input vocab
	for row in range(4):
		for col in range(4):
			# whenever starting and looping through a new vocab in boggle_lst, clear the used position lst
			used_position = []
			used_position.append((row, col))
			# create word(lst) to check if it exist in the dic_lst
			word = ''
			word += boggle_lst[row][col]
			# only one vocab will go through the next helper function
			helper(word, row, col, used_position)  # example: helper(['e'], 0, 0, [(0,0)])


def helper(word, row, col, used_position):
	global count

	# early stopping
	if has_prefix(word) is False:
		used_position.pop()
		word = word[:-1]
		helper(word, row, col, used_position)

	else:
		# base case: check if word is in word_dic
		if len(word) >= 4 and word in word_dic:
			print(f'Found \"{word}\"')
			count += 1
			# after finding the word from word_dic, delete the word from the dic in order to find roomy after room
			del word_dic[word]
			# 檢查完後，要再把 word 丟回helper繼續尋找有沒有相關的字
			helper(word, row, col, used_position)
		else:
			# 選位置，跟 (row,col) 座標，對其四周進行 loop
			for i in range(-1, 2, 1):  # loop -1 to 1
				for j in range(-1, 2, 1):
					new_r = i + row
					new_c = j + col

					# 避免超出邊界，且避免走重複的位置
					if (new_r, new_c) not in used_position:
						if 0 <= new_r < 4 and 0 <= new_c < 4:
							used_position.append((new_r, new_c))  # 用過的位置記錄起來，可以加速進行
							# choose
							word += boggle_lst[new_r][new_c]

							if has_prefix(word):
								# explore
								helper(word, new_r, new_c, used_position)
								# un-choose: update used position and word_str
								# 1. 這邊要把 used_position pop掉最後一格
								used_position.pop()
								# 2. 更新字串
								word = word[:-1]
								#
							else:
								used_position.pop()
								word = word[:-1]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for key, val in word_dic.items():
		if key.startswith(sub_s):
			return True
		else:
			pass
	return False


if __name__ == '__main__':
	main()
