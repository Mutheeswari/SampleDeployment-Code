from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def main():
    # return "Hai hello"
    return render_template("mainpage.html")




if __name__=="__main__":
    app.run()