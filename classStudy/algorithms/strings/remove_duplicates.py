# 移除重复的单词
def remove_duplicates(words: str) -> str:
    sen_list = words.split(" ")
    check = set()

    for a_word in sen_list:
        check.add(a_word)
    return " ".join(sorted(check))


if __name__ == '__main__':
    result = remove_duplicates("Python is great and Java is also great")
    print(result)
