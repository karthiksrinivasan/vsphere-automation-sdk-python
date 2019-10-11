#!/usr/bin/env python

import os

from setuptools import setup

setup(name='vSphere_Automation_SDK',
      version='1.8.0',
      description='VMware vSphere Automation SDK for Python',
      url='https://github.com/vmware/vsphere-automation-sdk-python',
      author='VMware, Inc.',
      license='MIT',
      install_requires=[
        'lxml >= 4.3.0',
        'suds ; python_version < "3"',
        'suds-jurko ; python_version >= "3.0"',
        'pyVmomi >= 6.7',
	'vapi-runtime==2.12.0',
	'vapi-client-bindings==3.1.0',
	'vapi-common-client==2.12.0',
        'vmc-client-bindings==1.14.0',
        'nsx-python-sdk==2.3.0.0.3.13851140',
        'nsx-policy-python-sdk==2.3.0.0.3.13851140',
        'nsx-vmc-policy-python-sdk==2.3.0.0.3.13851140',
        'nsx-vmc-aws-integration-python-sdk==2.3.0.0.3.13851140',
        'vmc-draas-client-bindings==1.0.0',
      ]
      )
