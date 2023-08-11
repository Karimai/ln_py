def reverse_words_order_and_swap_cases(sentence):
    sentence = sentence.swapcase()
    spl_sent = sentence.split()
    rev_sent = list(reversed(spl_sent))
    return " ".join(rev_sent)



def test_reverse_words_order_and_swap_cases():
    assert reverse_words_order_and_swap_cases("aWESOME is cODING") == "Coding IS Awesome"
