# Aigeon AI Google News Search

## Project Description

Aigeon AI Google News Search is a Python-based server application designed to interact with the Google News search engine via the SerpApi. This application allows users to perform comprehensive searches on Google News, utilizing various parameters to refine and customize the search results. The server is built using the FastMCP framework, providing a robust and efficient platform for handling search requests.

## Features Overview

- **Google News Search Integration**: Seamlessly integrates with Google News through the SerpApi, enabling detailed and customizable news searches.
- **Flexible Query Parameters**: Supports a wide range of parameters to refine search results, including country, language, topic, publication, and more.
- **Advanced Search Options**: Offers options for sorting, caching, and asynchronous search execution.
- **Enterprise Features**: Includes an enterprise-only ZeroTrace mode for enhanced privacy and security.

## Main Features and Functionality

The core functionality of this application revolves around the `search_google_news` function, which is exposed as a tool via the FastMCP server. This function allows users to perform detailed searches on Google News by specifying various parameters. The application constructs a search query using these parameters and sends a request to the SerpApi, returning the search results in JSON format.

### Main Functions Description

#### `search_google_news`

This function is the primary interface for performing Google News searches. It accepts several parameters that allow users to customize their search queries:

- **q**: A string parameter defining the query for the Google News search. It can include any terms or operators used in a regular Google News search. This parameter cannot be used with `publication_token`, `story_token`, or `topic_token`.

- **gl**: A two-letter country code specifying the country for the search (e.g., `us` for the United States, `uk` for the United Kingdom).

- **hl**: A two-letter language code specifying the language for the search (e.g., `en` for English, `es` for Spanish).

- **topic_token**: A token used to access news results for a specific topic (e.g., 'World', 'Business'). It cannot be used with `q`, `story_token`, or `publication_token`.

- **publication_token**: A token used to access news results from a specific publisher (e.g., 'CNN', 'BBC'). It cannot be used with `q`, `story_token`, or `topic_token`.

- **section_token**: A token for accessing a subsection of a specific topic. It can only be used with `topic_token` or `publication_token`.

- **story_token**: A token for accessing news results with full coverage of a specific story. It cannot be used with `q`, `topic_token`, or `publication_token`.

- **so**: An integer parameter for sorting results. Supported values are `0` for relevance and `1` for date. It can only be used with `story_token`.

- **no_cache**: A boolean parameter to force fetching fresh results from SerpApi, bypassing any cached versions.

- **aasync**: A boolean parameter to submit the search asynchronously, allowing results to be retrieved later.

- **zero_trace**: An enterprise-only boolean parameter to enable ZeroTrace mode, which enhances privacy by not storing search parameters or metadata.

The function constructs a payload with the specified parameters, filters out any `None` values, and sends a GET request to the SerpApi endpoint. The response is returned in JSON format, providing comprehensive news results based on the search criteria.

This application is designed to provide a powerful and flexible tool for accessing Google News data, making it suitable for various use cases, including news aggregation, research, and analysis.