var express = require('express'),
    logger = require('morgan'),
    fs = require('fs'),
    mongoose = require('mongoose');

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

var app = express();
var x = 1;
var y = 2;

app.set('views', __dirname + '/views');               // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');                        // Use the 'Pug' template system
app.locals.pretty = app.get('env') === 'development'; // The resulting HTML code will be indented in the development environment

app.use(logger('dev'));                            // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

app.get('/', function (req, res) {
    res.render('index', {x: x, op: '+',y: y}); // Render the 'index' view
});

app.get('/json/:name', function (req, res) {
    var file = req.params.name;
    let rawdata = fs.readFileSync(file);
    let json = JSON.parse(rawdata);

    res.render('json', { json: json });
});

app.get('/calculate/:operation/:x/:y', async function (req, res) {
    var x = req.params.x;
    var y = req.params.y;
    var op = req.params.operation;
    if (!["+", "-", "*", "/"].includes(req.params.operation)) { // USE '%2F' instead of '/'
      res.status(400).send("Invalid operation.");
      return;
    }
    let newOp = new Op({ x: x, op: op, y: y});
    await newOp.save();
    res.render('index', {x: x, op: op, y: y}); 
});

app.get('/results', async function (req, res) {
    let json = await Op.find();

    res.render('json', { json: json });
});

app.listen(3000, function () {
    console.log('The application is available on port 3000');
});
