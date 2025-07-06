# bindshell.py
This project is a lightweight reverse shell listener written in Python. It listens for incoming TCP connections from clients, receives shell commands, executes them on the host system, and sends back the output. It supports multiple concurrent clients using threading and logs all activity for transparency.

## Features

- Executes system commands from remote clients
- Receives and logs commands
- Sends back command output
- Handles multiple concurrent clients using threads
- Logs:
  - Server startup
  - Client connections
  - Received commands
  - Response sizes
- Gracefully handles the `exit` command

## Requirements

- Python 3.x
- `click` (for command-line argument parsing)

## Usage

Run the listener:

```
python3 shell.py --port 4444
```

Example Output:
```
[+] Started listening on port 4444
[+] Connection from 192.168.1.5:55322
[<] Received command: whoami
[>] Sending response (7 bytes)
[+] Client requested exit. Closing connection.
```

The command `exit` will close the connection from the client side.

## Security Warning

This script executes arbitrary shell commands received from remote clients without authentication or sandboxing. Do not expose it to the internet or use it on production systems. It is intended for use in controlled environments only, such as labs or educational demonstrations.


