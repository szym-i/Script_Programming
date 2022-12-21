/**
 * Simple class with one method - sum()
 * @class Operation
 * @param {Number} x - First value
 * @param {Number} y - Second value
 */

class Operation {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  /**
    * Get a sum of two variables
    * @method sum
    * @returns {Number} The sum of this.x + this.y
    */

  sum() {
    return this.x + this.y;
  }
};

export { Operation }
