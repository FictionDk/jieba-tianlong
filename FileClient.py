# -*- coding: utf-8 -*-

class FileClient(object):
    def __init__(self,path):
        self.path = path
        self.writer = open(path,'a+',encoding="utf-8")
        self.reader = open(path,'r',encoding="utf-8")

    def writeLine(self,strline):
        try:
            self.writer.write(strline + '\n')
            self.writer.flush()
        except UnicodeEncodeError:
            print("ERROR: ", strline, ", UnicodeEncodeError")
            self.writer.write("UnicodeEncodeError" + '\n')
            self.writer.flush()

    def readLine(self):
        return self.reader.readline()

    def read(self):
        return self.reader.read()

    def close(self):
        self.writer.close()
        self.reader.close()

def test():
    path = 'E:\\home\\filetest\\a.log'
    fileObj = FileClient(path)
    fileObj.writeLine("test")
    fileObj.close()

test()
