#!/usr/bin/env python3

import sys
from os import environ
from pachca_client import get_pachca, File


def exit_with_error(variable_name):
    print("The environment variable", variable_name, "is required!", file=sys.stderr)
    sys.exit(1)


pachca_access_token = (
    environ.get("PACHCA_ACCESS_TOKEN")
    if environ.get("PACHCA_ACCESS_TOKEN")
    else exit_with_error("PACHCA_ACCESS_TOKEN")
)

pachca_file_name = (
    environ.get("PACHCA_FILE_NAME")
    if environ.get("PACHCA_FILE_NAME")
    else exit_with_error("PACHCA_FILE_NAME")
)

pachca_chat_id = (
    int(environ.get("PACHCA_CHAT_ID"))
    if environ.get("PACHCA_CHAT_ID")
    else exit_with_error("PACHCA_CHAT_ID")
)

pachca_chat_message = (
    environ.get("PACHCA_CHAT_MESSAGE")
    if environ.get("PACHCA_CHAT_MESSAGE")
    else exit_with_error("PACHCA_CHAT_MESSAGE")
)

pachca = get_pachca(pachca_access_token)

files = [File(pachca_file_name)]

message = pachca.new_message(
    chat_id=pachca_chat_id, content=pachca_chat_message, files=files
)
