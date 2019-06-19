import os
import toml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):

    with host.sudo():

        f = host.file('/srv/gitlab-runner/config/config.toml')

        assert f.exists

        config_file = toml.loads(f.content_string)

        for runner in config_file['runners']:
            assert "/var/run/docker.sock:/var/run/docker.sock" in runner['docker']['volumes']
