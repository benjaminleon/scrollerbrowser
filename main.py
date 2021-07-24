""" The chrome extension stopped scrolling after a couple of hours. I could not make the extension click the
chat selectors to the left, but it's possible with pyppeteer. """

import asyncio
import time

from pyppeteer import launch


async def main():
    browser = await launch({'headless': False, 'userDataDir': r'C:\SW\cherry\chromesession'})
    page = await browser.newPage()

    chat_group = "#pane-side > div:nth-child(1) > div > div > div:nth-child(11) > div > div > div._3OvU8"
    chat = "#main > div._1LcQK > div > div"
    seconds_passed = 0
    while True:
        if seconds_passed % (60 * 10) == 0:
            seconds_passed = 0
            await page.goto('https://web.whatsapp.com')
            await page.waitForSelector(chat_group)
            await page.click(chat_group)

        await page.waitForSelector(chat)
        element = await page.querySelector(chat)
        await page.evaluate("(element) => element.scrollTo(0, element.scrollHeight)", element)
        time.sleep(1)
        seconds_passed += 1

asyncio.get_event_loop().run_until_complete(main())
