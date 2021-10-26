# autobash
Uses the OpenAI Codex API to provide the user with autocompleted bash commands



## Usage 

This version of autobash is currently reliant on the user having access to the OpenAI codex beta. 
Future plans include making requests to a server and having the data provided to you. 

To use autobash, you'll need to obtain an OpenAI key and set it to the `OPENAI_KEY` environment variable.



## Installation 

To install autobash, clone the repository and install it using your Python's pip:

```sh
# clone 
git clone https://github.com/osilkin98/autobash
cd autobash

# install to python
pip install -e .

# export your API key to .bashrc
echo 'export OPENAI_API_KEY="your api key"' >> ~/.bashrc
```

## Example usage

```sh
[osilkin]$ autoshell "print 'hello world' to your cli"
echo 'hello world'

```