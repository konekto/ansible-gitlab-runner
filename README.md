Ansible Gitlab Runner
=========

A simple role to install and register a Gitlab runner on a remote server

Requirements
------------

The Docker engine and a user with permission to interact with the Docker api.

Role Variables
--------------

- gitlab_url
- gitlab_runner_token
- gitlab_runner_description
- gitlab_runner_tag
- gitlab_runner_locked

Dependencies
------------

None

Example Playbook
----------------

    - name: Converge
      hosts: all
      tasks:

        - include_role:
            name: ansible-gitlab-runner
          vars:
           # for testing a correct values for gitlab_url and gitlab_runner_token
           gitlab_url: https://gitlab.konek.to
           gitlab_runner_token: s1snr6iNvoxEapC772tU
           gitlab_runner_description: A test runner
           gitlab_runner_tag: test
           gitlab_runner_locked: true

License
-------

MIT

Author Information
------------------

The konek.to Team in 2018
