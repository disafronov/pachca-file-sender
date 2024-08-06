# pachca-file-sender

Simple file sender for [Pachca](https://pachca.com) based on [k1nky/pachca-client](https://github.com/k1nky/pachca-client).

## Example usage

```shell
docker run --rm \
  -w [path_to_dir_with_your_file] \
  -v [path_to_dir_with_your_file]:[path_to_dir_with_your_file]:ro \
  -e PACHCA_ACCESS_TOKEN="BotAccessToken" \
  -e PACHCA_CHAT_ID="ChatIdFromShareChatLink" \
  -e PACHCA_CHAT_MESSAGE="VerboseFileDescription" \
  -e PACHCA_FILE_NAME="FullPathToYourFile" \
  ghcr.io/dmitriysafronov/pachca-file-sender:latest
```
