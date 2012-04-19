#! /bin/bash
ssh-copy-id spig@10.10.20.220
ssh-copy-id user@10.10.20.221
ssh-copy-id user@10.10.20.223
ssh-copy-id spig@10.10.20.224
# ssh-copy-id spig@haoluobo.com
cp ssh_config ~/.ssh/config
