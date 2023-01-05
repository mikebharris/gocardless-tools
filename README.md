# GoCardless Tools
Tools to interact with GoCardless for accounting purposes

* [Export Payments as CSV including customer and payout details](payments-list.py)

# Installation

You need to install the [GoCardless Pro Python client library](https://github.com/gocardless/gocardless-pro-python) with:

```shell
pip install gocardless_pro
```

And then run the tool with:

```shell
GC_ACCESS_TOKEN=live_?????? python3 payments-list.py
```

The access token you create and obtain from within the [GoCardless login Developer section](https://manage.gocardless.com/developers).