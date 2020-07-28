from python_study.tasks import t1, t2, t3, t4, t5, t6, t7, t8, t9

def test_t1():
    assert t1.reverse_str('Hello World!') == '!dlroW olleH'
    assert t1.reverse_str('1234567890') == '0987654321'

def test_t2():
    assert t2.palindrome('Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I Diet On Cod')
    assert t2.palindrome('Never Odd Or Even')

def test_t3():
    assert t3.remove_special_char('He*llo, Wo$rld!') == 'Hello World'
    assert t3.remove_special_char('!@#$%Message!@#$%') == 'Message'

def test_t4():
    assert t4.common_elements([3,2,4], [3,4,5,6]) == [3,4] or [4,3]
    assert t4.common_elements([], [1,2,3]) == []