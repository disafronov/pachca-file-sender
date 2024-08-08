#!/usr/bin/env python3

import sys
from os import environ
from pachca_client import get_pachca, File


def exit_with_error(variable_name):
    print("The environment variable", variable_name, "is required!", file=sys.stderr)
    sys.exit(1)


def get_env_var(variable_name):
    result = environ.get(variable_name)
    if result is None or result == "":
        exit_with_error(variable_name)
    return result


pachca_access_token = get_env_var("PACHCA_ACCESS_TOKEN")
pachca_file_name = get_env_var("PACHCA_FILE_NAME")
pachca_chat_id = int(get_env_var("PACHCA_CHAT_ID"))
pachca_chat_message = get_env_var("PACHCA_CHAT_MESSAGE")

pachca = get_pachca(pachca_access_token)

files = [File(pachca_file_name)]

message = pachca.new_message(
    chat_id=pachca_chat_id, content=pachca_chat_message, files=files
)
