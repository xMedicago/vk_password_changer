import random
import string

import aiohttp
from vkbottle import API


class VK:
    def __init__(self):
        self.__url = "https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={0}&password={1}"

    @property
    def password_generator(self):
        return "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))

    async def password_change(self, username, password):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.__url.format(username, password)) as response:
                result = await response.json()
                vk_token = result.get("access_token", 0)
                if vk_token:
                    vk_session = API(token=vk_token)
                    old_password = password
                    new_password = self.password_generator
                    try:
                        await vk_session.account.change_password(old_password=old_password, new_password=new_password)
                        return new_password
                    except Exception as e:
                        print(e)
                        return False
                return False
