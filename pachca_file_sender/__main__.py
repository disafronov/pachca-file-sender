#!/usr/bin/env python3

import sys
from os import environ
from pachca_client import get_pachca, File


def exit_with_error(message):
    print(message, file=sys.stderr)
    sys.exit(1)


def get_env_var(variable_name):
    result = environ.get(variable_name)
    if result is None or result == "":
        exit_with_error("The environment variable " + variable_name + " is required!")
    return result


def main():
    PACHCA_ACCESS_TOKEN = get_env_var("PACHCA_ACCESS_TOKEN")
    PACHCA_FILE_NAME = get_env_var("PACHCA_FILE_NAME")
    PACHCA_CHAT_ID = int(get_env_var("PACHCA_CHAT_ID"))
    PACHCA_CHAT_MESSAGE = get_env_var("PACHCA_CHAT_MESSAGE")

    pachca = get_pachca(PACHCA_ACCESS_TOKEN)

    files = [File(PACHCA_FILE_NAME)]

    pachca.new_message(chat_id=PACHCA_CHAT_ID, content=PACHCA_CHAT_MESSAGE, files=files)


if __name__ == "__main__":
    main()
