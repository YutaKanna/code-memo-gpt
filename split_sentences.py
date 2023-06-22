import re

def split_sentences(text):
    sentences = re.split('(?<=[。．！？])', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

# テスト用の文章
text = 'こんにちは。元気ですか？私は元気です！'
sentences = split_sentences(text)

for sentence in sentences:
    print(sentence)
