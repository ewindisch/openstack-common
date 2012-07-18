# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright 2011 Cloudscaling Group, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
The MatchMaker classes should except a Topic or Fanout exchange key and
return keys for direct exchanges, per (approximate) AMQP parlance.
"""

import contextlib
import logging

from openstack.common import cfg
from openstack.common.gettextutils import _
from openstack.common.matchmaker import *
from openstack.common.matchmaker import common


CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class StubExchange(Exchange):
    """Exchange that does nothing."""
    def run(self, key):
        return [(key, None)]

class MatchMakerStub(MatchMakerBase):
    """
    Match Maker where topics are untouched.
    Useful for testing, or for AMQP/brokered queues.
    Will not work where knowledge of hosts is known (i.e. zeromq)
    """
    def __init__(self):
        super(MatchMakerBase, self).__init__()

        self.add_binding(FanoutBinding(), StubExchange())
        self.add_binding(DirectBinding(), StubExchange())
        self.add_binding(TopicBinding(), StubExchange())
