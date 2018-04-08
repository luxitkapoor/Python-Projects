#! /usr/bin/env python3.

# A Very unsecure password vault
import sys
import pyperclip

# Replace the accounts with the actual account name, and password with the respective password

passwords = {
    "Account 1": 'password',
    "Account 2": 'password',
    "Account 3": 'password'
}

if len(sys.argv) < 2:
    print("Need Aditional Argument, Input of the form passwordVault.py accountName")
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard')
    sys.exit()
else:
    print('Account doesn\'t exit')
    sys.exit()
