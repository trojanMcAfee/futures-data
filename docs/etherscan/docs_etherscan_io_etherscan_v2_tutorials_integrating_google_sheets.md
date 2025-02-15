[**Etherscan's APIs**](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts) provides a convenient way to connect and import block explorer information for developers to use in your own apps and services 💻 .

Having technical knowledge is not a requirement for using APIs however, and **non-developers** 🙌 can make use of the available endpoints to build your own dashboards and statistics by importing API data to Google Sheets ![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FBg5llRDAtjdmtf6WK2ip%2Fsheet_logo.png&width=31&dpr=4&quality=100&sign=2c910cdd&sv=2) .

> A valid [**Etherscan API key**](https://docs.etherscan.io/etherscan-v2/getting-started/viewing-api-usage-statistics) and a [**Google Account**](https://www.google.com/account/about/) is required to follow along this tutorial.

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/integrating-google-sheets\#id-1.-integrating-google-apps-script)    1\. Integrating Google Apps Script

In a new Google Sheets document, head over to `Extensions` \> `Apps Script`.

We'll be utilizing an open source script called [**ImportJSON**](https://github.com/bradjasper/ImportJSON/blob/master/ImportJSON.gs) developed by [**@bradjasper**](https://github.com/bradjasper) and [**@tommyvernieri**](https://github.com/tommyvernieri) to help parse JSON responses returned by the API endpoints.

Paste the source code into the script editor, optionally you can rename the file to `ImportJSON.gs`.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FlpuVuDgTfoFkuQQlOaCf%2Fimage.png&width=768&dpr=4&quality=100&sign=21960361&sv=2)

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/integrating-google-sheets\#id-2.-setting-up-auto-refresh)    2\. Setting up auto refresh

Add a new Sheet from the small "+" icon at the bottom left and name it `AutoRefresh`.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FSQBqey7Pz8XP1hJK5DrJ%2F2.png&width=768&dpr=4&quality=100&sign=20ce258a&sv=2)

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

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2Fc2eMbpwW3vFmo195iuBD%2F3.png&width=768&dpr=4&quality=100&sign=9e1c9647&sv=2)

With the script in place, we can run this function every minute by going to ⏰ `Triggers` \> `Add Trigger` at the left panel.

Select the function as `AutoRefresh`, event source as `Time Driven`, time based trigger to `Minutes Timer` and minute interval to `Every Minute`.

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2F4LLy1xNew6mqieNYc4o6%2F4.png&width=768&dpr=4&quality=100&sign=b57b2938&sv=2)

### [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/integrating-google-sheets\#id-3.-making-an-api-request)    3\. Making an API request

Once you have added both scripts, go back to **Sheet1** and start making API endpoint calls with the following syntax in **cell A1**.

Copy

```min-w-full inline-grid grid-cols-[auto_1fr] p-2 [count-reset:line]
=ImportJSON("https://api.etherscan.io/v2/api?chainid=1
   &module=gastracker&action=gasoracle&apikey=YourApiKeyToken", "/result", "allHeaders", AutoRefresh!$A$1)
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

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FC5AbbOduTCOKjpl1LMBE%2F5.png&width=768&dpr=4&quality=100&sign=732fe093&sv=2)

## [Direct link to heading](https://docs.etherscan.io/etherscan-v2/tutorials/integrating-google-sheets\#extending-and-building-a-dashboard)    Extending and Building a Dashboard

While the above was a straightforward method to call an API endpoint and output the response into a Google Sheet, it could use further optimizing and data formatting.

Checkout some [**prepared dashboard examples**](https://docs.google.com/spreadsheets/d/1WK0InGA1LiovGejx0z-82m-HNFt4REWW5EH52dNz6FI/edit#gid=85820572) we have, simply duplicate this by going to `File > Make a copy` 🔗 and go about customizing this to your taste!

![](https://docs.etherscan.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fsg8e76TOnPYfHTGZoQl0%2Fblobs%2FVxlqNbzdHUq6JUPwqB0L%2F6.png&width=768&dpr=4&quality=100&sign=d56d2f4d&sv=2)

Last updated 5 months ago

This site uses cookies to deliver its service and to analyse traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject