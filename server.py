import os
import requests
from typing import Union, Annotated, Literal
from pydantic import Field
from mcp.server import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP('serp-news-search')

serp_url = "https://serpapi.com/search"
serp_api_key = os.getenv("SERP_API_KEY")


@mcp.tool()
def search_google_news(
    q: Annotated[Union[str, None], Field(
        description="Parameter defines the query you want to search. You can use anything that you would use in a regular Google News search. e.g. site:, when:. Parameter can't be used together with publication_token, story_token, and topic_token parameters."
    )] = None,

    topic_token: Annotated[Union[str, None], Field(
        description="Parameter defines the Google News topic token. It is used for accessing the news results for a specific topic (e.g., 'World', 'Business', 'Technology'). The token can be found in our JSON response or the URL of the Google News page. Parameter can't be used together with q, story_token, and publication_token parameters."
    )] = None,

    publication_token: Annotated[Union[str, None], Field(
        description="Parameter defines the Google News publication token. It is used for accessing the news results from a specific publisher (e.g., 'CNN', 'BBC', 'The Guardian'). The token can be found in our JSON response or the URL of the Google News page. Parameter can't be used together with q, story_token, and topic_token parameters."
    )] = None,

    section_token: Annotated[Union[str, None], Field(
        description="Parameter defines the Google News section token. It is used for accessing the sub-section of a specific topic. (e.g., 'Business -> Economy'). The token can be found in our JSON response or the URL of the Google News page. Parameter can only be used in combination with topic_token or publication_token parameters."
    )] = None,

    story_token: Annotated[Union[str, None], Field(
        description="Parameter defines the Google News story token. It is used for accessing the news results with full coverage of a specific story. The token can be found in our JSON response or the URL of the Google News page. Parameter can't be used together with q, topic_token, and publication_token parameters."
    )] = None,

    so: Annotated[Union[Literal[0, 1], None], Field(
        description="Parameter defines the sorting method. Results can be sorted by relevance or by date. By default, the results are sorted by relevance. Supported values: 0 - Relevance, 1 - Date. Parameter can only be used in combination with story_token parameter."
    )] = None,

    no_cache: Annotated[Union[bool, None], Field(
        description="Parameter will force SerpApi to fetch the Google News results even if a cached version is already present. A cache is served only if the query and all parameters are exactly the same. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month. It can be set to false (default) to allow results from the cache, or true to disallow results from the cache. no_cache and async parameters should not be used together."
    )] = None,

    aasync: Annotated[Union[bool, None], Field(
        description="Parameter defines the way you want to submit your search to SerpApi. It can be set to false (default) to open an HTTP connection and keep it open until you got your search results, or true to just submit your search to SerpApi and retrieve them later. In this case, you'll need to use our Searches Archive API to retrieve your results. async and no_cache parameters should not be used together. async should not be used on accounts with Ludicrous Speed enabled."
    )] = None,

    zero_trace: Annotated[Union[bool, None], Field(
        description="Enterprise only. Parameter enables ZeroTrace mode. It can be set to false (default) or true. Enable this mode to skip storing search parameters, search files, and search metadata on our servers. This may make debugging more difficult."
    )] = None
):
    """Search Google News for comprehensive news results"""
    payload = {
        'engine': "google_news",
        'api_key': serp_api_key,
        'q': q,
        'topic_token': topic_token,
        'publication_token': publication_token,
        'section_token': section_token,
        'story_token': story_token,
        'so': so,
        'no_cache': no_cache,
        'async': aasync,
        'zero_trace': zero_trace
    }
    # Remove None values
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(serp_url, params=payload)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    mcp.run(transport="stdio")