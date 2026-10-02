import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "real_chat.settings",
)

import django

django.setup()

import asyncio

from channels.layers import get_channel_layer


async def test():
    channel_layer = get_channel_layer()

    print("CHANNEL LAYER:", channel_layer)

    await channel_layer.group_add(
        "test_group",
        "test_channel",
    )

    print("GROUP ADD: OK")

    await channel_layer.group_send(
        "test_group",
        {
            "type": "test.message",
            "message": "Hello Redis!",
        },
    )

    print("GROUP SEND: OK")

    await channel_layer.group_discard(
        "test_group",
        "test_channel",
    )

    print("GROUP DISCARD: OK")


asyncio.run(test())