import aiohttp, re

async def search_youtube(query: str) -> str:

    yt_search_url = "https://www.youtube.com/results?search_query="
    yt_video_url = "https://www.youtube.com/watch?v="

    formatted_query = "+".join(query.split())
    request_url = yt_search_url + formatted_query

    async with aiohttp.request("GET", request_url) as resp:
        html = (await resp.read()).decode()

    video_ids = re.findall(r"watch\?v=(\S{11})", html)
    first_result = yt_video_url + video_ids[0]
    return first_result