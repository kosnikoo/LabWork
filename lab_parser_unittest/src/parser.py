import requests
from bs4 import BeautifulSoup


class ForumParser:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        posts = soup.select(".blockpost")
        result = []

        for post in posts:
            raw_id = post.get("id") or post.get("data-post-id") or ""
            post_id = str(raw_id).removeprefix("p")
            message = post.select_one(".post_body_html, .message")
            username = post.select_one(".username")

            if username and message and post_id:
                result.append({
                    "id": int(post_id),
                    "name": username.get_text(strip=True),
                    "message": message.decode_contents().strip()
                })

        return result

    def save_to_db(self, parsed_data, repository):
        for comment in parsed_data:
            repository.add(
                comment["id"],
                comment["name"],
                comment["message"]
            )
        return len(parsed_data)
