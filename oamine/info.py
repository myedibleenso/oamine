from typing import List, Text

class AppInfo:
    """
    General information about the application.
    """

    version: Text = "0.1"
    description: Text = "Facet discovery from product titles"
    
    authors: List[Text] = [
      "Xinyang Zhang", 
      "Chenwei Zhang", 
      "Xian Li", 
      "Luna Xin Dong", 
      "Jingbo Shang", 
      "Christos Faloutsos", 
      "Jiawei Han"
    ]
    contact: Text = "ghp@amazon.com"
    repo: Text = "https://github.com/myedibleenso/oamine"
    license: Text = "Apache 2.0"

    @property
    def download_url(self) -> str:
        return f"{self.repo}/archive/v{self.version}.zip"


info = AppInfo()