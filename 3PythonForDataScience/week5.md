# Week 5
## Simple APIs Part 1
- Application Program Interface
- Communicate with other software with inputs and outputs
- REST: representational state transfer interface, interact through web services
    - Client sends requests to the resource/web service
    - HTTP message returns response (usually JSON)
  
## Simple APIs Part 2
- API keys and endpoints
  - API key is used to access API service
  
- Used Watson speech to text API as an example

## REST APIs and HTTP Requests Part 1
- Understanding HTTP protocol: sending request and getting response through web
- URL or uniform resource locator
  - scheme
  - internet address or base url
  - route
  
- Request message
  - start line (request method like GET) and header, can also have body
  
- Response message
  - start line (HTTP status code like 200), header, and body
  
## REST APIs and HTTP Requests Part 2
- Using Requests library in Python
- URL query strings for parameters
- POST requests will send data via request body

## HTML for Webscraping
- Review of HTML composition and tags
- Document tree to determine/view parent-children relationships
- HTML tables

## Webscraping
- Process to automatically extract data from a website
- Using Requests and Beautiful Soup libraries
- Beautiful Soup find_all filter 

## Working with different file formats (csv, xml, json, xlsx)
- Library pandas capable of opening csv with read_csv
- Library json for json files