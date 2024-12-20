import os

def test_frontend_files_exist():
    frontend_dir = "frontend"
    required_files = ["app.py", "Dockerfile", "requirements.txt"]

    for file in required_files:
        file_path = os.path.join(frontend_dir, file)
        assert os.path.isfile(file_path), f"Le fichier {file} est manquant dans {frontend_dir}"
