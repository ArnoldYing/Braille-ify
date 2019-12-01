import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, MetadataOptions, ConceptsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authentication via IAM
authenticator = IAMAuthenticator('fvqo2-7Ubmnf5rmImg7ycQkj3IW9Op2J3bQtsCmqLqf_')
service = NaturalLanguageUnderstandingV1(
      version='2018-03-16',
      authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

# Authentication via external config like VCAP_SERVICES
# service = NaturalLanguageUnderstandingV1(
#    version='2018-03-16')
# service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

response = service.analyze(
    url='https://en.wikipedia.org/wiki/Overwatch_(video_game)',
    features=Features(concepts=ConceptsOptions(),
                      metadata=MetadataOptions()),
                      return_analyzed_text=True).get_result()

print(json.dumps(response, indent=2))

