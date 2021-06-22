"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams

"""

from collections import defaultdict

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global variables
word_dic = {}                 # word_dic could be faster than word_lst
answer_lst = []
count = 0


def main():
    global answer_lst
    global count
    read_dictionary()  # only read once and put info into word_dic

    while True:
        print("welcome to stanCode \"Anagram Generator\" ( or -1 to quit)")
        input_word = input('Find anagrams for: ')
        if input_word == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(input_word)
            print(count, 'anagrams:', answer_lst)

            # clean up the global variables after running through one word
            answer_lst = []
            count = 0


def read_dictionary():
    global word_dic
    with open(FILE, mode='r') as f:
        for line in f:
            # use strip to 去除換行字元
            word_dic[line.strip()] = None


def find_anagrams(s):
    """
    :param s: the word that the user input
    :return: find_anagrams_helper(empty_list, [], len(s), convert_list)
    """
    # create list for s before moving on to the helper function
    input_list = []
    for i in s:
        input_list.append(i)
    # word_to_number_converter ex.( ['a','r','m'] -> ['0','1','2'] )
    # 為了避免重複字母的問題，改用 index 去排列
    convert_list = []
    for i in range(0, len(s)):
        convert_list.append(i)
    find_anagrams_helper(input_list, [], len(s), convert_list, '')


def find_anagrams_helper(lst, current_lst, ans_len, convert_list, answer_string):
    global answer_lst
    global count

    # we use a helper function when the question is too difficult, we add self-defined variables
    if len(current_lst) == ans_len:
        if answer_string not in answer_lst:
            if answer_string not in word_dic:
                pass
            else:
                answer_lst.append(answer_string)
                count += 1
                print('Found: ' + answer_string)
                print('Searching...')
    else:
        # Grow the current_lst
        for num in convert_list:
            if num in current_lst:
                pass
            else:
                current_lst.append(num)
                num_to_lst = []
                answer_string = ''
                # convert number back to word ex.( ['0','1','2'] -> ['a','r','m'] )
                for i in current_lst:
                    num_to_lst.append(lst[i])
                for j in range(0, len(current_lst)):
                    answer_string = answer_string + num_to_lst[j]

                # find_anagrams_helper(lst, current_lst, ans_len, convert_list, answer_string)
                # current_lst.pop()

                # use has_prefix to speed up processing time
                if has_prefix(answer_string):
                    # recursive function
                    find_anagrams_helper(lst, current_lst, ans_len, convert_list, answer_string)
                    current_lst.pop()

                else:
                    current_lst.pop()
"""
    has_prefix(sub_s)之所以在這題不太會加速，是因為我們的data數量太少。當今天data數量太少時，這個has_prefix會拖慢你的程式運行。
    但這邊希望帶給大家一個蓋面，就是early stopping，在實行演算法時，通常你的data可能會有好幾百萬筆，如果你加上了early stopping 的概念後，
    程式計算時間會有顯著的差異。另外，想要加快的話，可以思考如何縮小你的搜尋資料庫，簡單來說可以用 目標單字的長度 或者 答案欄的單字 等方法去加速你的演算法。

"""
def has_prefix(sub_s):
    """
    :param sub_s:
    :return: True or False
    """
    for key, val in word_dic.items():
        if key.startswith(sub_s):
            return True
        else:
            pass
    return False


if __name__ == '__main__':
    main()
