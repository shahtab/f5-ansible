# -*- coding: utf-8 -*-
#
# Copyright 2017 F5 Networks Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import sys

if sys.version_info < (2, 7):
    from nose.plugins.skip import SkipTest
    raise SkipTest("F5 Ansible modules require Python >= 2.7")

import os
import json
import pytest

from ansible.compat.tests import unittest
from ansible.compat.tests.mock import patch, Mock
from ansible.module_utils import basic
from ansible.module_utils._text import to_bytes
from ansible.module_utils.f5_utils import AnsibleF5Client
from ansible.module_utils.f5_utils import F5ModuleError

try:
    from library.bigip_gtm_wide_ip import Parameters
    from library.bigip_gtm_wide_ip import ModuleManager
    from library.bigip_gtm_wide_ip import ArgumentSpec
    from library.bigip_gtm_wide_ip import UntypedManager
except ImportError:
    from ansible.modules.network.f5.bigip_gtm_wide_ip import Parameters
    from ansible.modules.network.f5.bigip_gtm_wide_ip import ModuleManager
    from ansible.modules.network.f5.bigip_gtm_wide_ip import ArgumentSpec
    from ansible.modules.network.f5.bigip_gtm_wide_ip import UntypedManager

fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
fixture_data = {}


def set_module_args(args):
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)


def load_fixture(name):
    path = os.path.join(fixture_path, name)

    if path in fixture_data:
        return fixture_data[path]

    with open(path) as f:
        data = f.read()

    try:
        data = json.loads(data)
    except Exception:
        pass

    fixture_data[path] = data
    return data


class TestParameters(unittest.TestCase):
    def test_module_parameters(self):
        args = dict(
            name='foo.baz.bar',
            lb_method='round-robin'
        )
        p = Parameters(args)
        assert p.name == 'foo.baz.bar'
        assert p.lb_method == 'round-robin'

    def test_api_parameters(self):
        args = dict(
            name='foo.baz.bar',
            poolLbMode='round-robin'
        )
        p = Parameters(args)
        assert p.name == 'foo.baz.bar'
        assert p.lb_method == 'round-robin'

    def test_api_not_fqdn_name(self):
        args = dict(
            name='foo.baz',
            poolLbMode='round-robin'
        )
        with pytest.raises(F5ModuleError) as excinfo:
            p = Parameters(args)
            assert p.name == 'foo.baz'
        assert 'The provided name must be a valid FQDN' in str(excinfo)


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()

    @patch('ansible.module_utils.f5_utils.AnsibleF5Client._get_mgmt_root',
           return_value=True)
    def test_create_wideip_pre_v12(self, *args):
        set_module_args(dict(
            name='foo.baz.bar',
            lb_method='round-robin',
            password='passsword',
            server='localhost',
            user='admin'
        ))

        client = AnsibleF5Client(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            f5_product_name=self.spec.f5_product_name
        )

        # Override methods in the specific type of manager
        tm = UntypedManager(client)
        tm.exists = Mock(return_value=False)
        tm.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(client)
        mm.version_is_less_than_12 = Mock(return_value=True)
        mm.get_manager = Mock(return_value=tm)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'foo.baz.bar'
        assert results['state'] == 'present'
        assert results['lb_method'] == 'round-robin'

    @patch('ansible.module_utils.f5_utils.AnsibleF5Client._get_mgmt_root',
           return_value=True)
    def test_create_wideip_post_v12(self, *args):
        set_module_args(dict(
            name='foo.baz.bar',
            lb_method='round-robin',
            password='passsword',
            server='localhost',
            user='admin'
        ))

        client = AnsibleF5Client(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            f5_product_name=self.spec.f5_product_name
        )

        # Override methods in the specific type of manager
        tm = UntypedManager(client)
        tm.exists = Mock(return_value=False)
        tm.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(client)
        mm.version_is_less_than_12 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=tm)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'foo.baz.bar'
        assert results['state'] == 'present'
        assert results['lb_method'] == 'round-robin'

    @patch('ansible.module_utils.f5_utils.AnsibleF5Client._get_mgmt_root',
           return_value=True)
    def test_create_wideip_deprecated_lb_method1(self, *args):
        set_module_args(dict(
            name='foo.baz.bar',
            lb_method='round_robin',
            password='passsword',
            server='localhost',
            user='admin'
        ))

        client = AnsibleF5Client(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            f5_product_name=self.spec.f5_product_name
        )

        # Override methods in the specific type of manager
        tm = UntypedManager(client)
        tm.exists = Mock(return_value=False)
        tm.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(client)
        mm.version_is_less_than_12 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=tm)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'foo.baz.bar'
        assert results['state'] == 'present'
        assert results['lb_method'] == 'round-robin'

    @patch('ansible.module_utils.f5_utils.AnsibleF5Client._get_mgmt_root',
           return_value=True)
    def test_create_wideip_deprecated_lb_method2(self, *args):
        set_module_args(dict(
            name='foo.baz.bar',
            lb_method='global_availability',
            password='passsword',
            server='localhost',
            user='admin'
        ))

        client = AnsibleF5Client(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            f5_product_name=self.spec.f5_product_name
        )

        # Override methods in the specific type of manager
        tm = UntypedManager(client)
        tm.exists = Mock(return_value=False)
        tm.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(client)
        mm.version_is_less_than_12 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=tm)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'foo.baz.bar'
        assert results['state'] == 'present'
        assert results['lb_method'] == 'global-availability'
