# This is a sample Python script.
import asyncio
import multiprocessing

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
app主启动类
"""

from sanic import Sanic, text, response
from sanic.response import ResponseStream
from test.test import get_chat_completion, get_no_stream
app = Sanic("StreamingApp")


@app.middleware("response")
async def cors_middleware(request, response):
    # 允许所有源
    response.headers["Access-Control-Allow-Origin"] = "*"

    # 允许的方法
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"

    # 允许的头
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

    # 允许凭证
    response.headers["Access-Control-Allow-Credentials"] = "true"

    # 如果是预检请求（OPTIONS），直接返回200
    if request.method == "OPTIONS":
        return text("OK", status=200)

@app.route("/stream", stream=True)
async def stream_handler(request):

    async def streaming_fn(response):
        for chat in get_chat_completion():
            content = ''
            if len(chat.choices) > 0:
                content = chat.choices[0].delta
            await response.write(f"data: {content}\n\n")
        #     await asyncio.sleep(1)

        # chat = get_no_stream()
        # await response.write(chat.choices[0].message.content)

    return ResponseStream(streaming_fn, content_type='text/event-stream')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, workers=multiprocessing.cpu_count())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
