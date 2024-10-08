// const fs = require('fs');

// const baseCurrency = ["AUD", "CNY", "EUR", "HKD", "IDR", "JPY", "KRW", "MYR", "PHP", "SAR", "SGD", "THB", "TWD", "USD", "VND", "INR"];
// const supportedCurrency = ["SGD", "AUD", "USD", "MYR", "EUR", "TWD", "JPY", "GBP", "INR", "PHP", "AED", "CAD", "CHF", "CNY", "CZK", "DKK", "HKD", "IDR", "KRW", "LKR", "MOP", "MXN", "NOK", "NZD", "PLN", "SAR", "SEK", "THB", "VND", "ZAR", "RUB"];
// const ws = fs.createWriteStream('filename.txt');

// for (let index = 0; index < baseCurrency.length; index++) {
//   const baseCurrencyItem = baseCurrency[index];

//   for (let index = 0; index < supportedCurrency.length; index++) {
//     const supportedCurrencyItem = supportedCurrency[index];
//     if (baseCurrencyItem !== supportedCurrencyItem) {
//       const contentFile = `('${baseCurrencyItem}${supportedCurrencyItem}','${baseCurrencyItem}','${supportedCurrencyItem}','2024-01-01 00:00:00', 'system'),\n`;
//       console.log(contentFile);
//       ws.write(contentFile)
//     }
//   }
// }

// ws.end((err) => {
//   if (err) throw err;
//   console.log('Data written to file');
// });

const message = "hahahaa \&quot";

if (message.indexOf('&quot') > -1) {
  tempDat = message.replace('\&quot', '\\"');
  console.log(JSON.stringify({ 'temp': tempDat }));
  console.log(tempDat);
}