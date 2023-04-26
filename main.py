from website import create_app

app = create_app()

def main():
    print("Hello World")

if __name__ == "__main__":
    main()
    app.run(debug=True)