
# File Downloader

This Python script downloads files from URLs listed in a JSON file. The script reads the JSON file, extracts the links, and downloads each file into the specified directory.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests
```

## Setup

1. Clone the repository or download the script.

2. Create a JSON file named `links.json` in the same directory as the script. The JSON file should contain the URLs of the files to be downloaded.

Example `links.json`:
```json
{
    "urls": [
        "http://example.com/file1.zip",
        "http://example.com/file2.zip",
        "http://example.com/file3.zip",
        "http://example.com/file4.zip",
        "http://example.com/file5.zip",
        "http://example.com/file6.zip",
        "http://example.com/file7.zip",
        "http://example.com/file8.zip",
        "http://example.com/file9.zip",
        "http://example.com/file10.zip"
    ]
}
```

3. Place the `links.json` file in the same directory as the Python script.

## Usage

Run the script using a Python interpreter:

```sh
python downloader.py
```

The script will read the URLs from `links.json` and download each file into the current directory.

## Code Explanation

### `download_file(url, dest_folder)`

This function downloads a file from the given URL and saves it in the specified destination folder.

- `url`: URL of the file to be downloaded.
- `dest_folder`: Destination folder where the file will be saved.

### `load_urls(json_file)`

This function loads the URLs from the specified JSON file.

- `json_file`: Path to the JSON file containing the URLs.

### `main()`

The main function reads the URLs from `links.json` and downloads each file by calling `download_file()`.

### Example JSON Structure

The JSON file should have the following structure:

```json
{
    "urls": [
        "http://example.com/file1.zip",
        "http://example.com/file2.zip"
    ]
}
```

## License

This project is licensed under the MIT License.
