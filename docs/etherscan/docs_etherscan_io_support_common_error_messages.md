An API call that encounters an error ⚠️ will return 0 as its `status code` and display the cause of the error under the `result` field.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
{
   "status":"0",
   "message":"NOTOK",
   "result":"Max rate limit reached, please use API Key for higher rate limit"
}
```

### [Direct link to heading](https://docs.etherscan.io/support/common-error-messages\#invalid-api-key)    Invalid API Key

> "Invalid API Key"

This error occurs when you specify an invalid API Key, or use a key from an explorer on a [**different chain**](https://docs.etherscan.io/support/faq#can-the-same-api-keys-be-used-across-different-explorers).

To resolve, ensure that you have copy pasted the right key from the right explorer.

New API Keys may also take a moment to be fully activated, so if your fresh key is throwing an error consider waiting for a few minutes.

### [Direct link to heading](https://docs.etherscan.io/support/common-error-messages\#max-rate-limit)    Max rate limit

> "Max rate limit reached, please use API Key for higher rate limit"

This error occurs when you **exceed the rate limit** assigned to your specific API key.

To resolve, adhere to the [**rate limits**](https://docs.etherscan.io/support/rate-limits) of your available plan by waiting for a certain amount of time before each request. If you are using a script or application, **apply throttling** to limit the frequency of calls.

### [Direct link to heading](https://docs.etherscan.io/support/common-error-messages\#missing-or-invalid-action)    Missing or invalid action

> "Error! Missing Or invalid Action name"

This error occurs when you **do not specify**, or specify an **invalid** `module` and `action` name.

To resolve, **double check** your API query to use a valid module and action name.

If you require some help getting started, try copying the sample queries provided in the [**API Endpoints**](https://github.com/BlockSolutions/etherscan-api-docs/blob/master/support/broken-reference/README.md) and pasting them into your browser.

### [Direct link to heading](https://docs.etherscan.io/support/common-error-messages\#endpoint-specific-errors)    Endpoint-specific errors

> "Error! Block number already pass"
>
> "Error! Invalid address format"
>
> "Contract source code not verified"

These error messages returned are specific to certain endpoints and their **related parameters.**

To resolve, kindly refer to the specific endpoint's documentation, and check for the **correct format** or **values** to be specified as **parameters.**

### [Direct link to heading](https://docs.etherscan.io/support/common-error-messages\#query-timeout)    **Query Timeout**

> "Query Timeout occured. Please select a smaller result dataset"
>
> "Unexpected err, timeout occurred or server too busy. Please try again later"

This error occurs when you have sent a particularly large query that did not manage to be completed in time.

To resolve, consider selecting a smaller date/block range, though you may [**ping us**](https://docs.etherscan.io/support/getting-help) if you think the issue may be performance related.

[PreviousRate Limits](https://docs.etherscan.io/support/rate-limits) [NextGetting Help](https://docs.etherscan.io/support/getting-help)

Last updated 6 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject