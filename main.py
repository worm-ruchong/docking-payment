import requests
import hashlib

# Define the API endpoint URL
url = 'https://www.mazfu.com/pay/apisubmit'

# Set the required parameters
merchant_id = 'YOUR_MERCHANT_ID'
payment_method = 'PAYMENT_METHOD'
merchant_order_number = 'MERCHANT_ORDER_NUMBER'
server_notification_url = 'SERVER_NOTIFICATION_URL'
page_jump_url = 'PAGE_JUMP_URL'
product_name = 'PRODUCT_NAME'
amount = 'PAYMENT_AMOUNT'
site_name = 'SITE_NAME'
api_key = 'YOUR_API_KEY'

# Create a dictionary of parameters
params = {
    'pid': merchant_id,
    'type': payment_method,
    'out_trade_no': merchant_order_number,
    'notify_url': server_notification_url,
    'return_url': page_jump_url,
    'name': product_name,
    'money': amount,
    'sitename': site_name,
}

# Generate the signature string
sorted_params = sorted(params.items())
signature_string = '&'.join(f'{k}={v}' for k, v in sorted_params) + api_key
signature = hashlib.md5(signature_string.encode()).hexdigest()

# Add the signature and sign_type parameters
params['sign'] = signature
params['sign_type'] = 'MD5'

# Make the POST request
response = requests.post(url, data=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the payment link from the response
    payment_link = response.text
    print("Payment link:", payment_link)
else:
    print("Request failed with status code:", response.status_code)
