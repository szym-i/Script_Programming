// No use of any template system
var express = require('express'),
  logger = require('morgan'),
  fs = require('fs'),
  mongoose = require('mongoose');

var app = express();
var x = 1;
var y = 2;
var op = '+';

const { Schema } = mongoose;
const opSchema = new Schema({
    x: Number,
    y: Number,
    op: String
})
var Op = mongoose.model('Op', opSchema);

async function connect() {
  try {
      await mongoose.connect("mongodb://127.0.0.1:27017");
      console.log("Connected");
  } catch (error) {
      console.log(error);
  }
}

connect();

app.use(logger('dev'));                            // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

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

  let start = `<!DOCTYPE html>
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
      <tbody>\n`;
    let end = `      </tbody>
    </table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>`;
  str = '';
  for (var obj of json) {
    str += '        <tr> \n          <td>' + obj.x + '</td>\n          <td>' + obj.op + '</td>\n          <td>' + obj.y + '</td>\n          <td>' + eval(obj.x + obj.op + obj.y) + '</td>\n        </tr>\n';
  }
  res.send(start + str + end)
});

app.get('/calculate/:operation/:x/:y', async function (req, res) {
  var x = req.params.x;
  var y = req.params.y;
  var op = req.params.operation;
  if (!["+", "-", "*", "/"].includes(req.params.operation)) {// USE %2F instead of /
    res.status(400).send("Invalid operation.");
    return;
  }
  let newOp = new Op({ x: x, op: op, y: y});
  await newOp.save();
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

app.get('/results', async function (req, res) {
  let mongodata = await Op.find();

  let start = `<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>RESULTS</title>
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
      <tbody>\n`
    let end = `</tbody>
    </table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>`;

  str = '';
  for (var obj of mongodata) {
      str += '<tr><td>' + obj.x + '</td><td>' + obj.op + '</td><td>' + obj.y + '</td><td>' + eval('' + obj.x + obj.op + obj.y) + '</td></tr>';
  }

  res.send(start+str+end);
});

app.listen(3000, function () {
  console.log('The application is available on port 3000');
});
