import eel

eel.init("web")  # Ensure 'web' is your frontend directory

@eel.expose
def run_python():
    return "Python function executed successfully!"

eel.start("start.html", mode="chrome", port=5500)
