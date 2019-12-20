# -*- coding: utf-8 -*-

import os
import copy

class GetDirSturc():
    def __init__(self, root):
        self.root = root    #D:\handbook\GetAllFiles"
        self.rootStruc = []
        self.nodeId = 1
        self.parentNodeId = 0
        self.rootNode = root.split('\\')[-1]   
        self.rootRelativePath = '../' + self.rootNode  #../GetAllFiles" 
        #Tree[0]  = "1|0|Collapsible|D:\handbook\GetAllFiles";
        self.files = list()
        self.idMap = {} # path: parentId
        
            
    def iterLoop(self, rootdir):
        self.appendNode(self.nodeId, self.parentNodeId, self.rootNode, rootdir)
        self.idMap[rootdir] = 1
        for path, subdirs, files in os.walk(rootdir): 
            subdirs.sort()
            for subdir in subdirs:
                self.nodeId += 1
                url = path + os.sep + subdir
                self.idMap[url] = self.nodeId
                parentNodeId = self.idMap[path]
                self.appendNode(self.nodeId, parentNodeId, subdir, url)
            files.sort()
            for f in files:
                #print('file: ', f)
                self.nodeId += 1
                url = path + os.sep + f
                parentNodeId = self.idMap[path]
                self.appendNode(self.nodeId, parentNodeId, f, url)
            
                
    def appendNode(self, nodeId, parentNodeId, nodeName, nodeUrl):
        nodeUrl = nodeUrl.replace(self.root, self.rootRelativePath)
        nodeUrl = nodeUrl.replace('\\', '/')
        Node = [str(nodeId), str(parentNodeId), nodeName, nodeUrl]
        self.rootStruc.append(Node)
           
    def writeParaFile(self):
        num = 0
        newContent = []
        for item in self.rootStruc:
            lineleft = "Tree[{0}]".format(str(num))
            lineright = "\""+ "|".join(item) +"\"" +";"
            newline = "{0} = {1}".format(lineleft, lineright) +'\n'
            num += 1
            newContent.append(newline)
        #delete old values   
        htmlfile = self.root +os.sep + 'MainView.html'
        contents = []
        with open(htmlfile, 'r', encoding="utf-8") as fout:
            for line in fout.readlines():       
                contents.append(line)


        oldContents = copy.copy(contents)
        for line in oldContents:
            if line.strip().startswith('Tree'):
                contents.remove(line)
        #add new tree values
        header =[]
        ender = []
        num = 0
        for line in contents:
            if line.strip().startswith('//'):
                print('line:', line)
                header = contents[0: num+1]
                ender = contents[num+1:]
                print('ender',ender[0])
                break
            else: num += 1
            
        fileContent = header + newContent + ender
        
        outfile = open(htmlfile, 'w', encoding='utf-8')
        for line in fileContent:
            #print('line:', line)
            outfile.writelines(line)
            
def main():
    root = os.getcwd()

    dirSturc = GetDirSturc(root)
    subdirs = dirSturc.iterLoop(root)
    dirSturc.writeParaFile()
    #print(struc)
    
if __name__ == "__main__":
	main()