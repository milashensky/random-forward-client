import re
import logging
import random
from telethon import TelegramClient

import settings

logger = logging.getLogger()


class RandomMessageClient:
    async def __aenter__(self):
        if not settings.SESSION_PATH:
            logging.info('connecting without session path')
        self.client = TelegramClient(
            settings.SESSION_PATH,
            settings.API_ID,
            settings.API_HASH,
        )
        await self.client.start()
        logging.info('connected')
        return self

    async def __aexit__(self, *args, **kwargs):
        if not settings.SESSION_PATH:
            logging.info('connected without session path, logging out')
            await self.client.log_out()

    async def make_entity(self, link_or_id):
        # telethon doesn't parses id on their own
        if re.match(r'^-?\d+$', link_or_id):
            link_or_id = int(link_or_id)
        entity = await self.client.get_entity(link_or_id)
        return entity

    async def get_random_message(self, chat):
        # we first get total length of messages in the chat, and then select random value as offset
        chat_entity = await self.make_entity(chat)
        total_list = await self.client.get_messages(chat_entity, limit=0)
        offset = random.randint(0, total_list.total - 1)
        messages = await self.client.get_messages(
            chat_entity,
            limit=1,
            add_offset=offset,
        )
        return messages[0]

    async def forward_message(self, message, to_chat):
        chat_entity = await self.make_entity(to_chat)
        message = await self.client.forward_messages(
            chat_entity,
            message.id,
            message.chat.id,
        )
        return message
