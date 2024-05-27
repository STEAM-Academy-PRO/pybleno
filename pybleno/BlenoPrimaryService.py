from . import UuidUtil
import json
from .hci_socket import Emit


class BlenoPrimaryService:
    def __init__(self, options):
        super(BlenoPrimaryService, self).__init__()
        self._dict = {}

        self['uuid'] = UuidUtil.removeDashes(options['uuid'])
        self['characteristics'] = options['characteristics'] if 'characteristics' in options else []

    def __str__(self):
        return json.dumps({
            'uuid':            self['uuid'],
            'characteristics': self['characteristics']
        })

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
        return self.__cmp__(self._dict, dict_)

    def __contains__(self, item):
        return item in self._dict

    def __iter__(self):
        return iter(self._dict)

    def __unicode__(self):
        return unicode(repr(self._dict))


Emit.Patch(BlenoPrimaryService)
