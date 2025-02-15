[**Etherscan's APIs**](https://docs.etherscan.io/api-endpoints/accounts) provides a convenient way to connect and import block explorer information for developers to use in your own apps and services 💻 .

Having technical knowledge is not a requirement for using APIs however, and **non-developers** 🙌 can make use of the available endpoints to build your own dashboards and statistics by importing API data to Google Sheets ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-e7acad5d0b75f0526eae5a06b6517d8676096661%252Fsheet_logo.png%3Falt%3Dmedia&width=31&dpr=4&quality=100&sign=a1edab36&sv=2) .

> A valid [**Etherscan API key**](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics) and a [**Google Account**](https://www.google.com/account/about/) is required to follow along this tutorial.

### [Direct link to heading](https://docs.etherscan.io/tutorials/integrating-google-sheets\#id-1.-integrating-google-apps-script)    1\. Integrating Google Apps Script

In a new Google Sheets document, head over to `Extensions` \> `Apps Script`.

We'll be utilizing an open source script called [**ImportJSON**](https://github.com/bradjasper/ImportJSON/blob/master/ImportJSON.gs) developed by [**@bradjasper**](https://github.com/bradjasper) and [**@tommyvernieri**](https://github.com/tommyvernieri) to help parse JSON responses returned by the API endpoints.

Paste the source code into the script editor, optionally you can rename the file to `ImportJSON.gs`.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-6ae906f02a60275b294f5236eb8203b3cfea3bd5%252Fimage.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=d1947757&sv=2)

### [Direct link to heading](https://docs.etherscan.io/tutorials/integrating-google-sheets\#id-2.-setting-up-auto-refresh)    2\. Setting up auto refresh

Add a new Sheet from the small "+" icon at the bottom left and name it `AutoRefresh`.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-c1b5a9fcfb516dc577ef139e8f0ed03d6a85fbb9%252F2.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=a57e1801&sv=2)

Back to Google Apps Script, create a new file and name it `AutoRefresh.gs`. Paste in this following code.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
function AutoRefresh() {
    SpreadsheetApp.getActive().getSheetByName('AutoRefresh').getRange(1, 1).setValue(Math.random());
}
```

> The idea of this script is to generate a random number to the AutoRefresh sheet, which is then appended to the end of the ImportJSON request.
>
> Google Sheets only performs a new request if it detects that a formula has changed.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-cc8f949655cff651bc32055cfb7b59788fe8cd60%252F3.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=c6d1b9a2&sv=2)

With the script in place, we can run this function every minute by going to ⏰ `Triggers` \> `Add Trigger` at the left panel.

Select the function as `AutoRefresh`, event source as `Time Driven`, time based trigger to `Minutes Timer` and minute interval to `Every Minute`.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-db24afaccb9f2d6f168ad2b7c5e242fdebc4a6d8%252F4.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=77317367&sv=2)

### [Direct link to heading](https://docs.etherscan.io/tutorials/integrating-google-sheets\#id-3.-making-an-api-request)    3\. Making an API request

Once you have added both scripts, go back to **Sheet1** and start making API endpoint calls with the following syntax in **cell A1**.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
=ImportJSON("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken", "/result", "allHeaders", AutoRefresh!$A$1)
```

Parameter

Description

url

the endpoint url to make requests from, with your API Key

query

comma separated paths to import, such as `/result` or `/result/SafeGasPrice`

parseOptions

list of options to process the returned data, either `noInherit`, `noTruncate`, `rawHeaders`, `noHeaders` or `allHeaders`

The query above will return the following response, and refreshes auto-magically ✨ every minute!

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-82b6c01cc0ebfb411f69d97310bffd59c69bf275%252F5.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=e29cdb7e&sv=2)

## [Direct link to heading](https://docs.etherscan.io/tutorials/integrating-google-sheets\#extending-and-building-a-dashboard)    Extending and Building a Dashboard

While the above was a straightforward method to call an API endpoint and output the response into a Google Sheet, it could use further optimizing and data formatting.

Checkout some [**prepared dashboard examples**](https://docs.google.com/spreadsheets/d/1WK0InGA1LiovGejx0z-82m-HNFt4REWW5EH52dNz6FI/edit#gid=85820572) we have, simply duplicate this by going to `File > Make a copy` 🔗 and go about customizing this to your taste!

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2F1052732906-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-McrExXKKJBLJqymbFhO%252Fuploads%252Fgit-blob-767e6479cd1e1908697c47d87b33b3558903e4ca%252F6.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=fe0c9562&sv=2)

[PreviousRead/Write Smart Contracts](https://docs.etherscan.io/tutorials/read-write-smart-contracts) [NextWhat's Contract Verification](https://docs.etherscan.io/contract-verification/whats-contract-verification)

Last updated 3 years ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject