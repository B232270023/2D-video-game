/**
 * Хоёр тооны нийлбэрийг олно.
 * @param {number} a - Эхний тоо
 * @param {number} b - Хоёр дахь тоо
 * @returns {number} Хоёр тооны нийлбэр
 * @throws {Error} Хэрэв оруулсан өгөгдөл тоо биш бол алдаа буцаана
 */
function sum(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Тоо оруулах шаардлагатай!');
  }
  return a + b;
}

module.exports = sum;