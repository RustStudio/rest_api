![Cargo build](https://github.com/RustStudio/rest_api/actions/workflows/build.yaml/badge.svg) ![Cargo test](https://github.com/RustStudio/rest_api/actions/workflows/test.yaml/badge.svg) ![Cargo format](https://github.com/RustStudio/rest_api/actions/workflows/format.yaml/badge.svg)

# Rest API on Rust

This is a template to implement a REST API server on rust.

The template is implemented from online examples and resources so it is not owned by the developers.

# Usage
```
curl http://localhost:3030/posts/<u64>
```

# TLS

Generate CA certs
```
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 -out ca.crt
```

## Server
```
openssl genrsa -out server.key 2048
```
```
openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr

```
```
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -extfile openssl-san.cnf -extensions v3_req
```

> [!NOTE]
> Use `openssl x509 -in server.crt -text -noout` to verify if the certificate contains the IP address

## Client
```
openssl genrsa -out client.key 2048
```

```
openssl req -new -newkey rsa:2048 -nodes -keyout client.key -out client.csr
```

```
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365 -extfile openssl-san.cnf -extensions v3_req
```

> [!NOTE]
> Use `openssl x509 -in client.crt -text -noout` to verify if the certificate contains the IP address

## Whitelisting
On MacOS
```
ifconfig lo0 
```

If IP address defined not in list
```
sudo ifconfig lo0 alias <127.0.0.1>
```

## Usage
Run the `client.py` to test
