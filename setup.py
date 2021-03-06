########
# Copyright (c) 2017 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


from setuptools import setup

setup(
    name='cloudify-kubernetes-plugin',
    version='1.2.0',
    author='Krzysztof Bijakowski',
    author_email='krzysztof.bijakowski@gigaspaces.com',
    description='Plugin provides Kubernetes management possibility',

    packages=['cloudify_kubernetes',
              'cloudify_kubernetes.k8s',
              'cloudify_kubernetes.cloudify_agent',
              'cloudify_kubernetes.cloudify_agent.installer'],

    license='LICENSE',
    install_requires=[
        'cloudify-plugins-common>=3.3.1',
        'kubernetes==1.0.2',
        'pyyaml',
        'paramiko'
    ]
)
