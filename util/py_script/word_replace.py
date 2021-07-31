# -*- coding:utf-8 -*-

import json
import os


def word_replace(text: str, mapper: dict) -> (bool, str):
    not_safe = False
    safe_text = text
    for k in mapper:
        if safe_text.find(k) >= 0:
            not_safe = True
            safe_text = safe_text.replace(k, mapper[k])
            print("触犯关键字: " + k + " , 已替换为" + mapper[k])
    return not_safe, safe_text


if __name__ == "__main__":
    print("opening dict ... ")
    with open("../sensitive_word_replace_english.json", encoding="utf8") as fp:
        json_data = json.load(fp)
        # print(json_data)
    print("checking markdown notes ... ")
    notes_dir = "../../笔记"
    for root, dirs, files in os.walk(notes_dir):
        for file_name in files:
            if file_name.endswith(".md"):
                print("\t\t\t搜查markdown文件: " + file_name)
                note_path = notes_dir + "/" + file_name
                # 将要被替换为的内容
                data_replace_to = ""
                should_be_replace = False
                with open(note_path, "r") as fp:
                    for line in fp:
                        res = word_replace(line, json_data)
                        if res[0]:
                            should_be_replace = True
                            data_replace_to += res[1]
                        else:
                            data_replace_to += line
                if should_be_replace:
                    with open(note_path, "w") as fp:
                        fp.write(data_replace_to)
                # 再检查文件名是否合规
                res = word_replace(file_name, json_data)
                if res[0]:
                    print("文件名可能违规 : " + res[1])
