import { getMenu, createOrder } from '../../../web_app/src/services/api';

global.fetch = jest.fn();

describe('API Service', () => {
  beforeEach(() => {
    fetch.mockClear();
  });

  it('fetches menu successfully', async () => {
    const mockMenu = [
      { id: 1, name: 'محشي ورق عنب', price: 25.0 },
      { id: 2, name: 'محشي كوسا', price: 30.0 }
    ];

    fetch.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockMenu),
    });

    const result = await getMenu();
    expect(result).toEqual(mockMenu);
    expect(fetch).toHaveBeenCalledWith(`${process.env.REACT_APP_API_BASE_URL}/menu`);
  });

  it('creates an order successfully', async () => {
    const mockOrder = { id: 1, total: 55.0, status: 'pending' };
    const orderData = { items: [{ menu_item_id: 1, quantity: 2 }] };

    fetch.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockOrder),
    });

    const result = await createOrder(orderData);
    expect(result).toEqual(mockOrder);
    expect(fetch).toHaveBeenCalledWith(
      `${process.env.REACT_APP_API_BASE_URL}/orders`,
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify(orderData),
      })
    );
  });
});