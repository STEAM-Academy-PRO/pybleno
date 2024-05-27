from .hci_socket import Emit
from . import UuidUtil


class Characteristic:
    RESULT_SUCCESS = 0x00
    RESULT_INVALID_OFFSET = 0x07
    RESULT_ATTR_NOT_LONG = 0x0b
    RESULT_INVALID_ATTRIBUTE_LENGTH = 0x0d
    RESULT_UNLIKELY_ERROR = 0x0e

    def __init__(self, options=None):
        super(Characteristic, self).__init__()
        self._dict = {}

        if options is None:
            options = {}
        self['uuid'] = UuidUtil.removeDashes(options['uuid'])
        self['properties'] = options['properties'] if 'properties' in options else []
        self['secure'] = options['secure'] if 'secure' in options else []
        self['value'] = options['value'] if 'value' in options else None
        self['descriptors'] = options['descriptors'] if 'descriptors' in options else []

        self.maxValueSize = None
        self.updateValueCallback = None

        if self['value'] and (len(self['properties']) != 1 or self['properties'][0] != 'read'):
            raise Exception('Characteristics with value can be read only!')

        if 'onReadRequest' in options:
            self.onReadRequest = options['onReadRequest']

        if 'onWriteRequest' in options:
            self.onWriteRequest = options['onWriteRequest']

        if 'onSubscribe' in options:
            self.onSubscribe = options['onSubscribe']

        if 'onUnsubscribe' in options:
            self.onUnsubscribe = options['onUnsubscribe']

        if 'onNotify' in options:
            self.onNotify = options['onNotify']

        if 'onIndicate' in options:
            self.onIndicate = options['onIndicate']

        self.on('readRequest', self.onReadRequest)
        self.on('writeRequest', self.onWriteRequest)
        self.on('subscribe', self.onSubscribe)
        self.on('unsubscribe', self.onUnsubscribe)
        self.on('notify', self.onNotify)
        self.on('indicate', self.onIndicate)

    def onReadRequest(self, offset, callback):
        callback(self.RESULT_UNLIKELY_ERROR, None)

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        callback(self.RESULT_UNLIKELY_ERROR)

    def onSubscribe(self, maxValueSize, updateValueCallback):
        self.maxValueSize = maxValueSize
        self.updateValueCallback = updateValueCallback

    def onUnsubscribe(self):
        self.maxValueSize = None
        self.updateValueCallback = None

    def onNotify(self):
        pass

    def onIndicate(self):
        pass

    def __setitem__(self, key, item):
        self._dict[key] = item

    def __getitem__(self, key):
        return self._dict[key]

    def __repr__(self):
        return repr(self._dict)

    def __len__(self):
        return len(self._dict)

    def __delitem__(self, key):
        del self._dict[key]

    def clear(self):
        return self._dict.clear()

    def copy(self):
        return self._dict.copy()

    def has_key(self, k):
        return k in self._dict

    def update(self, *args, **kwargs):
        return self._dict.update(*args, **kwargs)

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()

    def pop(self, *args):
        return self._dict.pop(*args)

    def __cmp__(self, dict_):
        return self._dict.__cmp__(dict_)

    def __contains__(self, item):
        return item in self._dict

    def __iter__(self):
        return iter(self._dict)

    def __unicode__(self):
        return unicode(repr(self._dict))


Emit.Patch(Characteristic)
