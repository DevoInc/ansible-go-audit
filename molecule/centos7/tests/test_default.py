import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_goaudit_runningi_and_enable(host):
    goaudit = host.service('go-audit')
    assert goaudit.is_running
    assert goaudit.is_enabled
