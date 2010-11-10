class DataItem:
    def __init__(self, title="", description="", date="", author="", category="", thumb="", thumbBig="", url="", isPlayable=False):
        self._title = title
        self._description = description
        self._date = date
        self._author = author
        self._category = category
        self._thumb = thumb
        self._thumbBig = thumbBig
        self._url = url
        self._isPlayable = isPlayable
    
    @property
    def isPlayable(self):
        return self._isPlayable
    
    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def date(self):
        return self._date
    
    @property
    def author(self):
        return self._author
    
    @property
    def category(self):
        return self._category
    
    @property
    def thumb(self):
        return self._thumb
    
    @property
    def thumbBig(self):
        return self._thumbBig
    
    @property
    def url(self):
        return self._url
