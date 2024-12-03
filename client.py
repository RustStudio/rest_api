import requests

# Paths to the certificate and key files
client_cert_path = 'tls/client/client.crt'  # Client certificate
client_key_path = 'tls/client/client.key'   # Client private key
ca_cert_path = 'tls/ca.crt'         # CA certificate

# URL of the API server
url = "https://127.0.0.1:8000/posts/1"

# Make the GET request with SSL certificates
response = requests.get(
    url,
    cert=(client_cert_path, client_key_path),  # Client certificate and key
    verify=ca_cert_path  # CA certificate to verify the server's certificate
)

# Print the response
print("Response Status Code:", response.status_code)
print("Response Content:", response.text)