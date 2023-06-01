import openWindow from '@/utils/open-window';


describe('open', () => {
  test('should return the correct result', () => {
    const result = openWindow ('www.baidu.com','title',100,100);
    expect(result).toBe(null);
  });
});
