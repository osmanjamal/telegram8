import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Menu from '../../../web_app/src/components/Menu';

jest.mock('../../../web_app/src/services/api', () => ({
  getMenu: jest.fn(() => Promise.resolve([
    { id: 1, name: 'محشي ورق عنب', price: 25.0, description: 'ورق عنب محشي بالأرز واللحم' },
    { id: 2, name: 'محشي كوسا', price: 30.0, description: 'كوسا محشي بالأرز واللحم' }
  ]))
}));

test('renders menu items', async () => {
  render(<Menu />);
  
  expect(await screen.findByText('محشي ورق عنب')).toBeInTheDocument();
  expect(await screen.findByText('محشي كوسا')).toBeInTheDocument();
  expect(await screen.findByText('25 ريال')).toBeInTheDocument();
  expect(await screen.findByText('30 ريال')).toBeInTheDocument();
});