from __future__ import annotations

from openai import OpenAI, Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk

client = OpenAI(
    # sk-5206c21a294f4b6c9b1dcc869a6ac56c
    api_key="sk-f91846a6776b4a64baae2366e5ffc52d",
    base_url="https://api.deepseek.com/v1"
)


def get_no_stream() -> ChatCompletion | Stream[ChatCompletionChunk]:
    """

    :rtype: object
    """
    return client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "讲个笑话",
            }
        ],
        stream=True,
        model="deepseek-chat",  # 此处更换其它模型,请参考模型列表 eg: google/gemma-7b-it
    )
def get_chat_completion() -> ChatCompletion | Stream[ChatCompletionChunk]:
    return client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "讲个笑话",
            }
        ],
        stream=True,
        model="deepseek-chat",  # 此处更换其它模型,请参考模型列表 eg: google/gemma-7b-it
    )

# for me in chat:
#     print(me)


# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "讲个笑话",
#         }
#     ],
#     stream=True,
#     model="ERNIE-Tiny-8K", #此处更换其它模型,请参考模型列表 eg: google/gemma-7b-it
# )
#
# chat_completion2 = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "算一下1+1",
#         }
#     ],
#     stream=True,
#     model="ERNIE-Tiny-8K", #此处更换其它模型,请参考模型列表 eg: google/gemma-7b-it
# )


if __name__ == '__main__':
    pass
