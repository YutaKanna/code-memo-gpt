# 文を単語に分割するプログラムを書いてください
import re

def split_sentence(sentence):
    # 文を単語に分割する正規表現パターン
    pattern = r'\b\w+\b'
    
    # 正規表現パターンに基づいて文を単語に分割
    words = re.findall(pattern, sentence)
    
    return words

# テスト
sentence = "私はPythonを使っています。"
words = split_sentence(sentence)
print(words)