"""
class Status:
    def __init__(self,caption):
        self.caption = caption
        print(f" '{self.caption}' is added")

class StatusV1(Status):
    def __init__ (self,url,caption):
        super().__init__(caption)
        self.url = url
        print(f'{self.url} is uploaded')

"""

#Base Class - Instagram Story
class InstragramStory:
    def __init__(self,user):
        self.user = user
        self.story_content = ""
    def post_story(self,content):
        self.story_content = content
        return f"{self.user} posted a story: {content}"













