An API call that encounters an error ⚠️ will return 0 as its `status code` and display the cause of the error under the `result` field.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"0",
   "message":"NOTOK",
   "result":"Max rate limit reached, please use API Key for higher rate limit"
}
```

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/support/common-error-messages\#missing-or-unsupported-chain)    Missing or Unsupported Chain

> "Missing or unsupported chainid parameter (required for v2 api), please see chainlist for the list of supported chainids"

The chain you've specified is not supported by us yet. It could also be that you've sent multiple chains at the same time like `420,10` , you can only send **one** at a time.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/support/common-error-messages\#invalid-api-key)    Invalid API Key

> "Invalid API Key"

This error occurs when you specify an invalid API Key.

Ensure you are using your **Etherscan API Key**, keys from other chains like Polygonscan/Arbiscan are not valid for V2.

Keys do take a few minutes to activate, anything longer than should be alarming.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/support/common-error-messages\#max-rate-limit)    Max rate limit

> "Max rate limit reached, please use API Key for higher rate limit"

This error occurs when you **exceed the rate limit** assigned to your specific API key.

To resolve, adhere to the [**rate limits**](https://docs.etherscan.io/etherscan-v2/support/rate-limits) of your available plan.

If you are using a script or application, **apply throttling** like a token bucket to limit the frequency of calls.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/support/common-error-messages\#missing-or-invalid-action)    Missing or invalid action

> "Error! Missing Or invalid Action name"

This error occurs when you **do not specify**, or specify an **invalid** `module` and `action` name.

To resolve, **double check** your API query to use a valid module and action name.

If you require some help getting started, try copying the sample queries provided in the [**API Endpoints**](https://github.com/BlockSolutions/etherscan-api-docs/blob/master/support/broken-reference/README.md) and pasting them into your browser.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/support/common-error-messages\#endpoint-specific-errors)    Endpoint-specific errors

> "Error! Block number already pass"
>
> "Error! Invalid address format"
>
> "Contract source code not verified"

These error messages returned are specific to certain endpoints and their **related parameters.**

To resolve, kindly refer to the specific endpoint's documentation, and check for the **correct format** or **values** to be specified as **parameters.**

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/support/common-error-messages\#query-timeout)    **Query Timeout**

> "Query Timeout occured. Please select a smaller result dataset"
>
> "Unexpected err, timeout occurred or server too busy. Please try again later"

This error occurs when you have sent a particularly large query that did not manage to be completed in time.

To resolve, consider selecting a smaller date/block range, though you may [**ping us**](https://docs.etherscan.io/etherscan-v2/support/getting-help) if you think the issue may be performance related.

[PreviousRate Limits](https://docs.etherscan.io/etherscan-v2/support/rate-limits) [NextGetting Help](https://docs.etherscan.io/etherscan-v2/support/getting-help)

Last updated 3 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject