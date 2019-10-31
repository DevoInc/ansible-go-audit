# ansible-go-audit
Ansible role to deploy go-audit

To run the role:

ansible-playbook -i ansible/environments/<provider>/<location>/<environment>/hosts ansible/playbooks/go-audit.yml -e "host=<hostname>"

To include new specific rules edit go-audit playbook in automation repo.

This is an example:

    - role: devoinc.go-audit
      goaudit_specific_rules:
        - "-a always,exit -S open -S openat -F exit=-EPERM  -k open_fail"
      goaudit_specific_filters:
        - syscall: 51
          message_type: 1307
          regex: "saddr=(12..|0c..)"
