from discord_webhook import DiscordWebhook


def send_msg(uname,msg,webhook_url):
    webhook = DiscordWebhook(username=uname, url=webhook_url, content=msg)
    response = webhook.execute()
