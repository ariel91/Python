from flask import Flask
app = Flask(__name__)

@app.route("/about")
def hello():
    return """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<html>
    <head>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        <title>Site Template - Welcome!</title>
    </head>

    <body>
        <div class="Container">
            <div class="Header">

            </div>
<input type="text">
<input type="color">
<input type="submit">
            <div class="Menu">
                <ul id="nav"> 
                    <li>menu item</li>  
                    <li>menu item</li> 
                    <li>menu item</li>  
                    <li>menu item</li> 
                    <li>menu item</li>  
                    <li>menu item</li> 
                </ul> 
            </div>

            <div class="Body">

            </div>
        </div>

    </body>

    <footer>
        <div class="Footer">
            <b>Copyright - 2010</b>
        </div>
    </footer>
</html>

    
    
    """

app.run(debug=True) 
