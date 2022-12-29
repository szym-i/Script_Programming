var supertest = require("supertest");
var server = supertest.agent("http://localhost:3000");

var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

describe('GET /', function() {
      it('respond with html', function(done) {
         server
         .get('/')
         .expect('Content-Type', /html/)
         .expect(200, done);
      });

      it('Output validation', function (done) {
            function testValue(res) {
              b = `<!DOCTYPE html>
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
      <h2>1 + 2 = 3</h2>
    </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  </body>
</html>`
              res.text.split('').forEach(function(val, i){
                if (val != b.charAt(i))
                  console.log(res.text.at(i) + '!=' + b.at(i));         
              });
              if (res.text != b)
                throw new Error('response doesn\'t match')
            }
            server
              .get('/')
              .expect('Content-Type', /html/)
              .expect(200)
              .expect(testValue)
              .end(done)
      });
});


describe('JSON test', function () {	
      it('Output validation', function (done) {
        expect('./example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 5,
          "op": "+",
          "y": 5
        })
        expect('./example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 125,
          "op": "-",
          "y": 25
        })
        expect('./example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 16,
          "op": "*",
          "y": 6
        })
        expect('./example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 4,
          "op": "/",
          "y": 2
        })
        expect('./example.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 125,
          "y": 12,
          "op": "/"
        })
        done()
      })
})

describe('GET /json/:name', function () {
      it('respond with html', function (done) {
        server
          .get('/json/example.json')
          .expect('Content-Type', /html/)
          .expect(200, done);
      });

      it('Output validation', function (done) {
            function testValue(res) {
              b = `<!DOCTYPE html>
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
          <td>5</td>
          <td>+</td>
          <td>5</td>
          <td>10</td>
        </tr>
        <tr> 
          <td>125</td>
          <td>-</td>
          <td>25</td>
          <td>100</td>
        </tr>
        <tr> 
          <td>16</td>
          <td>*</td>
          <td>6</td>
          <td>96</td>
        </tr>
        <tr> 
          <td>4</td>
          <td>/</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr> 
          <td>125</td>
          <td>/</td>
          <td>12</td>
          <td>10.416666666666666</td>
        </tr>
      </tbody>
    </table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>`
              if (res.text != b)
                throw new Error('response doesn\'t match')
            }
            server
              .get('/json/example.json')
              .expect('Content-Type', /html/)
              .expect(200)
              .expect(testValue)
              .end(done)
      });
    })

describe('GET /calculate/:operation/:x/:y', function () {
  it('Response validation', function (done) {
    server
      .get('/calculate/+/1/1')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('Check response code', function (done) {
    server
      .get('/calculate/x/1/1')
      .expect('Content-Type', /html/)
      .expect(400, done)
  })

})
    
