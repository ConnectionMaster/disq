# Copyright 2015 Ryan Brown <sb@ryansb.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pkg_resources

from disq.client import DisqueAlpha

from redis.exceptions import (
    ConnectionError,
    RedisError,
    ResponseError,
    TimeoutError,
)

Disque = DisqueAlpha

__all__ = ['DisqueAlpha',
           'Disque',
           'ConnectionError',
           'RedisError',
           'ResponseError',
           'TimeoutError',
           ]

__version__ = pkg_resources.get_distribution('disq').version
