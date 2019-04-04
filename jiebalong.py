# -*- coding: utf-8 -*-
from FileClient import FileClient
import jieba
import jieba.analyse

withWeight = True

def get_path():
    return 'tlong.txt'

def get_save_path():
    return 'jiebalong.txt'

def read_tianlong():
    fileobj = FileClient(get_path())
    return fileobj.read()

def seg_txt(txt):
    jieba.load_userdict("mydict.txt")
    jieba.analyse.set_stop_words("stop_words.txt")
    jieba.analyse.set_idf_path("idf.txt.big")
    return jieba.analyse.extract_tags(txt,topK=2000,withWeight=withWeight)

def txt_filter(txt):
    txt.replace(' ','')
    txt.replace('\n','')
    return txt

def main():
    tianlong = read_tianlong()
    tianlong = txt_filter(tianlong)
    tags = seg_txt(tianlong)
    saveobj = FileClient(get_save_path())
    for tag in tags:
        saveobj.writeLine(str(tag))
    saveobj.close()

if __name__ == "__main__":
    main()
