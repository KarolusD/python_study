'''
Write a function that will except
2 lists and return common elements list.

Example:
[2,3,4] and [4,3,5,9] => [3,4]
'''


def common_elements(list_one, list_two):
    score=[]
    for i in list_one :
        if i in list_two:
            score.append(i)
    return score

print(common_elements([2,3,4],[4,3,5,9]))
