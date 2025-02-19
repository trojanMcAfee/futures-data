OrdersCopy Location
All order-related functionality described below assumes the following are available:

Username with relevant relevant trading permissions
Authorized Web API session
Brokerage session (access to IServer endpoints)
Account ID of an account that can receive the order, and for which your username has trading permissions
New Order ExampleCopy Location
The following workflow describes the submission of a new order ticket.

Values needed:Copy Location
Contract ID ("conid") for the desired instrument(s)
Your desired order handling instructions
A POST request to the /iserver/account/{accountId}/orders endpoint is used to submit a new order ticket to the account referenced by {accountId} in the path. This endpoint takes one required path parameter:

accountId: The account ID of the account to which the order will be placed.
This endpoint also requires a JSON body. The specific keys required to successfully submit a given order ticket will vary depending on a variety of factors, including order type. More information on the construction of order tickets can be found on our Order Types page.

However, at a minimum, any new order ticket submitted via the Web API will require in its body:

conid: The instrument's conid
orderType: The Order Type of the new order ticket
side: The side of the order being placed (e.g., "BUY" or "SELL")
tif: Time in force, the duration for which the order will work.
quantity: A number of units of the instrument
Please consult our Reference Material for a list of all JSON keys available when submitting new order tickets.

Suppose we have trading permissions for account DU123456. We'd like submit a new order to this account to buy 100 shares of AAPL, with a limit price of USD 165, to work for the remainder of today's regular trading hours (an unmodified "day" order).

First we must have obtained IB's conid for AAPL stock, trading in the US in USD, which is 265598. We must also know how to represent our desired handling instructions to the Web API:

A buy order is "side":"BUY"
A quantity of 100 shares is "quantity":100
A limit order is "orderType":"LMT"
A limit price of USD 165 is "price":165
A day order is "tif":"DAY"
And finally, AAPL's conid is "conid":265598
Note that both the keys and values above are case-sensitive.

Care must also be taken to ensure the correct JSON data types are used, as detailed in our Reference Material. We may then construct the following request:

POST https://api.ibkr.com/v1/api/iserver/account/DU123456/orders
[
  {
    "conid": 265598,
    "side": "BUY",
    "orderType": "LMT",
    "price": 165,
    "quantity": 100,
    "tif": "DAY"
  }
]
Note also that the body of this POST request requires a JSON array containing the order ticket object. This array is used to submit order brackets, as detailed below. For now, we will submit only a single order ticket by way of a single object element in this array.

If we are successful in submitting our order, we will receive a response that includes an order_id value that can be used to keep track of the status of the order, as well as an indication of its current status at the time of submission:

{
  "order_id": "987654",
  "order_status": "Submitted",
  "encrypt_message": "1"
}
Order Reply MessagesCopy Location
In some cases the response to an order submission request might not deliver an acknowledgment.

Instead, it might contain an "order reply message" -- essentially a notice -- which must be confirmed via a second request before our order ticket can go to work.

The receipt of such an "order reply message" does not indicate that the order is rejected or otherwise encountered a problem. Rather, IB requires explicit confirmation of some element of the order ticket, or some aspect of our subsequent handling, before we can seek the order's execution.

Very often these messages pertain to precautionary settings that are client-configurable for a given username -- effectively "fat finger" protections that you can adjust or remove if desired:

[
  {
    "id": "07a13a5a-4a48-44a5-bb25-5ab37b79186c",
    "message": [
      "The following order \"BUY 100 AAPL NASDAQ.NMS @ 165.0\" price exceeds \nthe Percentage constraint of 3%.\nAre you sure you want to submit this order?"
    ],
    "isSuppressed": false,
    "messageIds": [
      "o163"
    ]
  }
]
Aside from the content of the message, there are two important values delivered in such an "order reply" response.

First, we have an id, which uniquely identifies the emitted message. Via the /iserver/reply/{messageId} endpoint, we can use this id value to dismiss the message and put our order to work:

POST https://api.ibkr.com/v1/api/iserver/reply/a12b34c5-d678-9e012f-3456-7a890b12cd3e
{
  "confirmed":true
}
The above request requires a JSON body containing {"confirmed":true}, which is an instruction to IB that the message has been received, and you would like to continue with your order.

Provided the order can be accepted and put to work, the response to your /iserver/reply/{messageId} request will be an order acknowledgement response as shown above:

{
  "order_id": "1234567890",
  "order_status": "Submitted",
  "encrypt_message": "1"
}
Another important value (or set of values) to capture from order message response is messageIds, as in "messageIds": ["o163"] above.

These messageIds strings categorize varieties of order reply messages. You can use these IDs to suppress certain types of order reply messages for the remainder of your username's current Web API brokerage session.

Please see the Suppressing Order Reply Messages section for more detail.

Order Reply SuppressionCopy Location
The following response to an order ticket submission indicates that we must confirm some aspect of our order ticket before it will be accepted:

[
  {
    "id": "07a13a5a-4a48-44a5-bb25-5ab37b79186c",
    "message": [
      "The following order \"BUY 100 AAPL NASDAQ.NMS @ 165.0\" price exceeds \nthe Percentage constraint of 3%.\nAre you sure you want to submit this order?"
    ],
    "isSuppressed": false,
    "messageIds": [
      "o163"
    ]
  }
]
We call these messages "order reply messages".

The "messageIds" array contains identifiers that categorize the type of order reply message we've received. In this case, we've received "messageIds": ["o163"].

Certain types of order reply messages may be suppressed for the duration of your username's current Web API brokerage session.

When a category of order reply messages is suppressed, you will no longer be sent order reply message responses requiring confirmation. Instead, a valid order ticket will be accepted and acknowledged immediately. Invalid order tickets will be rejected.

The /iserver/questions/suppress endpoint provides this suppression mechanism. You may POST an array of messageIDs to suppress those order message types for the remainder of the Web API brokerage session:

POST https://api.ibkr.com/v1/api/iserver/questions/suppress
{
  "messageIds": [
    "o163"
  ]
}
The response will confirm their suppression:

{
  "status": "submitted"
}
You do not need to have received a given messageID value previously in order to suppress it.

We recommend that you submit this list of messages to be suppressed at the beginning of your brokerage session, prior to conducting any trading.

If you would like to suppress a new type of message while trading, please resend the complete array of messageIds.

You may also undo all suppression of messages within your current brokerage session:

POST https://api.ibkr.com/v1/api/iserver/questions/suppress/reset
And the response will confirm the restoration of delivery of all messages generated during order submission:

{
  "status": "submitted"
}