const fs = require('fs');
const http = require("http");
var debug = require('debug')('http');

const book1 = ["1984", ["G.Orwell"], "", "","/images/1984.jpg"];
const book2 = ["Python", ["A","A"], "", "","/images/python.jpg"];
const book3 = ["test",["test"],"test","test",,"/images/krzyk.jpg"];
const book4 = ["Python", ["A","A"], "", "","/images/python.jpg"];
let books = [book1,book2,book3,book4];

function readHTML(arg){
    if (fs.existsSync(arg) === true){
        if (fs.lstatSync(arg).isFile()) {
            return(`${fs.readFileSync(arg, 'utf8')}`);
        }
    }
}

function readimage(arg){
    if (fs.existsSync(arg) === true){
        if (fs.lstatSync(arg).isFile()) {
            return(`${fs.readFileSync(arg, 'utf8')}`);
        }
    }
}

function print_books(books){
    let str='Avaliable books:<br>';
    books.forEach(book =>{
      if (book[2] === '' && book[3] == ''){
        str+=`"${String(book[0])}" ${book[1]}<br>`;
      }
    });
    return(str);
  }

function generateImages(books){
    str = ''
    books.forEach(book =>{
        str+=`<img src="${book.at(-1)}">\n`
    });
    return str;
}

function handle(m){
    debug(`Received message:${m}`);
    arr = m.split('+');
    if (arr.length < 3){
        console.log('Błąd!');
    }
    console.log(arr);
    var op = arr.at(0); 
    var title = arr.slice(1,-1).join(' ');
    var author = arr.at(-1);
    debug(`op = ${op}\ntitle = ${title}\nauthor = ${author}`);
}

function requestListener(request, response) {
	var url = new URL(request.url, `http://${request.headers.host}`);
    if (request.method == 'POST') {
        if ( 1 === 1){
            var body = ''
            request.on('data', function(data) {
                body += data;
            })
            request.on('end', function() {
                body = body.slice(5);
                debug('Received body: ' + body);
                handle(body);
                response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
                response.write(readHTML('response.html'));
                //console.log(readimage('python.txt'));
                response.write(`<img src="data:image/png;base64,${readHTML('images/python.txt')}" alt="Python" />`);
                response.write(`<div>${body}</div>`);
                response.write(`<div>${print_books(books)}</div>`);
                response.end();
            })

        }

    }
	else {
		response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
		response.write(readHTML('response.html'));
        response.write(`<div>${print_books(books)}</div>`);
		response.end();
	}
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