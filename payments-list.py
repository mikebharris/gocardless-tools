import os
import gocardless_pro

client = gocardless_pro.Client(
    # We recommend storing your access token in an
    # environment variable for security
    access_token=os.environ['GC_ACCESS_TOKEN'],
    # Change this to 'live' when you are ready to go live.
    environment='live'
)

payments = client.payments.list().records
print('"date","reference","company","contact","email","description","amount","payout total"')
for payment in reversed(payments):
    payout = client.payouts.get(payment.links.payout)
    if payment.links.payout is not None:
        mandate = client.mandates.get(payment.links.mandate)
        customer = client.customers.get(mandate.links.customer)

        if customer.company_name is None:
            company_name = ""
        else:
            company_name = customer.company_name

        if customer.given_name is None and customer.family_name is None:
            contact = ""
        else:
            contact = customer.given_name + " " + customer.family_name

        print('"{date}","{payoutref}","{company}","{contact}",'
              '"{email}","{description}","{amount:.2f}","{payouttotal:.2f}"'.format(
            date=payout.arrival_date,
            payoutref=payout.reference,
            company=company_name,
            contact=contact,
            email=customer.email,
            description=payment.description,
            amount=payment.amount / 100,
            payouttotal=payout.amount / 100
        ))
