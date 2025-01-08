import asyncio
import logging
from lib.Autolane import Autolane, AutolaneError
from lib.settings import email_user, password_user



async def main():
    autolane = Autolane()
    request_login = await autolane.login(email=email_user, password=password_user)
    logging.info(request_login)
    await asyncio.sleep(2)
  
try:
    asyncio.run(main())
except AutolaneError:
  print('Não foi possível realizar a automação, Contate o Lucas')
