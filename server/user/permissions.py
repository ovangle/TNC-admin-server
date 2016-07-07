from collections import defaultdict


class Permissions(object):
    @classmethod
    def from_json(cls, json_dict):
        return cls({k: set(v) for k,v in json_dict.items()})

    def __init__(self, permissions=None):
        self._dict = defaultdict(set, permissions)

    def check_permission(self, key, action):
        return action in self._dict[key]        

    def add_permission(self, key, action):
        self._dict[k].add(action)

    def remove_permission(self, key, action):
        self._dict[k].discard(action)

    def has_permission(self, key, action):
        return action in self._dict[key]

    def merge(self, permissions):
        copy = defaultdict(set, self._dict)
        for k in permissions:
            copy[k] |= permissions._dict[k]
        return copy

    def to_json(self):
        return {k: list(v) for k,v in self._dict.items() if v}

