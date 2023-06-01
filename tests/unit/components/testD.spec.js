import { scrollTo } from '@/utils/scroll-to.js';


describe('move', () => {
  test('should return the correct result', () => {
    const result =scrollTo(1,1,false);
    expect(result).toBe(null);
  });
});
describe('move2', () => {
  test('should return the correct result', () => {
    const result =scrollTo(1,1000,false);
    expect(result).toBe(null);
  });
});
