import json
from discord_send.discord_send_embed import discord_send_embed


class discord_send_message():
    '''Represents a message to be sent to a discord webhook.'''

    def __init__(self,message:str,username:str="",avatar_url:str="",embed:discord_send_embed=None) -> None:
        self.message = message
        self.username = username
        self.avatar_url = avatar_url
        self.embed = embed

    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "username":self.username,
            "content":self.message,
            "avatar_url":self.avatar_url,
            "embeds":"" if self.embed is None else [self.embed.getMessageObject()]
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()