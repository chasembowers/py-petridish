class Locatable(object):

    def isRightOf(self, xEquals): raise NotImplementedError('Must implement Locatable interface.')

    def isLeftOf(self, xEquals): raise NotImplementedError('Must implement Locatable interface.')

    def isAbove(self, yEquals): raise NotImplementedError('Must implement Locatable interface.')

    def isBelow(self, yEquals): raise NotImplementedError('Must implement Locatable interface.')

    def coordinates(self): raise NotImplementedError('Must implement Locatable interface.')