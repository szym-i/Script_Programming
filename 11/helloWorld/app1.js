// No use of any template system
var express = require('express'),
  logger = require('morgan'),
  fs = require('fs');
var app = express();
var x = 1;
var y = 2;
var op = '+';

app.use(logger('dev'));                            // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

// The first route
app.get('/', function (req, res) {
  res.send(`<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <title>Your first page</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello World</h1>
      <h2>${x} ${op} ${y} = ${eval(x+op+y)}</h2>
    </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
</html>`);
});

app.get('/json/:name', function (req, res) {
  var file =req.params.name;
  let rawdata = fs.readFileSync(file);
  let json = JSON.parse(rawdata);

  res.send(`<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>JSON</title>
  </head>
  <body>
    <table class="table table-striped"> 
      <thead class="thead-light">
        <tr> 
          <th>x</th>
          <th>Operation </th>
          <th>y </th>
          <th>Result</th>
        </tr>
      </thead>
      <tbody>
        <tr> 
          <td>${json[0].x}</td>
          <td>${json[0].op}</td>
          <td>${json[0].y}</td>
          <td>${eval(json[0].x + json[0].op + json[0].y)}</td>
        </tr>
        <tr> 
          <td>${json[1].x}</td>
          <td>${json[1].op}</td>
          <td>${json[1].y}</td>
          <td>${eval(json[1].x + json[1].op + json[1].y)}</td>
        </tr>
        <tr> 
          <td>${json[2].x}</td>
          <td>${json[2].op}</td>
          <td>${json[2].y}</td>
          <td>${eval(json[2].x + json[2].op + json[2].y)}</td>
        </tr>
        <tr> 
          <td>${json[3].x}</td>
          <td>${json[3].op}</td>
          <td>${json[3].y}</td>
          <td>${eval(json[3].x + json[3].op + json[3].y)}</td>
        </tr>
        <tr> 
          <td>${json[4].x}</td>
          <td>${json[4].op}</td>
          <td>${json[4].y}</td>
          <td>${eval(json[4].x + json[4].op + json[4].y)}</td>
        </tr>
      </tbody>
    </table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>`);
});

app.get('/calculate/:operation/:x/:y', function (req, res) {
  var x = req.params.x;
  var y = req.params.y;
  var op = req.params.operation;
  if (!["+", "-", "*", "/"].includes(req.params.operation)) {// USE %2F instead of /
    res.status(400).send("Invalid operation.");
    return;
  }
  res.send(`<!DOCTYPE html>
  <html lang="en" data-bs-theme="dark">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
      <title>Your first page</title>
    </head>
    <body>
      <main class="container">
        <h1>Hello World</h1>
        <h2>The sum of ${x} and ${y} is ${eval(x+op+y)}</h2>
      </main>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    </body>
  </html>`);
});

app.listen(3000, function () {
  console.log('The application is available on port 3000');
});
