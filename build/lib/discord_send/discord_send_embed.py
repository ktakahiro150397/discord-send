from datetime import datetime
import logging

from discord_send.discord_send_author import discord_send_author
from discord_send.discord_send_fields import discord_send_fields
from discord_send.discord_send_footer import discord_send_footer
from discord_send.discord_send_image import discord_send_image
from discord_send.discord_send_provider import discord_send_provider

class discord_send_embed():
    '''Represents a embed message to be sent to a discord webhook.'''
    
    def __init__(self,
                 title:str="",
                 description:str="",
                 url:str="",
                 timestamp:datetime=None,
                 sidebarColorCode:str="",
                 footer:discord_send_footer=None,
                 provider:discord_send_provider=None,
                 image:discord_send_image=None,
                 thumbnail:discord_send_image=None,
                 author:discord_send_author=None,
                 fields:discord_send_fields=None,
                 ) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.sidebarColorCode = sidebarColorCode
        self.footer = footer
        self.provider = provider
        self.image = image
        self.thumbnail = thumbnail
        self.author = author
        self.fields = fields

        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(logging.NullHandler())
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = True

    def getMessageObject(self) -> dict:
        '''Returns a dict object representing the message.'''

        obj = {
            "title":self.title,
            "description":self.description,
            "url":self.url,
            "timestamp":("" if self.timestamp == None else self.timestamp.isoformat()),
            "color":self.getColorCode(),
            "footer":("" if self.footer == None else self.footer.getMessageObject()),
            "provider":("" if self.provider == None else self.provider.getMessageObject()),
            "image":("" if self.image == None else self.image.getMessageObject()),
            "thumbnail":("" if self.thumbnail == None else self.thumbnail.getMessageObject()),
            "author":("" if self.author == None else self.author.getMessageObject()),
            "fields":("" if self.fields == None else self.fields.getMessageObject()),
        }

        for key in list(obj.keys()):
            if obj[key] == "":
                del obj[key]

        return obj
    
    def getColorCode(self) -> str:
        if self.sidebarColorCode == "":
            return ""
        else:
            code = self.sidebarColorCode.replace("#","")
            
            try:
                int_code = int(code,base=16)
                return int_code
            except ValueError:
                self._logger.error(f"Invalid color code: {self.sidebarColorCode}")
                return ""
    
    def __str__(self) -> str:
        return self.getMessageObject().__str__()
        
    