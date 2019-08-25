# -*- coding: utf-8 -*-
from FileClient import FileClient
import os
import jieba
import jieba.analyse
import json

withWeight = True

def get_inputfile():
    return os.path.join(os.getcwd(),'inputfile','tlong.txt')

def get_outputfile(filename="jiebalong.txt"):
    return os.path.join(os.getcwd(),'outputfile',filename)

def read_tianlong():
    fileobj = FileClient(get_inputfile())
    return fileobj.read()

def seg_txt(txt):
    jieba.load_userdict(os.path.join(os.getcwd(),'customdict',"mydict.txt"))
    jieba.analyse.set_stop_words(os.path.join(os.getcwd(),'customdict',"stop_words.txt"))
    jieba.analyse.set_idf_path(os.path.join(os.getcwd(),'customdict',"idf.txt.big"))
    return jieba.analyse.extract_tags(txt,topK=45,withWeight=withWeight,allowPOS=(),withFlag=True)

def txt_filter(txt):
    txt.replace(' ','')
    txt.replace('\n','')
    return txt

def read_result():
    json_obj = FileClient(get_outputfile('words.json'))
    tag_lists = []
    result = json_obj.readLine()
    while result != "":
        tag_lists.append(json.loads(result))
        result = json_obj.readLine()
    return tag_lists

def main():
    tianlong = read_tianlong()
    # tianlong = txt_filter(tianlong)
    tags = seg_txt(tianlong)
    saveobj = FileClient(get_outputfile())
    singal_words = FileClient(get_outputfile('singal_words.txt'))
    json_obj = FileClient(get_outputfile('words.json'))
    totle_w = 0.0
    for tag in tags:
        saveobj.writeLine(str(tag))
        singal_words.writeLine(str(tag[0]))
        tag_dict = {}
        tag_dict["name"] = tag[0]
        tag_dict["value"] = tag[1]
        # ensure_ascii默认为True,会造成unicode编码错误
        json_obj.writeLine(json.dumps(tag_dict,ensure_ascii=False))
        totle_w += tag[1]
    print("Totle W: %f ." % totle_w)
    saveobj.close()
    json_obj.close()
    singal_words.close()

if __name__ == "__main__":
    # main()
    read_result()
