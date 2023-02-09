const express = require('express');
const logger = require('morgan');
const app = express();
const { parse } = require('querystring');

// Configuring the application
app.set('views', __dirname + '/views');
app.set('view engine', 'pug');
app.locals.pretty = app.get('env') === 'development';

// Determining the contents of the middleware stack
app.use(logger('dev'));     
// app.use(express.static(__dirname + '/public'));

// *** Route definitions ***

// The first route
app.get('/', function (req, res) {
    res.render('index');
});

// The second route
app.get('/submit', function (req, res) {
    // Return the greeting in the format preferred by the WWW client
    switch (req.accepts(['html', 'text', 'json', 'xml'])) {
        case 'json':
            // Send the JSON greeting
            res.type('application/json');
            res.json({ welcome: "Hello World" });
            console.log("The server sent a JSON document to the browser");
            break;

        case 'xml':
            // Send the XML greeting
            res.type('application/xml');
            res.send('<welcome>Hello World</welcome>');
            console.log("The server sent an XML document to the browser");
            break;

        default:            
            var url = new URL(req.url, `http://${req.headers.host}`);
            if (url.searchParams.has("imie")) {
                var params = url.searchParams;
                var welcomeText = "Witaj " + params.get("imie");
            }
            else {
                var welcomeText = "Hello World";
            }
            // Send the text plain greeting
            res.type('text/plain');
            res.send(welcomeText);
            console.log("The server sent a plain text to the browser");
        }
});

app.post('/submit', function (req, res) {
    // Return the greeting in the format preferred by the WWW client
    switch (req.accepts(['html', 'text', 'json', 'xml'])) {
        case 'json':
            // Send the JSON greeting
            res.type('application/json');
            res.json({ welcome: "Hello World" });
            console.log("The server sent a JSON document to the browser");
            break;

        case 'xml':
            // Send the XML greeting
            res.type('application/xml');
            res.send('<welcome>Hello World</welcome>');
            console.log("The server sent an XML document to the browser");
            break;

        default:            
            if (req.method === 'POST') {
                let body = '';
                req.on('data', chunk => {
                    body += chunk.toString(); // convert Buffer to string
                });
                req.on('end', () => {
                    console.log("Witaj " + (parse(body)).imie);
                    res.end("Witaj " + (parse(body)).imie);
                });
            }
    }
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});