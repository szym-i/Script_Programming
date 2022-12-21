import { Operation } from "../module.js";
import assert from 'assert';

describe('The sum() method', function () {
  it('Returns 4 for 2+2', function () {
    assert.strictEqual(new Operation(2, 2).sum(), 4)
  });
  it('Returns 0 for -2+2', function () {
    assert.strictEqual(new Operation(-2, 2).sum(), 0)
  });
});