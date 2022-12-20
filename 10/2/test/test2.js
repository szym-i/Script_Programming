import * as assert from 'assert';
import * as fss from 'fs';

describe('exists', function () {
    it('file', function () {
        assert.strictEqual(fss.existsSync('fs.js'), true)
    });
    it('dir', function () {
        assert.strictEqual(fss.existsSync('.'), true)
    });
    it('none', function () {
        assert.strictEqual(fss.existsSync('non-existing-path'), false)
    });
});

describe('isDirectory', function () {
    it('file', function () {
        assert.strictEqual(fss.isDirectory('fs.js'), false)
    });
    it('dir', function () {
        assert.strictEqual(fss.isDirectory('.'), true)
    });
    it('none', function () {
        assert.strictEqual(fss.isDirectory('non-existing-path'), false)
    });
});

describe('isFile', function () {
    it('file', function () {
        assert.strictEqual(fss.isFile('fs.js'), true)
    });
    it('dir', function () {
        assert.strictEqual(fss.isFile('.'), false)
    });
    it('none', function () {
        assert.strictEqual(fss.isFile('non-existing-path'), false)
    });
});