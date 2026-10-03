from pathlib import Path
if __name__ == '__main__':
    root=Path(__file__).resolve().parents[1]
    for name in ('Dockerfile','compose.yaml','.env.example','app/main.py'):
        print(name,'present:',(root/name).exists())
    print('File presence is not a deployment or health test. Run Compose locally to validate.')
