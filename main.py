import requests


# github_request.py
class JokeApiRequest:
    _base_url = "https://v2.jokeapi.dev"

    @classmethod
    def get_events(cls):
        r = requests.get(cls._base_url + "/joke/Any")
        response = Response(status_code=r.status_code, content=r.json())
        return response


class Response:

    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


# VersioningEvent.py
class VersioningEvent:

    def __init__(self, category, joke, language):
        self.category = category
        self.joke = joke
        self.language = language


class VersioningEventFacade:
    @staticmethod
    def get_versioning_events():
        r = JokeApiRequest.get_events()
        json = r.content
        print(json)
        try:
            versioning_event = VersioningEvent(json['category'], json['joke'], json['lang'])
        except KeyError:
            versioning_event = VersioningEvent(json['category'], json['setup']+" "+json['delivery'], json['lang'])
        return versioning_event


if __name__ == '__main__':
    events = JokeApiRequest.get_events()
    assert isinstance(events, Response)
    assert not isinstance(events, requests.Response)
    print("ok")

    versioning_event = VersioningEventFacade.get_versioning_events()
    assert isinstance(versioning_event, VersioningEvent)
    print(versioning_event.joke)
    print("ok")