import json

import copy

class ClsCommonUtils:
    __config = None

    @staticmethod
    def getDictvalue(dictobj, key, default=None):
        return dictobj.get(key, default)

    @staticmethod
    def getConfig(configFileName="config.json"):
        if ClsCommonUtils.__config == None:
            ClsCommonUtils.__config = json.load(open(configFileName, 'r'))
        return copy.deepcopy(ClsCommonUtils.__config)

    @staticmethod
    def getApiKey():
        return ClsCommonUtils.getDictvalue(ClsCommonUtils.getConfig(), 'ApiKey')
