import websocket
import logging
import json

onMatch = [None]

def on_open(ws):
    ws.send("""
        {
            "type": "subscribe",
            "product_ids": [
                "BTC-USD", "BTC-GBP", "BTC-EUR", "ETH-BTC"
            ],
            "channels": [
                {
                    "name": "matches",
                    "product_ids": [
                        "BTC-USD", "BTC-GBP", "BTC-EUR", "ETH-BTC"
                    ]
                }
            ]
        }
    """)

def on_message(ws, message):
    msg = json.loads(message)

    if msg['type'] == 'error':
        logging.error('Error subscribing to Coinbase. info=', msg.message, msg.reason)
        return

    if msg['type'] == 'subscriptions':
        logging.info('Subscription confirmed. Starting to listen to matches...')
        return

    if msg['type'] == 'match':
        onMatch[0](msg)
        return

    logging.info('Message ignored: ' + str(msg))


def on_error(ws, err):
    logging.warn("Websocket err=" + str(err))

def on_close(ws):
    logging.warn("Websocket closed")

def SubscribeMatchesChannel(websocketURL, onMatch_=None):
    logging.info("Connecting to Coinbase match channel...")

    onMatch[0] = onMatch_

    ws = websocket.WebSocketApp(websocketURL,
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)

    ws.run_forever()

    # async with websockets.connect(websocketURL) as ws:
    #     await ws.send("""
    #         {
    #             "type": "subscribe",
    #             "product_ids": [
    #                 "BTC-USD", "BTC-GBP", "BTC-EUR", "ETH-BTC"
    #             ],
    #             "channels": [
    #                 {
    #                     "name": "matches",
    #                     "product_ids": [
    #                         "BTC-USD", "BTC-GBP", "BTC-EUR", "ETH-BTC"
    #                     ]
    #                 }
    #             ]
    #         }
    #     """)

    #     r = ws.recv()
    #     resp = json.loads(r)
    #     if resp['type'] == 'error':
    #         logging.error('Error subscribing to Coinbase. info=', resp.message, resp.reason)

    #     if resp['type'] == 'subscriptions':
    #         logging.info('Subscription confirmed. Starting to listen to matches...')

    #         while True:
    #             r = await ws.recv()
    #             print('GOT NEW MESSAGE')
    #             # resp = json.loads(r)
    #             # if resp['type'] == 'match':
    #             #     onMatch(resp)

