from collections import Counter
import email
from email import policy
import re
import hashlib

metadata_to_include = ('Subject', 'From', 'Return-Path', 'Received', 'Content-Type', 'To')

def tokenize(path):
    extra = {}
    extra["upper"] = get_upper_percentage(path)
    extra["hash"] = get_hash(path)

    return tokenize_to_counter_without_tags(path), extract_metadata_to_dict(path), extra

def get_list_of_word_in_letter_body(path):
    with open(path, 'rb') as file:
        message = email.message_from_binary_file(file, policy=policy.default)
    
    # Gets body through payloud (.get_contents() would sometimes crash the program)
    part = message.get_body(preferencelist=('plain', 'html'))
    if part:
        payload = part.get_payload(decode=True)
        body = payload.decode('utf-8', errors='replace')
    else:
        body = ""

    if body is None:
        return []
    body = re.sub(r'<.*?>', '', body, flags=re.DOTALL)
    body_list = body.strip().split()
    return body_list

def tokenize_to_counter_without_tags(path):
    words_counter = Counter()
    body_list = get_list_of_word_in_letter_body(path)
    for word in body_list:
        word = word.lower()
        if word == "":
            continue
        words_counter.update({word : 1})
    return words_counter

def extract_metadata_to_dict(path):
    mtdt_dict = {}
    with open(path, 'rt', encoding='utf-8') as file:
        message = email.message_from_file(file)
    for key in metadata_to_include:
        mtdt = message.get_all(key)
        if mtdt:
            if len(mtdt) == 1:
                mtdt_dict[key] = mtdt[0]
            else:
                mtdt_dict[key] = mtdt  # Uložíme jako list

    return mtdt_dict

def get_upper_percentage(path):
    total_letters = 0
    total_upper = 0
    body_list = get_list_of_word_in_letter_body(path)
    for word in body_list:
        for char in word:
            if char.isalpha():
                if char.isupper():
                    total_upper += 1
                total_letters += 1
    if total_letters == 0:
        return 0
    percentage = round(total_upper/total_letters, 2)
    return percentage


def get_hash(path):
    with open(path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


if __name__ == "__main__":
    #print(tokenize_to_counter_without_tags("testing_mail.txt"))
    #print(extract_metadata_to_dict("testing_mail.txt"))
    #print(get_upper_percentage("testing_mail.txt"))

    print(tokenize_to_counter_without_tags("data/1/0001.bfc8d64d12b325ff385cca8d07b84288"))
    print(tokenize_to_counter_without_tags("data/1/00002.9438920e9a55591b18e60d1ed37d992b"))