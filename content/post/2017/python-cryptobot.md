---
title: 'How To Build A Cryptobot In Python Able To Fetch Data From External APIs'
description: >-
  A step by step tutorial to building a chatbot able to fetch crypto prices using Recast.AI (now SAP)
date: '2017-11-23T13:21:53.376Z'
categories: [🔧 Tutorials]
tags: [Chatbot, Python, Cryptos]
image: /img/2017/sato/satodemo.gif
---

Chatbots have an incredible  potential. Yet, for bots to be efficient, they must integrate and  exchange data with existing services and processes.

**The ability to fetch data from external API allows for more complex use case that a simple Q and A logic**. Moreover, this ability combined with NLP offers even more opportunities. 

For instance, Sato – the cryptobot we’ll be building today, is able to recognize all  cryptocurrencies, even those not even listed yet. I won’t have to do anything for him to be able to process queries on  crypto appearing even years from now, because Sato, deep-down,  understood what a cryptocurrency symbol is  (after being fed with thousands of them).

## **WHAT ARE WE BUILDING TODAY?**

By the end of this tutorial, we  will have a bot able to fetch data from a third party API depending on  what our users input, and reply to them with the value fetched. Here’s  the end-result of what we’ll build today: a cryptobot aka a chatbot able to fetch any cryptocurrency price.

What you’ll have by the end of this tutorial

In a rush? Here is all you need to build your own:

-   [The bot on SAP Conversational AI](https://cai.tools.sap/ahirice/sato-cryptobot/train/?utm_source=blog&utm_campaign=sato)
-   [The GitHub repo](https://github.com/Ahirice/sato/)

Need to see it to believe it? That’s wise!

[![chat-on-messenger](/img/2017/sato/messenger-button-1.png)](https://www.messenger.com/t/satofolio)Or if you would rather understand how it was made, go through with the tutorial.

## **I/ BUILD THE BASE OF YOUR BOT: CHOOSE YOUR PATH**

The goal today is to build bot able to recognize a question about pricing on any cryptocurrency. Let your imagination flow, **it could be really anything there is involving data available on third party APIs**. 

Before we dive in the tutorial, let me give you some information on how Sato works.

### **MEET SATO, THE CRYPTOBOT**

Sato is a bot made to answer basic questions about cryptocurrencies and fetch their prices. Here’s an  overview of what he can do:

1.  Fecth cryptocurrencies prices  (what we’ll build today): Sato recognizes cryptocurrencies symbol  (“ETH”, “BTC”) and fetch their price on [cryptocompare API](https://www.cryptocompare.com/api/) to finally return BTC and USD value to the user.
2.  Answer the users’ questions about wallets – online wallets, exchange wallets, cold wallets and hardware wallets.
3.  Address questions about private and public keys as well as the security of cryptocurrencies.
4.  Briefly present the main cryptocurrencies, currently BTC, ETH, BCH and LTC.

### **INSIDE SATO, CRYPTOBOT**

Today, we’ll focus on the skill fetching the crypto prices, as it requires an external API call. Essentially, Sato needs three things to be able to detect a question about crypto price and return the value asked:

Firstly, he needs an intent [(@crypto_price](https://cai.tools.sap/ahirice/sato-cryptobot/train/crypto_price?utm_source=blog&utm_campaign=sato)) with diverse expressions and cryptocurrencies mentioned, so he can  efficiently recognize these questions. Here are some of the expressions  used to define the @crypto_price intent:

![cryptobot @crypto_price expressions](/img/2017/sato/i-crypto-price.png)

A sample of the expressions used to define the @crypto_price intent

Secondly, for Sato to be able to recognize all cryptocurrencies, he’ll need the biggest list you can find. I found 1200+ on CoinMarketCap which is good enough to begin with. I created a gazette of the crypto names to improve its understanding.

Thirdly, we’ll need to build a skill which triggers when the @ask_price intent or #crypto_name entity is recognized:

![cryptobot - triggers](/img/2017/sato/skill1.png)

Sato – Cryptobot / crypto_main skill triggers

You can also add #crypto_name as a requirements, to make sure no API called is fired without parameters:

[![Sato - Cryptobot / crypto_main skill requirements](/img/2017/sato/cryptomissing.png)](https://mk0caiblog1h3pefaf7c.kinstacdn.com/wp-content/uploads/2017/11/cryptomissing.png)

Sato – Cryptobot / crypto_main skill requirements

This skill must also call your webhook that we’ll setup below:

[![Sato - Cryptobot / crypto_main skill actions](/img/2017/sato/webhookcryotio.png)](https://mk0caiblog1h3pefaf7c.kinstacdn.com/wp-content/uploads/2017/11/webhookcryotio.png)

Sato – Cryptobot / crypto_main skill actions

Don’t forget to add a memory reset after the webhook trigger, it’s required to clean the memory after each answer.

Finally, we’ll test our bot  straight in Messenger, so you’ll need to create a page and an app and  connect it. Everything is documented in the `CONNECT` tab and in [the getting started tutorial](https://cai.tools.sap/blog/build-your-first-bot-with-sap-conversational-ai/?utm_source=blog&utm_campaign=sato).

To keep it concise**, this tutorial will not detail the creation of a bot**. We’ll start from a functioning bot already. 

To meet me there, you have two options: 

-   Option A: build your own bot (who doesn’t have to be a cryptobot)
-   Option B: fork Sato and start from here.

You’ll also need[ an account on SAP Conversational AI](https://cai.tools.sap/signup/?utm_source=blog&utm_campaign=sato) to complete this tutorial.

### **A/ BUILD YOUR OWN BOT**

Nathan wrote an exhaustive tutorial on [how to build your first bot with SAP Conversational AI](https://cai.tools.sap/blog/build-your-first-bot-with-sap-conversational-ai/?utm_source=blog&utm_campaign=sato) so I’ll leave the basics to him. Feel free to [reach our to our community on Slack](https://slack.cai.tools.sap/) if you need some help.

### **B/ FORK THE BOT USED IN THIS TUTORIAL**

SAP Conversational AI is **collaborative bot platform**, it works pretty much like GitHub. Which means you can [simply fork my bot Sato](https://cai.tools.sap/ahirice/sato-cryptobot/?utm_source=blog&utm_campaign=sato) and start from here. Here’s how:

[![img](/img/2017/sato/Recast-AI-ahirice-sato-cryptobot-1024x158.png)](https://mk0caiblog1h3pefaf7c.kinstacdn.com/wp-content/uploads/2017/11/Recast-AI-ahirice-sato-cryptobot.png)

Forking a bot on SAP Conversational AI

## **II/ BASIC SERVER CODE AND REQUIREMENTS**

Since we want to interact with our bot, we’ll need a server to be able to receive the results of the NLP made by SAP Conversational AI and send our responses back.

On the [bot builder](https://cai.tools.sap), go to the `CODE` tab to find an example of base code required to start your API. We give examples in Node.JS, PHP, Python and Ruby. This tutorial will be Python only.

Here’s the base code for Python:

```
from flask import Flask, request, jsonify 
import json 

app = Flask(__name__) 
port = '5000' 

@app.route('/', methods=['POST']) 
def index(): 
  print(json.loads(request.get_data())) 
  return jsonify( 
    status=200, 
    replies=[{ 
      'type': 'text', 
      'content': 'Roger that', 
    }]
  ) 
 
@app.route('/errors', methods=['POST']) 
def errors(): 
  print(json.loads(request.get_data())) 
  return jsonify(status=200) 
 
app.run(port=port)
```

Take some time to look at the code to get a better understanding of what we’ll be doing: **we’ll build on this code during this tutorial**. You can save it in your favorite text editor for now.

### **REQUIREMENTS**

As you can see, the server script uses the [Flask as a web framework](http://flask.pocoo.org/), so we’ll need it.

For the API call, we’ll also use [Requests](http://docs.python-requests.org/en/master/). Let’s go ahead and install both:

```
pip install Flask
pip install requests
```

## **III/ TEST THE SERVER: NGROK**

Now that we have the base server,  let’s make it run and test it. It will allow us to be more incremental  in the process so the debugging (if any) is simplified.

To expose our local server to the internet, we’ll need ngrok. 

*Note: If you are using Windows like me, there is awesome package manager – [Chocolatey](https://chocolatey.org/) which works pretty much like apt-get on UNIX. With it, you’ll be able to install ngrok in one line `choco install ngrok_portable`. Moreover, Chocolatey adds ngrok to your PATH, allowing you to start ngrok from any terminal simply by typing `ngrok`.*

Now is the time to start our server and test it, this implies:

1.  Set a webhook trigger in your bot (detailed in step 1)
2.  Run your python script, 
3.  Expose port 5000 to the internet with ngrok: `ngrok http 5000`, 
4.  Copy the forwarding URL form ngrok and past it as your bot base URL on SAP Conversational AI

## **IV/ PREPARING THE EXTERNAL API CALL**

It’s about time to start building! Let’s have a look at the api call we’ll be doing to get the price of  any cryptocurrency. Several APIs are available for this purpose so I  just went ahead and picked one: [Cryptocompare API](https://www.cryptocompare.com/api/).

[Cryptocompare API](https://www.cryptocompare.com/api/) offers thousands of possibilities, but for the sake of simplicity, we’ll stick with the basics. **We want the price of the matched crypto in BTC, USD and EUR**.

Here’s how the call is structured(here for ETH):`https://min-api.cryptocompare.com/data/price?fsym="ETH"&tsyms=BTC,USD,EUR"`

You have two parameters:

-   `fsym`: the symbol of the cryptocurrency, this is where we’ll need to fetch the crypto_name recognized in the #crypto_name entity.
-   `tsyms`: the currency in which the price will be returned. We chose BTC, USD and EUR here.

So, in our case, we’ll only need to adapt the `fsym` parameter to the recognized cryptocurrency, while the rest of the call stays the same.

## **V/ ADAPT THE API CALL TO INCLUDE THE SYMBOL RECOGNIZED IN THE USER INPUT**

Now that we know how to fetch the prices, we need to go back to our server code and upgrade it so it can:

-   Know the #crypto_name recognized by SAP Conversational AI.
-   Make an API call to Cryptocompare using the #crypto_name.

Let’s get started!

### **A/ FINDING OUR DATA IN SAP Conversational AI JSON**

Let’s have a look at the data returned by SAP Conversational AI on a user input. To do so, you click the `CHAT WITH YOUR BOT` button present on all pages, on the bottom-right corner. Then, you can  switch between the conversation and the JSON view by clicking on the  orange information circle as below:

[![img](/img/2017/sato/priceOMG.png)](https://mk0caiblog1h3pefaf7c.kinstacdn.com/wp-content/uploads/2017/11/priceOMG.png)

Check the JSON of the conversation.

 

Here, our symbol is accessible with `['conversation']['memory']['crypto']['raw']`. Since the value and the raw and identical in this case, you can use either.

On our server, the JSON returned by the website test panel is **encapsulated into the `data` dictionary** (see server code). So we need an extra step to retrieve it on our server:

```
# FETCH THE CRYPTO NAME
crypto_name = data['conversation']['memory']['crypto']['value']
```

### **B/ MAKE AN API CALL USING THE RECOGNIZED ENTITY**

For the API call, we’ll be using  Requests. Don’t forget to import it in your server’s script, then, we  build our base request (r):

```
import requests
r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")
```

Go ahead and print it, but you may be disappointed:

![cryptobot - cryptocompare API response](/img/2017/sato/r.png)

Indeed, if you want to get the values returned by the call, you need to print `r.json()`. The good news is that JSON returned by Cryptocompare is really as simple as it could be:

![cryptobot - JSON from cryptocompare API](/img/2017/sato/cryptocompare-json.png)

Cryptocompare JSON

Great! Now, we just have one last step to figure out: returning the prices to the user.

## **VI/ RETURNING THE DATA FETCHED TO THE USER**

Now, it’s time to finish our base  server code upgrade: we need to edit the replies returned to include our freshly fetched data. To do so, we’ll edit the message returned by our  server code:

```
return jsonify( 
    status=200, 
    replies=[{ 
      'type': 'text', 
      'content': 'Roger that', 
    }],
```

We’ll be editing the replies only, to include the prices we fetched:

```
   replies=[{
      'type': 'text',
      'content': 'The price of %s is %f BTC and %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
    }],
```

Since the reply is a string, we must use the modulo (%) operator to  include our prices in the string. Here, the first %s tells Python to  look for a string while the two following %f indicates floats.

Our upgraded server is now finished, here’s the whole code :

```
from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
port = '5000'

@app.route('/', methods=['POST'])
def index():
  data = json.loads(request.get_data())

  # FETCH THE CRYPTO NAME
  crypto_name = data['conversation']['memory']['crypto']['raw']

  # FETCH BTC/USD/EUR PRICES
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'The price of %s is %f BTC and %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)
```

With our new server completed, we now have all the pieces of our puzzle. Let’s assemble it:

1.  Run your python script, 
2.  Expose port 5000 to the internet with ngrok: `ngrok http 5000`, 
3.  Copy the forwarding URL form ngrok and past it as your bot base URL on SAP Conversational AI

Now that you have the basics to build a bot able to fetch third party data, what’s gonna be? You show us!

PS: Since this tutorial uses ngrok, your computer must be on and ngrok must be running for your bot to function.

[If you want to make your bot always available, follow the next tutorial](https://cai.tools.sap/blog/github-repo-heroku/).