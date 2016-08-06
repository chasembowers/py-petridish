class Introspection(object): pass

class Introspector:

    def introspect(self, cell): raise NotImplementedError()

class NullIntrospection(Introspection): pass

class NullIntrospector(Introspector):

    def introspect(self, cell): return NullIntrospection()