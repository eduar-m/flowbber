# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 KuraLabs S.R.L
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Module implementating Source base class.

All custom Flowbber sources must extend from the Source class.
"""

from time import time
from abc import abstractmethod
from multiprocessing import Queue

from setproctitle import setproctitle

from .base import BaseEntity


class Source(BaseEntity):
    def __init__(self, index, type_, key, config):
        super().__init__(index, type_, config)
        self._key = key

        self.result = Queue(maxsize=1)
        self.duration = Queue(maxsize=1)

    @property
    def key(self):
        return self._key

    def execute(self):
        setproctitle(str(self))

        start = time()
        entry = {}

        try:
            entry[self._key] = self.collect()
        finally:
            self.result.put(entry)
            self.duration.put(time() - start)

    @abstractmethod
    def collect(self):
        pass

    def __str__(self):
        return '#{} {}.{}.{}'.format(
            self._index,
            self.__class__.__name__,
            self._type_,
            self._key
        )


__all__ = ['Source']
