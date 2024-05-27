class Emit:
    def __init__(self):
        self._events = {}

    def on(self, event, handler):
        if event not in self._events:
            self._events[event] = []

        self._events[event].append(handler)

    def off(self, event, handler):
        if event not in self._events:
            return

        self._events[event].remove(handler)

    def emit(self, event, arguments):
        # print self._events
        # print self._events[event]
        if event not in self._events:
            return

        for handler in self._events[event]:
            handler(*arguments)

    def once(self, event, arguments, handler):
        def temporary_handler(*arguments):
            self.off(event, temporary_handler)
            handler(*arguments)

        self.on(event, temporary_handler)
