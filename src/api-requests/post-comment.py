import requests




class PostComment:
    """
    """
    def __init__(self) -> None:
        self.url = 'http://localhost:8000/'

    def post(self):
        """
        """

        res = requests.post(
            self.url,
            headers = {
                'Content-type': 'application/json'
            },
            json = {"text": "Fast API"},
        )

        print(res.text)