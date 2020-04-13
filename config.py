ROBOT_TOKEN = '1208761172:AAFgmf9U6HYuOG0dF-pzsqEzRXWkPnw4OJo'
YOURIP = 'home.khashayarn.ir'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(ROBOT_TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(YOURIP)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'


#bot: https://api.telegram.org/bot<Token>/getme
#webhook: https://api.telegram.org/bot<Token>/getWebhookInfo

