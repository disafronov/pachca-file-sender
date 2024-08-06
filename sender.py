#!/usr/bin/env python3

from pachca_client import get_pachca, File
from os import environ

pachca_access_token = environ.get("PACHCA_ACCESS_TOKEN")
pachca_file_name = environ.get("PACHCA_FILE_NAME")
pachca_chat_id = int(environ.get("PACHCA_CHAT_ID"))
pachca_chat_message = environ.get("PACHCA_CHAT_MESSAGE")

pachca = get_pachca(pachca_access_token)

files = [File(pachca_file_name)]

message = pachca.new_message(
    chat_id=pachca_chat_id, content=pachca_chat_message, files=files
)
