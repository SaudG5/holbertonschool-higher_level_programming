# RESTful API

This project covers how systems communicate over HTTP: the basics of HTTP/HTTPS, consuming APIs with `curl` and Python, building APIs with `http.server` and Flask, and securing them with authentication.

## Task 0: Basics of HTTP/HTTPS

### Differences between HTTP and HTTPS

HTTP (Hypertext Transfer Protocol) sends data as plain text. Anyone who intercepts the traffic, for example on a public Wi-Fi network, can read or modify it.

HTTPS (HTTP Secure) is the same protocol wrapped in SSL/TLS encryption, which adds three protections:

- **Encryption:** the data is scrambled, so eavesdroppers cannot read it.
- **Integrity:** the data cannot be modified in transit without being detected.
- **Authentication:** the server proves its identity with a certificate, so the client knows it is talking to the real website.

| | HTTP | HTTPS |
|---|---|---|
| Encryption | None | SSL/TLS |
| Default port | 80 | 443 |
| Certificate | Not required | Required |
| Browser display | "Not secure" warning | Padlock icon |
| Typical use | Public, non-sensitive content | Logins, banking, email, any sensitive data |

### Structure of an HTTP request and response

Both requests and responses follow the same shape: a start line, headers, a blank line, and an optional body.

**Request**

```
GET /index.html HTTP/1.1            <- method, path, HTTP version
Host: www.example.com               <- headers
User-Agent: Mozilla/5.0
Accept: text/html
                                    <- blank line
(optional body, e.g. form data or JSON for POST/PUT)
```

**Response**

```
HTTP/1.1 200 OK                     <- HTTP version, status code, reason
Content-Type: text/html             <- headers
Content-Length: 1256
                                    <- blank line
<html>...</html>                    <- body
```

This structure can be observed in a browser by opening the developer tools (right-click, then "Inspect"), going to the **Network** tab, reloading the page, and clicking the first request to view its **Headers**.

### Common HTTP methods

| Method | Description | Use case |
|---|---|---|
| GET | Retrieves data without changing anything | Loading a web page or fetching a list of users from an API |
| POST | Sends data to create a new resource | Submitting a sign-up form or creating a new post |
| PUT | Replaces an existing resource with new data | Updating all the details of a user's profile |
| PATCH | Changes part of an existing resource | Updating only a user's email address |
| DELETE | Removes a resource | Deleting a comment or an account |

### Common HTTP status codes

Status codes are grouped by their first digit: 1xx (informational), 2xx (success), 3xx (redirection), 4xx (client errors), and 5xx (server errors).

| Code | Description | Scenario |
|---|---|---|
| 200 OK | The request succeeded | A page or API response loads normally |
| 201 Created | A new resource was created | After a POST request that successfully adds a new user |
| 301 Moved Permanently | The resource has a new URL | An old page address redirects to its new location |
| 400 Bad Request | The server could not understand the request | Sending malformed JSON or missing required fields |
| 401 Unauthorized | Authentication is required or has failed | Calling a protected API without a valid token |
| 403 Forbidden | The client is authenticated but not allowed | A regular user trying to access an admin-only page |
| 404 Not Found | The resource does not exist | Visiting a mistyped URL or a deleted page |
| 500 Internal Server Error | Something broke on the server | A bug in the server code crashes while handling the request |

## Task 1: Consume data from an API using command line tools (curl)

`curl` (Client URL) is a command-line tool for transferring data to or from a server. It is commonly used to test and debug APIs.

### Installing and checking curl

```bash
sudo apt update
sudo apt install curl
curl --version
```

The output shows the installed version and a list of supported protocols, such as `http`, `https`, and `ftp`.

### Fetching a web page

```bash
curl http://example.com
```

This prints the raw HTML of the page.

### Fetching data from an API

```bash
curl https://jsonplaceholder.typicode.com/posts
```

This returns a JSON array of 100 posts. Each post has a `userId`, `id`, `title`, and `body`:

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit..."
}
```

### Fetching only the headers

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

The `-I` flag returns only the status line and headers, without the content. The output starts with `HTTP/2 200` and includes headers such as `content-type: application/json; charset=utf-8`.

### Making a POST request

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

The `-X` flag sets the HTTP method, and `-d` sends data in the request body. The server responds with the created post:

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

The `id` is `101` because the API already contains 100 posts. JSONPlaceholder only simulates the creation, so the new post is not actually saved.

### Formatting JSON output with jq

```bash
sudo apt install jq
curl -s https://jsonplaceholder.typicode.com/posts/1 | jq
```

The `-s` flag hides the progress bar, and `jq` formats and colours the JSON so it is easier to read.

### Useful curl flags

| Flag | Purpose |
|---|---|
| `-I` | Fetch only the response headers |
| `-i` | Include the response headers along with the body |
| `-X` | Set the HTTP method (GET, POST, PUT, DELETE, etc.) |
| `-d` | Send data in the request body |
| `-H` | Add a request header, e.g. `-H "Content-Type: application/json"` |
| `-s` | Silent mode, hides the progress bar |
| `-u` | Send Basic authentication credentials, e.g. `-u user:password` |