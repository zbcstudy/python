from collections import defaultdict


# 统计字符串中字符出现的次数
def word_count(sentence: str) -> dict:
    """
    >>> from collections import Counter
    >>> SENTENCE = "a b A b c b d b d e f e g e h e i e j e 0"
    >>> count_dict = word_count(SENTENCE)
    >>> all(count_dict[word] == count for word, count
    ...     in Counter(SENTENCE.split()).items())
    True
    """
    count_number = defaultdict(int)
    for wd in sentence.split(" "):
        count_number[wd] += 1
    return count_number


if __name__ == '__main__':
    for word, count in word_count("input string").items():
        print(f"{word}:{count}")
