import json
import os
from datetime import datetime

class StudyFlowEngine:
    def __init__(self, filename = "studyflow_data.json"):
        self.filename = filename
        #mengisi data awal kalo json belum dibuat
        self.data = {
                    "tasks": [],
                    "schedule": []
                    }
        self.load_data()

    #fungsi database
    def load_data(self):
        """Membaca data dari file json"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.data = json.load(file)
                except json.JSONDecodeError:
                    #jika file corrupt, pakai data kosong
                    self.data = {"tasks": [], "schedule": []}