const express = require('express');
const logger = require('morgan');
const cors = require('cors');
/************* */
const app1 = express();
const app2 = express();
app1.use(cors());
app2.use(cors());
/************* */
app1.use(logger('dev'));
app2.use(logger('dev'));
/************* */
app1.listen(3000, function () {
	    console.log('The application is available on port 3000');
});
app2.listen(3001, function () {
	    console.log('The application is available on port 3001');
});
/************* */
app1.get('/', function (req, res) {
	    res.send(res.send(`<!DOCTYPE html>
        <html lang="en" data-bs-theme="dark">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <title>Your first page</title>
          </head>
          <body>
            <main class="container">
                <input type="text" id="area">
                <input type="text" id="location">
                <input type='button' value='Download' style="background-color:blue; color:white" onclick="download()">
                <h1>Remote</h1>
                <div id='remote'>
                    Remote date and time
                </div>
                <!-- ***************** -->
                <h1>Local</h1>
                <div id='local'>
                    Local date and time
                </div>
            </main>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
            <script>
                var remote = document.getElementById("remote");
                var local = document.getElementById("local");
                var area_input = document.getElementById("area");
                var local_input = document.getElementById("location");
                
                function download() {
                    remote.textContent = "Downloading data";
                    local.textContent = "Downloading data";
                    
                    fetch('http://worldtimeapi.org/api/timezone/' + area_input.value + '/' + local_input.value)
                    .then(function (response) { 
                    if (!response.ok) {
                        throw Error(response.statusText);
                    }
                    response.text().then(x => {
                        if (x == "This website is currently experiencing high load.")
                            remote.textContent = "The server is overloaded";
                        else {
                            remote.textContent = JSON.parse(x).datetime;
                        }
                    });
                    })
                    .catch(function (error) { 
                        window.alert(error);
                    });
                    
                    fetch('http://localhost:3001')
                    .then(function (response) { 
                    if (!response.ok)
                        throw Error(response.statusText);
                        response.text().then(x => new window.DOMParser().parseFromString(x, "text/xml")).then(x => {
                            local.textContent = x.getElementById("date").textContent + " " + x.getElementById("time").textContent;
                        });
                    })
                    .catch(function (error) {
                    window.alert(error);
                    });
                }
            </script>
          </body>
        </html>`));
});

app2.get('/', function (req, res) {
    var date = new Date();
    var xml = "<?xml version='1.0'?> <div><span id='date'>"+date.toDateString()+"</span><span id='time'>"+date.toTimeString()+"</span></div>"
	res.send(xml);
});
/************* */
console.log("To stop the server, press 'CTRL + C'");