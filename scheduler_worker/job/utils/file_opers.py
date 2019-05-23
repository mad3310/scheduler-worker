import os
import json
import time

class FileOpers(object):

    def getValue(self, fileName, keyList=None):
        resultValue = {}
        f = file(fileName, 'r')

        totalDict = {}

        try:
            while True:
                line = f.readline()

                if not line:
                    break

                pos1 = line.find('=')
                key = line[:pos1]
                value = line[pos1 + 1:len(line)].strip('\n')
                totalDict.setdefault(key, value)
        finally:
            f.close()

        if keyList == None:
            resultValue = totalDict
        else:
            for key in keyList:
                value = totalDict.get(key)
                resultValue.setdefault(key, value)

        return resultValue

    def setValue(self, fileName, keyValueMap):
        inputstream = open(fileName)
        lines = inputstream.readlines()
        inputstream.close()

        outputstream = open(fileName, 'w')

        textContents = []
        for line in lines:
            pos1 = line.find('=')
            targetKey = line[:pos1]
            resultLine = line

            if keyValueMap.has_key(targetKey):
                value = keyValueMap[targetKey]
                resultLine = targetKey + '=' + value + '\n'

            textContents.append(resultLine)

        outputstream.writelines(textContents)

        outputstream.close()
        st = os.stat(fileName)
        os.chmod(fileName, st.st_mode)

    def retrieveFullText(self, fileName):
        inputstream = open(fileName)

        try:
            lines = inputstream.readlines()
        finally:
            inputstream.close()

        resultValue = ''
        for line in lines:
            resultValue += line

        return resultValue

    def writeFullText(self, fileName, fullText):
        if not os.path.exists(fileName):
            raise Exception("%s file not existed!" % (fileName))

        outputstream = open(fileName, 'w')
        outputstream.write('')
        outputstream.write(fullText)
        outputstream.close()

    lockfilepath = '/var/lock/scheduler-worker.lock'
    def appendJsonToFile(self, filename, json_info):
        while os.path.exists(self.lockfilepath):
            time.sleep(2)

        open(self.lockfilepath,"w+")

        try:
            if not os.path.exists(filename):
                open(filename, "w+")

            outputstream = open(filename, 'a')
            outputstream.write(json.dumps(json_info) + '\n')
            outputstream.close()
        finally:
            os.remove(self.lockfilepath)



    def loadFiletoJson(self, filename):
        while os.path.exists(self.lockfilepath):
            time.sleep(5)

        open(self.lockfilepath, "w+")

        if not os.path.exists(filename):
            open(filename, "w+")

        payload = []

        try:
            outputstream = open(filename, 'r')
            contents = outputstream.readlines()
            for line in contents:
                line = line.strip()
                json_data = json.loads(line)
                payload.append(json_data)

            outputstream.close()

            self.__emptyFile(filename)
        finally:
            os.remove(self.lockfilepath)


        return payload


    def __emptyFile(self, filename):
        if not os.path.exists(filename):
            raise Exception("%s file not existed!" % (filename))

        outputstream = open(filename, 'w')
        outputstream.write('')
        outputstream.close()


if __name__ == "__main__":
    s = FileOpers()
    json_data = s.loadFiletoJson('/tmp/scheduler-work-result')
    print json_data
