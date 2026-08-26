import os
import subprocess
import hashlib
import pickle

PASSWORD = "supersecret123"


def get_user( name ):
    unused_var = 42
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return query


def run_command(cmd):
    result = subprocess.run(cmd, shell=True)
    return result


def load_data(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data


def weak_hash(value):
    return hashlib.md5(value.encode()).hexdigest()


def eval_input(user_input):
    return eval(user_input)


def bind_all_interfaces():
    return os.popen("ifconfig").read()


class myclass:
    def __init__(self):
        self.x=1
        self.y =2

    def method1(self):
        try:
            pass
        except:
            pass


def unused_import_example():
    import sys
    x = 10
    return 5
