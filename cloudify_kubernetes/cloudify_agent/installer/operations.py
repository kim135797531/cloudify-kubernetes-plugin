#########
# Copyright (c) 2015 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.

import os
import errno
import yaml

from cloudify import ctx
from cloudify.decorators import operation
from cloudify_agent.installer import operations


def make_conn_cmd():

    # TODO: Should be real pod name, not a tag name
    # name = ctx.node.properties['definition']['metadata']['name']
    name = 'pacman-9w4n7'

    kubeconfig = ctx.node.properties['agent_config']['extra']['kubeconfig']
    filename = os.getcwd() + "/.kube/config-" + name
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, 'w') as f:
        f.write(yaml.safe_dump(kubeconfig, default_flow_style=False))

    # TODO: Make a multiple connections if a pod has more than one container.
    context = kubeconfig['current-context']
    conn_cmd = 'kubectl --kubeconfig="{0}" --context={1} exec {2} -i -- '.format(filename, context, name)
    ctx.node.properties['agent_config']['extra']['conn_cmd'] = conn_cmd


@operation
def create(**_):
    make_conn_cmd()
    return operations.create(**_)


@operation
def configure(**_):
    make_conn_cmd()
    return operations.configure(**_)


@operation
def start( **_):
    make_conn_cmd()
    return operations.start(**_)


@operation
def stop(**_):
    make_conn_cmd()
    return operations.stop(**_)


@operation
def delete(**_):
    make_conn_cmd()
    return operations.delete(**_)


@operation
def restart(**_):
    make_conn_cmd()
    return operations.restart(**_)
