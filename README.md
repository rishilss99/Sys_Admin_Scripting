# Python Scripts for Linux/Unix System Administration  

This repository contains a collection of Python scripts designed to automate various system administration tasks on Linux and Unix systems. The scripts utilize built-in and external Python libraries to enhance functionality, making system administration more efficient and automated.  

## Overview  

The repository is structured into multiple directories based on functionality, covering a wide range of system administration tasks:  

- **Data**: Scripts for data management, parsing, and transformation.  
- **Information**: Scripts for gathering and displaying system information such as CPU usage, memory status, and disk space.  
- **Introduction**: Introductory scripts demonstrating fundamental system administration operations.  
- **Networking**: Scripts for configuring network settings, monitoring connections, managing SSH sessions, and automating file transfers.  
- **Text**: Scripts for processing and manipulating text, including searching, formatting, and extracting information using regex.  

## Features and Tools  

This project leverages various Python libraries and modules to streamline system administration tasks:  

- **`re` (Regex)**: Used for pattern matching and text parsing.  
- **`subprocess`**: Facilitates execution of system commands directly from Python scripts, enhancing automation capabilities.  
- **`functools`**: Provides higher-order functions like caching and function composition for optimizing script execution.  
- **`xml.etree.ElementTree`**: Processes XML data, making it useful for parsing system logs, configuration files, and structured data formats.  
- **`ftplib`**: Enables FTP-based file transfers, useful for automating backups and remote storage.  
- **`pyro`**: Implements remote procedure calls (RPC) for distributed computing and inter-process communication.  
- **`paramiko`**: Provides secure SSH-based automation for remote server administration, executing commands, and transferring files via SFTP.  
- **`http` (Requests & HTTP Handling)**: Allows interaction with web services and APIs, useful for monitoring system health, fetching external data, or automating HTTP-based tasks.  

## Prerequisites

- **Python 3.x**: Ensure that Python 3 is installed on your system. You can verify the installation by running:

```bash
python3 --version
```

## Getting Started  

Clone the repository and navigate to the desired script directory:  

```bash
git clone https://github.com/rishilss99/Sys_Admin_Scripting.git
cd Sys_Admin_Scripting
python3 script_name.py
```