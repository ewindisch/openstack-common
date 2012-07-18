# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright 2011 Cloudscaling Group, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The matchmaker module for Nova. Different implementations can be plugged
according to the Nova configuration.
"""

import openstack.common.cfg


matchmaker_opts = [
    # Matchmaker ring file
    cfg.StrOpt('matchmaker_driver',
               default='openstack.common.matchmaker.loopback',
               help='Matchmaker driver'),
]

CONF = cfg.CONF
CONF.register_opts(matchmaker_opts)


# rpc_zmq_matchmaker should be set to a 'module.Class'
mm_path = conf.matchmaker_driver.split('.')
mm_module = '.'.join(mm_path[:-1])
mm_class = mm_path[-1]

# Only initialize a class.
if mm_path[-1][0] not in string.ascii_uppercase:
    LOG.error(_("Matchmaker could not be loaded.\n"
              "matchmaker_driver is not a class."))
    raise RPCException(_("Error loading Matchmaker."))

mm_impl = importutils.import_module(mm_module)
mm_constructor = getattr(mm_impl, mm_class)
matchmaker = mm_constructor()
