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

import logging

from openstack.common import cfg
from openstack.common.gettextutils import _
from openstack.common.matchmaker import *
from openstack.common.matchmaker.common import *


CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class LocalhostExchange(Exchange):
    """Exchange where all direct topics are local."""
    def __init__(self):
        super(Exchange, self).__init__()

    def run(self, key):
        return [(key.split('.')[0] + '.localhost', 'localhost')]


class MatchMakerLocalhost(MatchMakerBase):
    """
    Match Maker where all bare topics resolve to localhost.
    Useful for testing.
    """
    def __init__(self):
        super(MatchMakerLocalhost, self).__init__()
        self.add_binding(FanoutBinding(), LocalhostExchange())
        self.add_binding(DirectBinding(), DirectExchange())
        self.add_binding(TopicBinding(), LocalhostExchange())
