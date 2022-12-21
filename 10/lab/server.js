const fs = require('fs');
const http = require("http");
var debug = require('debug')('http');

class User{
    constructor(name,surname,borrowed){
        this.name = name;
        this.surname = surname;
        this.borrowed = borrowed;
    }
}

class Book{
    constructor(title,authors,n){
        this.title = title;
        this.authors = authors;
        this.n = n;
    }
    print(){
        return `${this.title} ${String(this.authors)} : ${this.n}`
    }
    borrow(){
        if (this.n > 0){
            this.n-=1;
            return 'The book has been borrowed'
        }
        else{
            return "Not enough books"
        }
    }
    return(){
        this.n+=1;
        return 'The book has been returned'
    }
}

function requestListener(request, response) {
	var url = new URL(request.url, `http://${request.headers.host}`);
	if (url.pathname == '/submit') {
		if (request.method == 'GET') {
            let p = url.searchParams.get('path');
			process(response, p);
        }
        else {
            response.writeHead(405, { "Content-Type": "text/plain; charset=utf-8" });
			response.write(`This application does not support the ${request.method} method`);
            response.end();
        }
	}
	else {
		response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
		response.write(`<form method="GET" action="/submit">
	    					<label for="path">Give a path</label>
	    					<input name="path">
	    					<br>
	    					<input type="submit">
	    					<input type="reset">
	    				</form>`);
		response.end();
	}
}

function process(response, p) {
    fs.stat(p, (err, stats) => {
        if (err) {
            response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
            response.write("path doesn't exist");
            response.end();
            return;
        }
        else{
            response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
            if (stats.isDirectory() === true){
                response.write("\npath is directory.");
            };    
            if (stats.isFile())
            {
                response.write("\npath is file.");
                fs.readFile(p, (err, data) => {
                    response.write("\nContent of the file:\n" + data);
                    response.end();
                });
            }
            else response.end();
        }
    });
}

//var server = http.createServer(requestListener);
//server.listen(8080);
//debug("The server was started on port 8080");
//debug("To stop the server, press 'CTRL + C'");

b1 = new Book('TYTUŁ','AuTorzy',1);
console.log(b1.print())
console.log(b1.borrow())
console.log(b1.print())
console.log(b1.return())
console.log(b1.print())