//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8080");

// UNIT test begin
describe('GET /submit?path=', function () {
      it('a', function (done) {
            server.get('/submit?path=a')
                  .expect('Content-Type', /text\/plain/)
                  .expect(404, "path doesn't exist", done);
      });
      it('.', function (done) {
            server.get('/submit?path=.')
                  .expect('Content-Type', /text\/plain/)
                  .expect(200, "\npath is directory.", done);
      });
      it('/etc', function (done) {
            server.get('/submit?path=/etc')
                  .expect('Content-Type', /text\/plain/)
                  .expect(200, "\npath is directory.", done);
      });
      it('../2/tekst.txt', function (done) {
            server.get('/submit?path=../2/tekst.txt')
                  .expect('Content-Type', /text\/plain/)
                  .expect(200, "\npath is file.\nContent of the file:\n12314\n31421\nsasa", done);
      });
});