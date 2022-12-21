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
    borrow(user){
        if (this.n > 0){
            this.n-=1;
            user.borrowed.push(this.name);
            return 'The book has been borrowed'
        }
        else{
            return "Not enough books"
        }
    }
    return(user){
        if (user.borrowed.includes(this.name)){
            this.n+=1;
            return 'The book has been returned'
        }
        else
            return 'You cannot return this book'
    }
}

function readHTML(arg){
    if (fs.existsSync(arg) === true){
        if (fs.lstatSync(arg).isFile()) {
            return(`${fs.readFileSync(arg, 'utf8')}`);
        }
    }
}

function handle(m){
    console.log(m);
    arr = m.split('+');
    console.log(arr);
    var op = arr.at(0); 
    var title = arr.slice(1,-1).join(' ');
    var author = arr.at(-1);
    console.log(`op = ${op}`);
    console.log(`title = ${title}`);
    console.log(`author = ${author}`);
}

function requestListener(request, response) {
	var url = new URL(request.url, `http://${request.headers.host}`);
    if (request.method == 'POST') {
        var body = ''
        request.on('data', function(data) {
             body += data;
        })
        request.on('end', function() {
            body = body.slice(5);
            debug('Received body: ' + body);
            handle(body);
            response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
            response.write(body);
            response.end('\npost received');
        })
    }
	// if (url.pathname == '/submit') {
	// 	if (request.method == 'GET') {
    //         let p = url.searchParams.get('path');
	// 		process(response, p);
    //     }
    //     else {
    //         response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
	// 		response.write(`This application does not support the ${request.method} method`);
    //         response.end();
    //     }
	// }
	else {
		response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        //use readfile żeby nie pierdolić się z tym htmlem
		response.write(readHTML('response.html'));
		response.end();
	}
}

function process(response, p) {
    console.log(p.split(''));
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

var server = http.createServer(requestListener);
server.listen(8080);
console.log("The server was started on port 8080");
console.log("To stop the server, press 'CTRL + C'");

// u1 = new User('Szymon','Szymon',['TYTUŁ'])
// b1 = new Book('TYTUŁ','AuTorzy',1);
// console.log(b1.print());
// console.log(b1.borrow(u1));
// console.log(u1);
// console.log(b1.return(u1));
// console.log(u1);