import cohere
from utils.CommonUtils import ClsCommonUtils


class ClsApiRun:
    def __init__(self):
        print("Instance for ClsApi Created")

    def callApi(self,text):
        co = cohere.Client(ClsCommonUtils.getApiKey())
        response = co.generate(
            model='xlarge',
            prompt=text,
            max_tokens=50,
            temperature=0.8,
            stop_sequences=['"'],num_generations=5)

        summary = "\n".join([i.text for i in response.generations])
        return summary
