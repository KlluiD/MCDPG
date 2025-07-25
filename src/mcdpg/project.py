class Project:
    def __init__(self, name:str, namespace:str):
        self.name = name
        self._namespace = namespace
        self.description = ""
        self.project_output = f"./{self.name}/"

    @property
    def setting(self):
        return self
    
    def name(self, name):
        self.name = name
        return self
    
    def description(self, des:str):
        self.description = des
        return self
    
    def ouput_dir(self, dir: str):
        self.project_output = dir
        return self
    
    