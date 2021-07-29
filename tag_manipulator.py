import re


class TagManipulator():
    def parse_string(self, tags, regex=""):
        result = []

        tags = tags.lstrip(",").rstrip(",").strip()

        tempResult = re.split(regex, tags)
        if(len(tempResult[0]) > 0):
            result = tempResult
            result = [s.strip() for s in result]

        return result
