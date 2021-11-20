from dataclasses import dataclass


@dataclass
class WordCloudRequest(object):
    model_uuid: str

@dataclass
class WordCloudResponse(object):
    model_uuid: str

    