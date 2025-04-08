# Pyblish Debug

This is an example setup to reproduce an issue with setting breakpoints in pyblish-base 

## How to Install

### Using `uv`
1. Install `uv` if not already installed:
    ```bash
    pip install uv
    ```


### Using `pip`
1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to run

I have probided a vscode launch.json file. All you need to do is open this folder in vscode and run debugging

## what will happen

If the Bugfix is not yet applied, nothing will happen. If the bugfix has been added, a breakpoint should trigger.