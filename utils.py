import aiohttp, re
from datetime import timedelta

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

def get_time(
    key: str, string: str
) -> int:  # CircuitSacul == pog (he made this)
    string = f" {string} "
    results = re.findall(f" [0-9]+{key}", string)
    if len(list(results)) < 1:
        return 0
    r = results[0]
    r = r[1 : 0 - len(key)]
    return int(r)

def str_time_to_timedelta(
    time_string: str,
) -> timedelta:  # CircuitSacul == pog (he made this)
    time_string = time_string.lower()

    days = get_time("d", time_string)
    hours = get_time("h", time_string)
    minutes = get_time("m", time_string)
    seconds = get_time("s", time_string)

    actual_seconds = 0
    if hours:
        actual_seconds += hours * 3600
    if minutes:
        actual_seconds += minutes * 60
    if seconds:
        actual_seconds += seconds

    datetime_obj = timedelta(
        days=days,
        seconds=actual_seconds,
    )
    return datetime_obj
