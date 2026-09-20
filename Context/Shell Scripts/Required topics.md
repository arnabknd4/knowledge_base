# 🐚 Shell Script (Linux Bash)- 
## Core Building Blocks
- Variables (VAR=value, $VAR)- 
- Conditionals (if, cas- e)
- Loops (for, wh- ile)
- Functions
- File redirection (>,-  >>, 2>)
- Exit codes ($?)

## Essential Commands
- ls, cd, pwd, cat,-  grep, awk, se- d
- chmod, cho- wn
- ps, kill, top
- curl, wget

## Real‑Life Usage
Automating log cleanup: 

- `find /var/log -type f -name "*.log" -mtime +7 -exec rm {} \;`
- `./deploy.sh && echo "Deployment successful"`

# 🐍 Python
## Core Building Blocks
- Data types (list, dict, tuple, set)
- Control flow (if, for, while)

## Functions & modules
- File I/O
- Error handling (try/except)
- Virtual environments (venv)

## Essential Commands
- pip install <package>
- python script.py
- venv activation: source venv/bin/activate

## Real‑Life Usage
Parsing JSON config:
``` python
import json
with open("config.json") as f:
    data = json.load(f)
    print(data["cluster"])
```
REST API call
``` python
import requests
r = requests.get("https://api.github.com")
print(r.status_code)

```
# 🦫 Go (Golang)
## Core Building Blocks
- Packages & imports
- Variables & constants
- Functions
- Structs & interfaces
- Goroutines & channels (concurrency)
- Error handling (error type)

## Essential Commands
- go run file.go
- go build
- go mod init, go mod tidy
- go test

## Real‑Life Usage
Simple HTTP server:
``` go
package main
import ("fmt"; "net/http")
func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, DevOps!")
}
func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}

```
CLI tool for automation (build/deploy scripts).