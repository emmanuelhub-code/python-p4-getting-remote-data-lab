import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Returns the raw response body as bytes (exactly what the test expects).
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content  # bytes

    def load_json(self):
        """
        Loads JSON from the response.
        """
        return json.loads(self.get_response_body())


# Example usage
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    data = requester.load_json()
    print(json.dumps(data, indent=2))
